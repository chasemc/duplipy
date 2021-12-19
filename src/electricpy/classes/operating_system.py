# python dependencies
from sys import platform
from typing import List

# internal dependencies
from electricpy.utils.logging_handler import log

supported_os = ["linux", "linux2", "darwin", "win32"]


class OperatingSystem:
    def __init__(
        self,
        this_operating_system: str = platform,  # make temppath default
    ):
        """Define the current operating system

        Args:
            this_operating_system (str, optional): Defaults to platform.

        Raises:
            ValueError: [description]
        """
        super().__init__()
        if this_operating_system in supported_os:
            response = this_operating_system
        else:
            message = "".join(
                [
                    "Operating system found: '",
                    str(this_operating_system),
                    "'. Must be one of: ",
                    ", ".join(supported_os),
                ]
            )
            log.error(message)
            raise ValueError(message)

        log.info("".join(["Operating system: ", response]))
        self.this_operating_system = response
