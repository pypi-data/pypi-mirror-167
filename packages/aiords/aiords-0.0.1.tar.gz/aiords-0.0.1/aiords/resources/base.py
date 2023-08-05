"""Declares :class:`BaseResource`."""
from cbra.resource import PublicResource


class BaseResource(PublicResource):
    __abstract__: bool = True
    __module__: str = 'aiords.resources'