from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix="/api",
)

@base_router.get('/')
async def welcome():
    return "Hi, Atef!"