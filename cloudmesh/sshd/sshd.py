from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.systeminfo import os_is_linux
from cloudmesh.common.systeminfo import os_is_mac
from cloudmesh.common.console import Console
from cloudmesh.common.Shell import Shell


class Sshd:

    # implement cases for each os

    def __init__(self):
        pass

    def start(self):
        if os_is_windows():
            raise NotImplementedError
        elif os_is_linux():
            raise NotImplementedError
        elif os_is_mac():
            Console.warning('Go to System Preferences > Sharing, uncheck Remote Login, check Remote Login.')
        else:
            raise NotImplementedError

    def stop(self):
        if os_is_windows():
            raise NotImplementedError
        elif os_is_linux():
            raise NotImplementedError
        elif os_is_mac():
            Console.warning('Go to System Preferences > Sharing, uncheck Remote Login, uncheck Remote Login.')
        else:
            raise NotImplementedError

    def status(self):
        if os_is_linux():
            r = Shell.run("service sshd status").strip()
            return "running" in r
        elif os_is_windows():
            r = Shell.run("ps")
            return "sshd" in r
        elif os_is_mac():
            whoami = Shell.run('whoami').strip()
            # ssh -o StrictHostKeyChecking=no localhost hostname
            remote_whoami = Shell.run("ssh -o StrictHostKeyChecking=no localhost whoami").strip()
            return whoami == remote_whoami
        return False
