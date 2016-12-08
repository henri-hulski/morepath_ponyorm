from pony.orm import db_session, commit, flush, rollback

import morepath
from morepath.reify import reify
from morepath.request import Request


class DBSessionRequest(Request):

    @reify
    def db_session(self):
        return db_session()

    @reify
    def db_commit(self):
        return commit

    @reify
    def db_flush(self):
        return flush

    @reify
    def db_rollback(self):
        return rollback


class App(morepath.App):
    request_class = DBSessionRequest
