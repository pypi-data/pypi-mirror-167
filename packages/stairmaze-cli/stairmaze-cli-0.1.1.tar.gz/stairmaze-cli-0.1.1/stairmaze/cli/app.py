import typer

from stairmaze.cli import check, prepare

app = typer.Typer()
app.add_typer(prepare.app, name="prepares")
app.add_typer(check.app, name="checks")

if __name__ == "__main__":  # pragma: no cover
    app()
