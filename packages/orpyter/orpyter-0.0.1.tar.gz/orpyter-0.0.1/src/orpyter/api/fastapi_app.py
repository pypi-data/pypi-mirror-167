from typing import Any, Dict

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from orpyter import Orpyter
from orpyter.api.fastapi_utils import patch_fastapi


def launch_api(orpyter_path: str, port: int = 8501, host: str = "0.0.0.0") -> None:
    import uvicorn

    from orpyter import Orpyter
    from orpyter.api import create_api

    app = create_api(Orpyter(orpyter_path))
    uvicorn.run(app, host=host, port=port, log_level="info")


def create_api(orpyter: Orpyter) -> FastAPI:

    title = orpyter.name
    if "orpyter" not in orpyter.name.lower():
        title += " - Orpyter"

    # TODO what about version?
    app = FastAPI(title=title, description=orpyter.description)

    patch_fastapi(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post(
        "/call",
        operation_id="call",
        response_model=orpyter.output_type,
        # response_model_exclude_unset=True,
        summary="Execute the orpyter.",
        status_code=status.HTTP_200_OK,
    )
    def call(input: orpyter.input_type) -> Any:  # type: ignore
        """Executes this orpyter."""
        return orpyter(input)

    @app.get(
        "/info",
        operation_id="info",
        response_model=Dict,
        # response_model_exclude_unset=True,
        summary="Get info metadata.",
        status_code=status.HTTP_200_OK,
    )
    def info() -> Any:  # type: ignore
        """Returns informational metadata about this Orpyter."""
        return {}

    # Redirect to docs
    @app.get("/", include_in_schema=False)
    def root() -> Any:
        return RedirectResponse("./docs")

    return app
