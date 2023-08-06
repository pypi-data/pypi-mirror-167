# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lj_api_client', 'lj_api_client.cli']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['ljcli = lj_api_client.cli:app']}

setup_kwargs = {
    'name': 'lj-api-client',
    'version': '0.1.1',
    'description': 'API client for Livejourney App',
    'long_description': '<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->\n<a name="readme-top"></a>\n\n<!-- PROJECT LOGO -->\n<br />\n<div align="center">\n  <a href="https://www.livejourney.com/">\n    <img src="https://www.livejourney.com/wp-content/uploads/2021/06/cropped-logo-livejourney-frenchtech.png" alt="Logo" width="300" height="86">\n  </a>\n\n  <h3 align="center">Live Journey API Client</h3>\n\n  <p align="center">\n    A Client to interact with Live journey API easily\n    <br />\n    <a href="https://public-api.livejourney.io/api/v1/docs/"><strong>Explore the API docs</strong></a>\n    <br />\n    <br />\n  </p>\n</div>\n\n\n<!-- TABLE OF CONTENTS -->\n<details>\n  <summary>Table of Contents</summary>\n  <ol>\n    <li>\n      <a href="#getting-started">Getting Started</a>\n      <ul>\n        <li><a href="#prerequisites">Prerequisites</a></li>\n        <li><a href="#installation">Installation</a></li>\n      </ul>\n    </li>\n    <li><a href="#usage">Usage</a></li>\n    <li><a href="#cli">CLI</a></li>    \n    <li><a href="#contact">Contact</a></li>\n  </ol>\n</details>\n\n\n<!-- GETTING STARTED -->\n## Getting Started\n\n\n### Prerequisites\n\nIn order to login the client you will have to authenticate yourself via your API KEY. If you don\'t have/lost your api key please contact our tech team at api@livejourney.com in order to generate a new one.\n\n### Installation\n\nInstall and update using pip:\n```\n    pip install -U lj-api-client\n```\n\n<p align="right">(<a href="#readme-top">back to top</a>)</p>\n\n\n\n<!-- USAGE EXAMPLES -->\n## Usage\n\nThe client allows you to build request in a more convinient way thus speed up your integration with the live journey app.\n```\n# Init client\nfrom lj_api_client import Client\n\napi_key = \'{YOUR API KEY HERE}\'\nclient = Client(api_key)\n\n# Get current user\nres = client.users.fetch_list() \n\n# List workspaces\nres = client.workspaces.fetch_list()\n\n# Get specific worksapce\nworkspace_id = \'{WORKSPACE_ID}\'\nres = client.workspaces.fetch_item(workspace_id)\n\n# List workspace cards\nworkspace_id = \'{WORKSPACE_ID}\'\nres = client.workspaces.cards(workspace_id).fetch_list()\n\n# Get specific card\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nres = client.workspaces.cards(workspace_id).fetch_item(card_id)\n\n# Create new card\nworkspace_id = \'{WORKSPACE_ID}\'\n# Card data see our API Docs for in depth specification\ncard_data = {\n    \'name\': \'my-new-card\',\n    \'unit_name\': \'Unit\',\n    \'permission\': \'public\',\n    \'key_mapping\': {\n        \'unit_key\': \'{YOUR UNIT KEY}\',\n        \'date_format\': \'{YOUR DATE FORMAT}\',\n        \'event_keys\':[\n            \'{YOUR EVENT KEY}\',\n        ],\n        \'date_keys\':[\n            \'{YOUR DATE KEY}\',\n        ],        \n    }\n}\nres = client.workspaces.cards(workspace_id).create_item(card_data)\n\n# Update card\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\ncard_new_data = {\n    \'name\': \'new-name\'\n}\nres = client.workspaces.cards(workspace_id).update_item(\n        card_id,\n        card_new_data\n    )\n\n# Delete card\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nres = client.workspaces.cards(workspace_id).delete(card_id)\n\n# Get card presigned url\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nparams = {\'data_type\': \'log\'}\nres = client.workspaces.cards(workspace_id).presigned_url(card_id).fetch_list(params=params)\n\n# Feed card\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nres = client.workspaces.cards(workspace_id).feed(card_id).create_item({})\n\n```\n\nThe client also validate the requests via its higher level API\n```\nres = client.get_user()\n\nres = client.get_workspaces()\n\nworkspace_id = \'{WORKSPACE_ID}\'\nres = client.get_workspace(workspace_id)\n\nworkspace_id = \'{WORKSPACE_ID}\'\nres = client.get_cards(workspace_id)\n\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nres = client.get_card(workspace_id, card_id)\n\nworkspace_id = \'{WORKSPACE_ID}\'\ncard_data = {\n    \'name\': \'my-new-card3\',\n    \'unit_name\': \'Unit\',\n    \'permission\': \'public\',\n    \'key_mapping\': {\n        \'unit_key\': \'{YOUR UNIT KEY}\',\n        \'date_format\': \'{YOUR DATE FORMAT}\',\n        \'event_keys\':[\n            \'{YOUR EVENT KEY}\',\n        ],\n        \'date_keys\':[\n            \'{YOUR DATE KEY}\',\n        ],        \n    }\n}\nres = client.create_card(workspace_id, card_data)\n\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nres = client.update_card(workspace_id, card_id, card_new_data)\n\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nres = client.delete_card(workspace_id, card_id)\n\nworkspace_id, card_id = \'{WORKSPACE_ID}\', \'{CARD_ID}\'\nlog_file_path, desc_file_path = \'{LOG DATA FILE PATH}\', \'{DESC DATA FILE PATH}\'\nres = client.upload_data_to_card(\n  workspace_id, \n  card_id, \n  log_file_path, \n  desc_file_path=desc_file_path\n)\n```\n\nFor more examples, please refer to the examples directory\n\n<p align="right">(<a href="#readme-top">back to top</a>)</p>\n\n## CLI\nYou can also interact with the API directly from the terminal using our CLI. See the interactive doc `ljcli --help` for more infos.\n\n<p align="right">(<a href="#readme-top">back to top</a>)</p>\n\n\n<!-- CONTACT -->\n## Contact\n\napi@livejourney.com\n\n\n<p align="right">(<a href="#readme-top">back to top</a>)</p>',
    'author': 'Livejourney',
    'author_email': 'api@livejourney.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
