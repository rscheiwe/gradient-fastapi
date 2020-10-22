from fastapi import APIRouter

from gradient.api.routes import heartbeat
from gradient.api.routes.content_routes import unfamiliar_routes

api_router = APIRouter()

api_router.include_router(heartbeat.router, tags=['health'], prefix='/health')
api_router.include_router(unfamiliar_routes.router, tags=['unfamiliar-wow'])
