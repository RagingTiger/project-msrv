# custom libs
from . import cryptic

# custom classes
class PurchaseError(Exception):
    """https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions"""
    pass

class ExpirationError(Exception):
    """https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions"""
    pass

# custom funcs
def get_contents(app):
    """
        Return select digital catalog contents.
    """
    # get reference to digitial catalog
    dc = app.config['DIGI_CATALOG']

    # generate name and price items dic from catalog
    catalog = {name: data["price"] for name, data in dc.items()}

    # give back
    return catalog

def get_item(app, pop, poe, item):
    """
        Check access and return item.
    """
    # get reference to digital catalog
    dc = app.config['DIGI_CATALOG']

    # check item in catalog and get file name, dir, mimetype, upload name
    file_name = dc[item]["fname"]
    file_dir = dc[item]["fdir"]
    mimetype = dc[item]["mime"]
    upload_name = dc[item]["upname"]

    # get new pointer to NONCE in app.config
    nonce_hash = app.config['NONCE_HASH']

    # get duplicate proof of purchase (PoP) for comparing with client PoP
    dup_pop = cryptic.sha256(file_name + nonce_hash)

    # check PoP submitted by client (similiar to BTC Proof of Work)
    if pop != dup_pop:
        # purchase not verified
        print('PurchaseError')
        print('Client PoP: {}'.format(pop))
        print('Server PoP: {}'.format(dup_pop))
        raise PurchaseError

    # generate Proof of Expiration (PoE) hash by scrambling PoP hash
    poe_nonce = cryptic.scramble_hash(dup_pop)

    # encode with current datetime
    dup_poe = cryptic.encode_dtime(poe_nonce)

    # check PoE submitted by client (similar to Proof of Purchase above)
    if poe <= dup_poe:
        # access has expired
        print('ExpirationError')
        print('Client PoE: {}'.format(poe))
        print('Server PoE: {}'.format(dup_poe))
        raise ExpirationError

    # give access to file_name at file_dir withe mime type and upload name
    return file_name, file_dir, mimetype, upload_name
