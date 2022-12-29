from typing import List
from .model import Process, File, Event, IPAddress, Objects
from collections import defaultdict


OUTFLOW_OPERATION = ["write", "sendmsg", "writev", "rename", "renameat", "renameat2"]
processes = defaultdict(set)

def is_outflow_edge(oper):
    return oper in OUTFLOW_OPERATION

def handle_process_name(process: Process):
	processes[str(process.PID)].add(process.name)

def extract_nodes(log: dict):
	if 'ptid' in log['evt.args']:
		process = Process(ptid=log['evt.args']['ptid'])
		handle_process_name(process)
		return process, []
	elif 'oldpath' in log['evt.args']:
		old_path, new_path = File(path=log['evt.args']['oldpath']), File(path=log['evt.args']['newpath'])
		return old_path, [Event(old_path, log['evt.type'], new_path)]
	elif 'filename' in log['evt.args']:
		return File(log['evt.args']['filename']), []
	elif log['fd.type'] == 'file':
		return File(log['fd.name']), []
	elif log['fd.type'] and 'ipv' in log['fd.type']:
		return IPAddress(log), []
	elif log['fd.type']:
		return Objects(log), []
	return "", []

def extract_events(log: dict) -> Event:
	subject = Process(log=log)
	handle_process_name(subject)

	objct, extra_event = extract_nodes(log)
	extra_event.append(Event(subject, log['evt.type'], objct))
	return extra_event
	
def modifiy_events(events, processes):
	modified_events = []
	for event in events:
		if event.subject in processes:
			event.subject = f"{event.subject}({processes[event.subject]})"
		if event.object in processes:
			event.object = f"{event.object}({processes[event.object]})"
		if event.operation not in OUTFLOW_OPERATION:
			event.subject, event.object = event.object, event.subject
		if event.subject and event.object:
			modified_events.append(event)
	return modified_events	

def handle(parsed_logs: List[dict]):
	pending_events,	completed_event = {}, []

	for log in parsed_logs:
		events = extract_events(log)
		for event in events:
			key = event.key()

			if log['evt.dir'] == '>':
				event.start_time = log['evt.num']
				pending_events[key] = event
			elif log['evt.dir'] == '<':
				old_event = pending_events.get(key, event)
				old_event.set_etime(log['evt.num'])
				old_event.object = event.object if event.object else old_event.object
				pending_events.pop(key, None)
				completed_event.append(old_event)

	completed_event.extend(pending_events.values())

	return modifiy_events(completed_event, processes)
