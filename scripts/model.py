class Event:

    def __init__(self, sub, oper, obj, stime=None, etime=None) -> None:
        self.subject = str(sub)
        self.object = str(obj)
        self.operation = oper
        self.start_time = stime
        self.end_time = etime
        self.open = True

    def key(self):
        return f"{self.subject}###{self.operation}###{self.open}"
    
    def set_etime(self, etime):
        self.end_time = etime
        self.open = False

    def __repr__(self) -> str:
        return f"\n [ {self.subject}  ---  {self.operation}  ---  {self.object} ]"

class Process:
    
    def __init__(self, log=None, ptid=None) -> None:
        if ptid:
            if '(' not in ptid:
                self.PID = ptid
                self.name = ""
            else:
                self.PID, self.name = ptid.split('(', 2)
                self.name = self.name[:-1]
        else:
            self.PID, self.name = log['proc.pid'], log['proc.name']

    def __repr__(self) -> str:
        return f"{self.PID}"

class File:

    def __init__(self, name = None, path = None) -> None:
        if name:
            self.name = name 
        else:
            self.name = path if '(' not in path else path.split('(')[1][:-1]
    
    def __repr__(self) -> str:
        return f"[{self.name}]"

class IPAddress:

    def __init__(self, log) -> None:
        self.sIP = log['fd.sip']
        self.cIP = log['fd.cip']
        self.cport = log['fd.cport']
        self.sport = log['fd.sport']
        self.protocol = log['fd.l4proto']
    
    def __repr__(self) -> str:
        return f"[({self.protocol}){self.cIP};{self.cport}->{self.sIP};{self.sport}]"

class Objects:

    def __init__(self, log) -> None:
        self.fd_type = log['fd.type']
        self.fd_num = log['fd.uid']
        self.fd_name = log['fd.name']

    def __repr__(self) -> str:
        return f"{self.fd_type}({self.fd_num}[{self.fd_name}])"