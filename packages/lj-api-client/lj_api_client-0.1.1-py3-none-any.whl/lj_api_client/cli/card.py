import os
import json

import typer
from rich import print
from click import Choice

from lj_api_client import schemas
from lj_api_client.cli.utils import (
    client, 
    prompt_schema_properties
)

app = typer.Typer()


@app.command()
def list(workspace_id: str):
    '''
    Retrieve a list of card attached to a specific workspace.
    '''
    print(client.get_cards(workspace_id).json())

@app.command()
def get(workspace_id: str, card_id: str):
    '''
    Returns a single card.
    '''
    print(client.get_card(workspace_id, card_id).json())

@app.command()
def create(
    workspace_id: str, 
    data_file: str = typer.Argument('', help='Path of card data file in json format, if not provided enable interactive mode')
):
    '''
    Add a new card to a specific workspace.
    '''
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            card_data = json.load(f)
    else:
        card_data = prompt_schema_properties(schemas.CardCreationModel)
        print(card_data)
        confirmation: bool = typer.prompt(
            text=f'Confirm card creation ?',
            type=Choice(['yes', 'no']),
            default='yes',
        )
        if confirmation == 'no':
            return        

    return print(client.create_card(workspace_id, card_data).json())


@app.command()
def update(
    workspace_id: str, 
    card_id: str,
    data_file: str = typer.Argument('', help='Path of card data file in json format, if not provided enable interactive mode')
):
    '''
    Update card meta datas.
    '''
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            card_data = json.load(f)
    else:
        card_data = prompt_schema_properties(schemas.CardUpdateModel)
        print(card_data)
        confirmation: bool = typer.prompt(
            text=f'Confirm card update ?',
            type=Choice(['yes', 'no']),
            default='yes',
        )
        if confirmation == 'no':
            return        

    return print(client.update_card(workspace_id, card_id, card_data).json())

@app.command()
def delete(workspace_id: str, card_id: str, force: bool = False):
    '''
    Delete a card from its workspace.
    '''
    if not force:
        confirmation: bool = typer.prompt(
            text=f'Permanently delete card {card_id} ?',
            type=Choice(['no', 'yes']),
            default='no',
        )
        if confirmation == 'no':
            return
    return print(client.delete_card(workspace_id, card_id).json())

@app.command()
def upload_data(
    workspace_id: str, 
    card_id: str, 
    log_file: str = typer.Argument(..., help='Log data file path'),
    desc_file: str = typer.Option(None, help='Descriptive data file path')
    ):
    '''
    Upload log and descriptive data to a card.
    '''
    client.upload_data_to_card(workspace_id, card_id, log_file, desc_file_path=desc_file)
    print('Data upload launched!')

