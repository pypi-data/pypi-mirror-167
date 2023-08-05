"""Declares :class:`BaseEnvironmentConfig`"""
import copy
import os
from typing import Mapping

import pydantic


class BaseEnvironmentConfig(pydantic.BaseModel):

    @classmethod
    def parse_env(cls, env: Mapping[str, str] | None = None) -> 'BaseEnvironmentConfig':
        return cls.parse_obj(env or copy.deepcopy(os.environ))