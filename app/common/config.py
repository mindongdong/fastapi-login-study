import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

class Settings(BaseSettings):
    ROUTES_STR: str = "/routes"
    SECRET_KEY: str = secrets.token_urlsafe(32)