"""Declares :class:`ProjectResource`."""
from typing import Any

import cbra

from aiords.models import Project
from .base import BaseResource
from .projectfile import ProjectFileResource


class ProjectResource(BaseResource):
    __module__: str = 'aiords.resources'
    path_name: str = "project"
    path_parameter: str = 'project_id'
    response_model: type[Project] = Project
    response_model_by_alias: bool = True
    name: str = "project"
    subresources: list[type[BaseResource]] = [ProjectFileResource]
    verbose_name: str = "Project"
    verbose_name_plural: str = "Projects"

    @cbra.summary("Publishes in service")
    @cbra.description("The project is published.")
    async def replace(self) -> None:
        """Publishes the project, if possible. This will disable any
        future changes to the given `projectId`.
        """
        raise NotImplementedError

    async def create(self) -> Project:
        """Add a new project to the service."""
        raise NotImplementedError

    @cbra.summary("Remove project from service")
    @cbra.description("The project is removed.")
    async def delete(self, project_id: str) -> None:
        """Removes the project from the backend service."""
        raise NotImplementedError

    async def list(self) -> list[Project]:
        """Returns all projects available in the service for user."""
        raise NotImplementedError

    @cbra.summary("Update metadata in service")
    @cbra.description("The project metadata is updated.")
    async def update(
        self,
        project_id: str,
        metadata: dict[str, Any] | None
    ) -> None:
        """Updates the metadata for the given project."""
        raise NotImplementedError