"""Declares :class:`OAuth2EnvironmentConfig`."""
import pydantic

from .base import BaseEnvironmentConfig


class OAuth2EnvironmentConfig(BaseEnvironmentConfig):
    backend_service: str = pydantic.Field(..., alias='BACKEND_SERVICE_URL')
    redirect_uri: str = pydantic.Field(..., alias='RDS_OAUTH_REDIRECT_URI')
    token_endpoint: str = pydantic.Field(..., alias='OAUTH_TOKEN_ENDPOINT')
    client_id: str = pydantic.Field(..., alias='OAUTH_CLIENT_ID')
    client_secret: str = pydantic.Field(..., alias='OAUTH_CLIENT_SECRET')
