from pathlib import Path

from github import Github
import typer

from racoon.argument_types import DefaultSrcDir
from racoon.argument_types import DefaultTemplateURL
from racoon.argument_types import RequiredAccessToken
from racoon.git import init_template
from racoon.github_integration import GitHubIntegration
from racoon.template_generation import Context
from racoon.template_generation import generate_template
from racoon.template_generation import sanitize_repo_name

app = typer.Typer()


def read_file(path: Path) -> str:
    with open(path, "r") as file_pointer:
        return file_pointer.read().strip("\n")


@app.command()
def generate(
    project_name: str,
    github_access_token: Path = RequiredAccessToken,
    src_dir: str = DefaultSrcDir,
    template_url: str = DefaultTemplateURL,
) -> None:
    github = Github(login_or_token=read_file(path=github_access_token))
    repo_name = sanitize_repo_name(project_name)
    context = Context(github=github, repo_name=repo_name, src_dir=src_dir)
    generate_template(template_url=template_url, context=context)
    github_integration = GitHubIntegration(github=github)
    repo = github_integration.setup(repo_name=repo_name)
    init_template(repository=repo)


if __name__ == "__main__":
    app()
