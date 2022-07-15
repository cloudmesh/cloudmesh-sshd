from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.systeminfo import os_is_linux
from cloudmesh.common.systeminfo import os_is_mac

class Sshd:

    # implement cases for each os

    def __init__(self):
        raise NotImplementedError

    def start(self):
        if os_is_windows():
            raise NotImplementedError
        elif os_is_linux():
            raise NotImplementedError
        elif os_is_mac():
            raise NotImplementedError
        else:
            raise NotImplementedError

    def stop(self):
        if os_is_windows():
            raise NotImplementedError
        elif os_is_linux():
            raise NotImplementedError
        elif os_is_mac():
            raise NotImplementedError
        else:
            raise NotImplementedError

    def status(self):
        if os_is_windows():
            raise NotImplementedError
        elif os_is_linux():
            raise NotImplementedError
        elif os_is_mac():
            raise NotImplementedError
        else:
            raise NotImplementedError
