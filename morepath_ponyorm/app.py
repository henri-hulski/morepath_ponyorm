from pony.orm import db_session

import morepath
from morepath.reify import reify
from morepath.request import Request


class DBSessionRequest(Request):

    @reify
    def db_session(self):
        return db_session()


class App(morepath.App):
    request_class = DBSessionRequest
