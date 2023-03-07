from typing import Dict

from nicegui import ui
from fastapi import Request

import sys
sys.path.append("../Auth")

def base(session):
    
    with ui.header() as header:
        with ui.row().classes("w-full justify-between"):
            ui.button(on_click=lambda: left_drawer.toggle()).props('flat color=white icon=menu')
            with ui.row():
                with ui.menu() as menu:
                    ui.menu_item("Profile", lambda: ui.open("/user"))
                    ui.menu_item("Logout", lambda: ui.open("/logout"))
                ui.button(on_click=menu.open).props('flat color=white icon=account_circle')
    with ui.left_drawer()as left_drawer:
        ui.label('Side menu')

