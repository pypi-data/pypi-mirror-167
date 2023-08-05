"""Contains parsers for environment variables."""
from .base import BaseEnvironmentConfig
from .oauth2 import OAuth2EnvironmentConfig


__all__: list[str] = [
    'BaseEnvironmentConfig',
    'OAuth2EnvironmentConfig'
]