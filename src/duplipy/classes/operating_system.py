# python dependencies
import platform
from typing import List


# internal dependencies
from duplipy.utils.logging_handler import log

class OperatingSystem:
    def __init__(
        self,
        verbose=False
    ):
        """Define the current operating system

        Args:
            this_operating_system (str, optional): Defaults to platform.

        Raises:
            ValueError: [description]
        """
        self.this_operating_system = {"Darwin": 'osx', "Linux": 'linux', "Windows": 'win' }[platform.system()]
        self.this_machine = platform.machine()
        if not self.this_operating_system:
            message = "".join(
                [
                    "Operating system not supported: '",
                    str(platform.system())
                ]
            )
            log.error(message)
            raise ValueError(message)
        if verbose:
            log.info("".join(["Operating system: ", self.this_operating_system]))
            log.info("".join(["Machine: ", self.this_machine]))

