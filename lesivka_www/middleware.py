from google.cloud import ndb


def ndb_middleware(wsgi_app):
    client = ndb.Client()

    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware
