from enum import Enum
from typing import List

import typer
from click import Choice
from pydantic import BaseModel

from lj_api_client import Client
from lj_api_client.cli.config import Config

class YesNoEnum(str, Enum):
    yes = 'yes'
    no = 'no'

def get_formatted_properties_from_schema(data, schema, definitions={}, prefix=''):
    properties = schema.get('properties', {})
    for property_name, property_data in properties.items():
        choices = None
        ref = property_data.get('$ref')
        required = property_name in schema.get('required', [])
        if ref:
            new_schema_name = ref.split('/')[-1]
            new_schema = definitions.get(new_schema_name, {})
            if not new_schema.get('enum'):
                get_formatted_properties_from_schema(data, new_schema, definitions=definitions, prefix=property_name)
                continue
            choices = new_schema['enum']
        all_of = property_data.get('allOf', [{}])[0].get('$ref')
        property_type = str if property_data.get('type', '') != 'array' else List[str]
        default = property_data.get('default')
        if all_of:
            choices = definitions[all_of.split('/')[-1]]['enum'] if all_of else None
        item = {
            'property_name': f'{prefix}.{property_name}' if len(prefix) else property_name,
            'required': required,
            'type': property_type,
            'default': default,
            'choices': choices
        }
        data.append(item) 
    return data

def prompt_schema_properties(schema: BaseModel):
    formatted_properties = get_formatted_properties_from_schema(
        [], schema.schema(), definitions=schema.schema()['definitions']
    )
    data = {}
    for property_data in formatted_properties:
        property_name = property_data['property_name']
        property_type = property_data['type']
        required = property_data['required']
        default_value = property_data['default']
        choices = property_data['choices']
        res = typer.prompt(
            text=f'{property_name}, separate values with commas' if property_type is List[str] else property_name,
            default=default_value if required else '',
            type=None if not choices else Choice(choices if required else choices + ['']),
        )
        if res != '' and property_type is List[str]:
            res = [el.strip() for el in res.split(',') if len(el)]

        if res == '':
            continue
        elif '.' in property_name:
            root, child = property_name.split('.')
            if not data.get(root):
                data[root] = {}
            data[root][child] = res
        else:
            data[property_name] = res
    return data

def init_client() -> Client:
    config_data = Config.get_config_data()
    api_key, host = config_data.get('api_key'), config_data.get('host')
    
    client = Client(
        api_key,
        host=host
    )

    return client

client = init_client()
