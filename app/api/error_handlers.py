from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def setup_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request, exc: Exception  # pylint: disable=unused-argument
    ) -> JSONResponse:
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
