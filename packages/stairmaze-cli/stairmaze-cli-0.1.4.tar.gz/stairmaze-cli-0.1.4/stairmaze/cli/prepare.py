import json
import os
from pathlib import Path
import shutil

from omegaconf import OmegaConf
import typer

from stairmaze.cli import check
from stairmaze.transformers.dag2sfn_definition import Dag2SFNDefintionTransformer
from stairmaze.transformers.task2job_definition import Task2JobDefinitionTransformer

app = typer.Typer()


@app.command()
def dag(
    file: Path = typer.Option(...),
    folder: Path = typer.Option(...),
    env: str = typer.Option("beta"),
):
    check.dag(file)

    typer.echo("Preparing dag templates (state machine and job definitions)")

    dag = OmegaConf.load(file)

    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

    job_definitions_folder = os.path.join(folder, "batch")
    os.makedirs(job_definitions_folder)

    for task in dag.tasks:
        job_definition = Task2JobDefinitionTransformer.transform(task)

        job_definition_filename = os.path.join(
            job_definitions_folder, f"{task.name}.json"
        )
        with open(job_definition_filename, "w") as fout:
            fout.write(job_definition)

    state_machine = Dag2SFNDefintionTransformer.transform(dag, env)

    output_filename = os.path.join(folder, "state_machine.json")
    with open(output_filename, "w") as fout:
        fout.write(json.dumps(state_machine, indent=4))
