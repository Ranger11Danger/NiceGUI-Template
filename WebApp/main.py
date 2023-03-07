from nicegui import ui

# We need to import our login shit
import Auth.auth

# with how our templates are setup we can import any of our pages we want
from Pages import home

ui.run(dark=True, show=False, title='Template')