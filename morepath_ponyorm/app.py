import logging

from pony.orm import db_session, TransactionError

import morepath


class App(morepath.App):
    pass


@App.setting_section(section='pony')
def get_pony_settings():
    return {
        'allowed_exceptions': [],
        'immediate': False,
        'retry': 0,
        'retry_exceptions': [TransactionError],
        'serializable': False,
        'strict': False
    }


@App.tween_factory(over=morepath.EXCVIEW)
def pony_tween_factory(app, handler):
    @db_session(
        allowed_exceptions=app.settings.pony.allowed_exceptions,
        immediate=app.settings.pony.immediate,
        retry=app.settings.pony.retry,
        retry_exceptions=app.settings.pony.retry_exceptions,
        serializable=app.settings.pony.serializable,
        strict=app.settings.pony.strict
    )
    def pony_tween(request):
        @request.after
        def after(response):
            logging.warning('Here is the @request.after of pony_tween.')

        logging.warning('Here is the pony_tween.')
        return handler(request)

    logging.warning('Here is the pony_tween_factory.')
    return pony_tween

@App.tween_factory(over=pony_tween_factory)
def side_effect_tween_factory(app, handler):
    def side_effect_tween(request):
        @request.after
        def after(response):
            logging.warning('Here is the @request.after of side_effect_tween.')

        logging.warning('Here is the side_effect_tween.')
        return handler(request)

    logging.warning('Here is the side_effect_tween_factory.')
    return side_effect_tween
