"""Console script for GitHub Automation Base."""

import typer
import asyncpg
import asyncio

from gh_automation_base.config import Config

app = typer.Typer()


async def hello_async() -> None:
    """Say hello to NAME asynchronously"""
    config = Config()
    connection = await asyncpg.connect(config.postgres.dsn)
    try:
        result = await connection.fetch("SELECT now();")
        print(result[0][0])
    finally:
        await connection.close()


@app.command()
def hello() -> None:
    """Say hello to NAME"""
    asyncio.run(hello_async())


def main() -> None:
    app()


if __name__ == "__main__":
    main()
