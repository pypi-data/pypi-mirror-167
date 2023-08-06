from pathlib import Path

import typer

DEFAULT_ACCESS_TOKEN = Path.home().joinpath(".cache/github_token")
RequiredAccessToken: Path = typer.Option(default=DEFAULT_ACCESS_TOKEN, envvar="GITHUB_ACCESS_TOKEN")
DefaultSrcDir: str = typer.Option("src")
DefaultTemplateURL: str = typer.Option("https://github.com/nymann/python-template.git")
