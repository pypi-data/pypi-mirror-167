import typer
from rich import print

from lj_api_client import Client
from lj_api_client.cli.utils import client
from lj_api_client.cli.config import Config
from lj_api_client.cli import workspace, card

app = typer.Typer()

app.add_typer(workspace.app, name='workspace', help='Workspace operations. Try `ljcli workspace --help` for more infos')
app.add_typer(card.app, name='card', help='Card operations. Try `ljcli card --help` for more infos')

@app.command()
def login(
    host: str = typer.Option(Client.DEFAULT_HOST, prompt=True), 
    api_key: str = typer.Option(..., prompt=True, hide_input=True)
):
    '''
    Store your api key and host in config file
    '''
    Config.update_config(**{
        'api_key': api_key,
        'host': host
    })

@app.command()
def user():
    '''
    Fetch logged user infos
    '''
    print(client.get_user().json())
           

