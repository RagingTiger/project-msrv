# std lib
import json

# custom libs
from . import cryptic

# custom func
def init(app):
    """
        Setup initial flask app
    """
    # get digital catalog
    with app.open_resource('config/catalog.json') as dc:
        # add digital catalog to app config dict
        app.config['DIGI_CATALOG'] = json.load(dc)

    # get sha256 hash of NONCE environment variable and add to app config dic
    app.config['NONCE_HASH'] = cryptic.get_nonce_hash()
