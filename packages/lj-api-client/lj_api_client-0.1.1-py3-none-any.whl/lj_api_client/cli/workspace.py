import typer
from rich import print

from lj_api_client.cli.utils import client

app = typer.Typer()


@app.command()
def list():
    '''
    Retrieve a list of workspace.
    '''
    print(client.get_workspaces().json())

@app.command()
def get(workspace_id: str):
    '''
    Fetch specific workspace.
    '''
    print(client.get_workspace(workspace_id).json())