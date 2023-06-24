"""Console script for GitHub Automation Base."""

import typer


app = typer.Typer()


@app.command()
def hello(name: str) -> None:
    """Say hello to NAME"""
    typer.echo(f"Hello {name}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
