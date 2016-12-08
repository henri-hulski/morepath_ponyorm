import morepath
from pony.orm import sql_debug

from .app import App
from .model import db


def run():   # pragma: no cover
    db.bind('sqlite', 'user.db', create_db=True)
    db.generate_mapping(create_tables=True)

    # This shows the SQL query in console
    # Remove in production
    sql_debug(True)

    morepath.autoscan()
    morepath.run(App())
