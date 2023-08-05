"""Declares :class:`File`."""
import pydantic


class File(pydantic.BaseModel):
    id: str
    filename: str
    content: str