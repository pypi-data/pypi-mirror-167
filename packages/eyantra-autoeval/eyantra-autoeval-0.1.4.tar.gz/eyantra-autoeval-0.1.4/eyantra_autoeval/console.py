# standard imports
import importlib

# third-party imprts
import click
from rich import print


@click.group()
def cli():
    pass


@click.command()
@click.option("--year", required=True, help="Year.")
@click.option("--theme", required=True, help="Theme Initials.")
@click.option("--task", required=True, help="Task Number.")
def evaluate(year, theme, task):
    """Dry run evaluation for a task."""
    print(
        f"Running evaluation scripts for [bold blue]{year}[/bold blue] "
        f"theme [bold blue]{theme}[/bold blue] for "
        f"task [bold blue]{task}[/bold blue]"
    )
    evaluator = importlib.import_module(
        f"eyantra_autoeval.year.y{year}.{theme}.task{task}.evaluator"
    )
    evaluator.evaluate()


cli.add_command(evaluate)

