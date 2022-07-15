from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.variables import Variables
from cloudmesh.common.util import banner

class SshdCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_sshd(self, args, arguments):
        """
        ::

          Usage:
                sshd status
                sshd start
                sshd stop

          This stats and stops the sshd service on the local machine.


          Description:

            cms sshd start
                starts the sshd service

            cms sshd stop
                stopss the sshd service

            cms status
                returns "running" when it runs. otherwise "error"

        """
        # from clousmesh.sshd.sshd import Sshd
        # sshd = Sshd()

        if arguments.start:
            Console.ok("Starting...")
            raise NotImplementedError

        elif arguments.stop:
            Console.ok("Stoping...")
            raise NotImplementedError

        elif arguments.status:
            raise NotImplementedError


        return ""
