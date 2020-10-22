from fastapi import FastAPI

from gradient.api.routes.router import api_router
from gradient.core.config import (API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG)


def get_app() -> FastAPI:
    gradient = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    gradient.include_router(api_router, prefix=API_PREFIX)

    return gradient


app = get_app()
