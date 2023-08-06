"""Command line interface."""

import os
import sys

import typer
from pydantic.error_wrappers import ValidationError

from orpyter.export import ExportFormat

cli = typer.Typer()


@cli.command()
def launch_ui(orpyter: str, port: int = typer.Option(8051, "--port", "-p")) -> None:
    """Start a graphical UI server for the orpyter.

    The UI is auto-generated from the input- and output-schema of the given function.
    """
    from orpyter.ui.streamlit_ui import launch_ui  # type: ignore

    launch_ui(orpyter, port)


@cli.command()
def launch_api(
    orpyter: str,
    port: int = typer.Option(8080, "--port", "-p"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
) -> None:
    """Start a HTTP API server for the orpyter.

    This will launch a FastAPI server based on the OpenAPI standard and with an automatic interactive documentation.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the orpyter path
    sys.path.append(os.getcwd())

    from orpyter.api.fastapi_app import launch_api  # type: ignore

    launch_api(orpyter, port, host)


@cli.command()
def call(orpyter: str, input_data: str) -> None:
    """Execute the orpyter from command line."""
    # Add the current working directory to the sys path
    # This is required to resolve the orpyter path
    sys.path.append(os.getcwd())

    try:
        from orpyter import Orpyter

        output = orpyter(orpyter)(input_data)
        if output:
            typer.echo(output.json(indent=4))
        else:
            typer.echo("Nothing returned!")
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)


@cli.command()
def export(
    orpyter: str, export_name: str, format: ExportFormat = ExportFormat.ZIP
) -> None:
    """Package and export an orpyter."""
    if format == ExportFormat.ZIP:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: https://github.com/ml-tooling/orpyter/issues/3",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.DOCKER:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: https://github.com/ml-tooling/orpyter/issues/4",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.PEX:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: https://github.com/ml-tooling/orpyter/issues/5",
            fg=typer.colors.BRIGHT_YELLOW,
        )


@cli.command()
def deploy(orpyter: str) -> None:
    """Deploy an orpyter to a cloud platform.

    This provides additional features such as SSL, authentication, API tokens, unlimited scalability, load balancing, and monitoring.
    """
    typer.secho(
        "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: https://github.com/ml-tooling/orpyter/issues/6",
        fg=typer.colors.BRIGHT_YELLOW,
    )
