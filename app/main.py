import logging
from fastapi import APIRouter, FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

# reading config file
from .shared.config import config

from .controllers import PlayerController

# default start
app = FastAPI()
router = APIRouter()

# adding classes to handle exceptions


class ExceptionHandlerClass(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(ExceptionHandlerClass)
async def unicorn_exception_handler(request: Request, exc: ExceptionHandlerClass):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    logging.error(f"{request}: {exc_str}")
    content = {'status_code': 422, 'message': exc_str, 'data': None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.get("/", tags=["Home"])
async def home():
    return {"message": "Welcome to " + config['SERVICE_NAME']}

# including routes
app.include_router(router)
app.include_router(PlayerController.router)
