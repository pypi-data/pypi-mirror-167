"""Declares :class:`Project`."""
from typing import Any

import pydantic


class Project(pydantic.BaseModel):
    project_id: str = pydantic.Field(
        default=...,
        title="Project ID",
        alias="projectId",
        description="Identifies the project."
    )

    metadata: dict[str, Any] = pydantic.Field(
        default={},
        title="Metadata",
        description="Metadata object describing the project."
    )