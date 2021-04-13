from script import get_form, send

def routes(app):
    app.router.add_get('/', get_form)
    app.router.add_post('/', send, name='send')