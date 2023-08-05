"""Declares :class:`Port`."""
from typing import Any

from cbra import Application
from RDS import FileTransferMode
from RDS import FileTransferArchive

from .resources import ProjectResource


class Port(Application):
    """Base implementation for all ports used with RDS."""
    __module__: str = 'aiords'
    archive: FileTransferArchive
    description: str
    display_name: str
    help_url: str
    implements: list[str]
    info_url: str
    name: str
    transfer_mode: FileTransferMode

    def __init__(
        self,
        name: str,
        display_name: str,
        description: str,
        implements: list[str],
        transfer_mode: FileTransferMode,
        archive: FileTransferArchive,
        info_url: str,
        help_url: str,
        *args: Any,
        **kwargs: Any
    ):
        kwargs.setdefault('docs_url', '/ui')
        kwargs.setdefault('redoc_url', '/')
        super().__init__(*args, **kwargs)
        self.archive = archive
        self.description = description
        self.display_name = display_name
        self.help_url = help_url
        self.implements = implements
        self.info_url = info_url
        self.name = name
        self.transfer_mode = transfer_mode

    async def boot(self):
        await super().boot()
        self.add(ProjectResource)