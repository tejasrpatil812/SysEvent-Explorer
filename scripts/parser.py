import json

LOG_DIR = "./data_files/logs.txt"

def load_file(file_name: str = LOG_DIR):
	with open(file_name) as f:
		logs = f.readlines()
	return logs

def parse_log(log: str):
	parsed_dict = json.loads(log)
	event_args = parsed_dict['evt.args']

	parserd_event_args = {}
	for word in event_args.split(' '):
		try:
			key, value = word.split('=', 1)
			parserd_event_args[key]=value
		except:
			pass
	
	parsed_dict['evt.args'] = parserd_event_args

	return parsed_dict


def handle(file_name=None):
	logs = load_file(file_name) if file_name else load_file()
	parsed_logs = []
	for log in logs:
		parsed_logs.append(parse_log(log))
	
	return parsed_logs