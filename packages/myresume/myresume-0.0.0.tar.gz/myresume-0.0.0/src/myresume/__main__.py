"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """MyResume."""


if __name__ == "__main__":
    main(prog_name="myresume")  # pragma: no cover
