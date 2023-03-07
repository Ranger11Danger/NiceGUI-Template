import uuid
from typing import Dict

from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import sys
sys.path.append("../Utils")
from Utils.db_utils import client

from nicegui import app, ui

app.add_middleware(SessionMiddleware, secret_key='some_random_string')  # use your own secret key here

session_info: Dict[str, Dict] = {}

def is_authenticated(request: Request) -> bool:
    # we disable auth so we can speed up dev times for now
    return session_info.get(request.session.get('id'), {}).get('authenticated', False)
    #return True

@ui.page('/user')
def main_page(request: Request) -> None:
    if not is_authenticated(request):
        return RedirectResponse('/login')
    session = session_info[request.session['id']]
    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Hello {session["username"]}!').classes('text-2xl')
        ui.button('', on_click=lambda: ui.open('/logout')).props('outline round icon=logout')


@ui.page('/login')
def login(request: Request) -> None:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        response = client.query(f"SELECT * FROM user where username='{username.value}' && password='{password.value}'")
        if len(response[0]["result"]) == 1:
            session_info[request.session['id']] = {'username': username.value, 'authenticated': True}
            ui.open('/')
        else:
            ui.notify('Wrong username or password', color='negative')

    if is_authenticated(request):
        return RedirectResponse('/')
    request.session['id'] = str(uuid.uuid4())  # NOTE this stores a new session ID in the cookie of the client
    with ui.card().classes('absolute-center w-96 items-center items-stretch'):
        ui.label("Login").classes("self-center text-2xl")
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password').props('type=password').on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)


@ui.page('/logout')
def logout(request: Request) -> None:
    if is_authenticated(request):
        session_info.pop(request.session['id'])
        request.session['id'] = None
        return RedirectResponse('/login')
    return RedirectResponse('/')


ui.run()