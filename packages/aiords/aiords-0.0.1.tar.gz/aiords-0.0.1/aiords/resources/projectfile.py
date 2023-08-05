"""Declares :class:`ProjectFileResource`."""
from aiords.models import File
from .base import BaseResource


class ProjectFileResource(BaseResource):
    __module__: str = 'aiords.resources'
    path_parameter: str = 'file_id'
    path_name: str = 'files'
    verbose_name: str = "File"
    verbose_name_plural: str = "Files"

    async def list(self, project_id: str) -> list[File]:
        """Lists all the files for a given project."""
        raise NotImplementedError

    async def retrieve(self) -> File:
        """Get the specified file."""
        raise NotImplementedError