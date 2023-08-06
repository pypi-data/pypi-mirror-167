import json
import sys, inspect
import importlib

from beam import App

def build() -> str:
    app_modules = importlib.import_module(("app"))
    beamapp = None

    for member in inspect.getmembers(app_modules):
        member_value = member[1]
        if isinstance(member_value, App):
            beamapp = member_value
            break

    if beamapp is not None:
        return json.dumps(beamapp.dumps(), indent=4)
    
    raise Exception("Beam app not found")

