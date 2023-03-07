import sys
import json
sys.path.append("../Templates")
sys.path.append("../Utils")
from Templates.base import base
from fastapi import Request
from fastapi.responses import RedirectResponse
from nicegui import ui
from Auth.auth import is_authenticated, session_info
import Utils.db_utils as db_utils

@ui.page("/")
def home(request: Request):
    if not is_authenticated(request):
        return RedirectResponse('/login')
    # temp disabled so i dont have to keep logging in
    #session = session_info[request.session['id']]
    session = None
    base(session)
    
    