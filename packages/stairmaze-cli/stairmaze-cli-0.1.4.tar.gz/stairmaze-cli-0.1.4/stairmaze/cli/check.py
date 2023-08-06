from pathlib import Path

from omegaconf import OmegaConf
import typer

from stairmaze.checker import Checker
from stairmaze.exceptions import CycleDetected, NoRootDag

app = typer.Typer()


@app.command()
def dag(file: Path = typer.Option(...)):
    typer.echo("Checking dag configuration")

    dag = OmegaConf.load(file)

    try:
        Checker.check_dag(dag)
    except NoRootDag as e:
        typer.echo("Failed due to: " + str(e))
        raise typer.Exit(code=1)
    except CycleDetected as e:
        typer.echo("Failed due to: " + str(e))
        raise typer.Exit(code=1)
