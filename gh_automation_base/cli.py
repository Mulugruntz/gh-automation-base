"""Console script for GitHub Automation Base."""

import typer
import asyncpg
import asyncio

from gh_automation_base.config import Config
from gh_automation_base.persistence.init import cmd_init, cmd_clean

app = typer.Typer()


async def time_async() -> None:
    """Get the time from the DB and prints it."""
    config = Config()
    connection = await asyncpg.connect(config.postgres.dsn)
    try:
        result = await connection.fetch("SELECT now();")
        typer.echo(result[0][0])
    finally:
        await connection.close()


@app.command()
def time() -> None:
    """Show the time in the DB."""
    asyncio.run(time_async())


@app.command()
def dsn() -> None:
    """Print the DSN."""
    config = Config()
    typer.echo(config.postgres.dsn)


@app.command()
def init() -> None:
    """Initialize a new project"""
    config = Config()
    asyncio.run(cmd_init(config))


@app.command()
def clean() -> None:
    """Clean the database"""
    config = Config()
    asyncio.run(cmd_clean(config))


def main() -> None:
    app()


if __name__ == "__main__":
    main()
