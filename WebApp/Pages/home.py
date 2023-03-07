import sys
sys.path.append("../Templates")
from Templates.base import base

from fastapi import Request
from fastapi.responses import RedirectResponse
from nicegui import ui
from Auth.auth import is_authenticated, session_info

@ui.page("/")
def home_page(request: Request):
    if not is_authenticated(request):
        return RedirectResponse('/login')
    session = session_info[request.session['id']]
    base(session)
    
    