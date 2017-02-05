import logging

from .app import App


@App.signal.on_any()
def log_event_emitter(location):
    logging.warning('Here is the %s.' % location)
