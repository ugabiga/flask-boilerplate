import fnmatch
import os
from typing import Any, Dict

import yaml

from app.__meta__ import __api_name__, __version__

_swagger_definition = {}


def get_swagger_config() -> Dict[str, Dict[str, Any]]:
    return {
        "config": {
            "headers": [],
            "specs": [
                {
                    "endpoint": "apispec",
                    "route": "/apispec.json",
                    "rule_filter": lambda rule: True,  # all in
                    "model_filter": lambda tag: True,  # all in
                }
            ],
            "static_url_path": "/group/flasgger_static",
            "swagger_ui": True,
            "specs_route": "/apidoc",
        },
        "template": {
            "swagger": "2.0",
            "info": {
                "title": __api_name__,
                "description": "Glam group server",
                "version": __version__,
                "contact": {
                    "responsibleOrganization": "ME",
                    "responsibleDeveloper": "Me",
                    "email": "me@me.com",
                    "url": "www.me.com",
                },
                "termsOfService": "http://me.com/terms",
            },
            "host": "localhost:5000",  # overrides localhost:500
            "basePath": "",  # base bash for blueprint registration
            "schemes": ["http", "https"],
            "operationId": "getmyData",
            "definitions": _swagger_definition,
            "securityDefinitions": {
                "Token Bearer": {
                    "type": "apiKey",
                    "name": "Authorization",
                    "in": "header",
                    "description": "Access Token",
                    "bearerFormat": "JWT",
                }
            },
        },
    }


def import_definitions() -> None:
    working_folder_path = os.path.dirname(os.path.realpath(__file__))
    for path, sub_dir, files in os.walk(working_folder_path):
        for file_name in files:
            if fnmatch.fnmatch(file_name, "*.yml"):
                definition_doc = yaml.full_load(open(os.path.join(path, file_name)))
                _swagger_definition.update(definition_doc)


import_definitions()
