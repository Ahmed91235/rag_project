from fastapi import FastAPI, APIRouter, Depends
from core.config import get_settings, Settings
import os
base_router = APIRouter(
    prefix="/api",
)

@base_router.get('/')
async def welcome(app_settings: Settings = Depends(get_settings)):
    
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return F"{app_name}:{app_version} is running successfully."