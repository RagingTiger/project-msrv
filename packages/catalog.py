# custom libs
from . import cryptic

# custom classes
class PurchaseError(Exception):
    """Exception raised when price mismatch of order and catalog items

    Attributes:
        cli_pop -- The client's Proof of Purchase sha256 hash
        srv_pop -- The server's Proof of Purchase sha256 hash

    More Info:
        https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    """
    def __init__(self, client_pop, server_pop, item):
        self.cli_pop = client_pop
        self.srv_pop = server_pop
        self.item = item

    def __str__(self):
        purch_err = (
                    'Client Pop: {}\n'
                    'Server PoP: {}\n'
                    'Client does not have access to item: {}'
                    ).format(self.cli_pop, self.srv_pop, self.item)
        return purch_err

class ExpirationError(Exception):
    """Exception raised when price mismatch of order and catalog items

    Attributes:
        cli_poe -- The client's Proof of Expiration sha256 hash
        srv_poe -- The server's sha256 hash of current datetime

    More Info:
        https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    """
    def __init__(self, client_poe, server_poe, item):
        self.cli_poe = client_poe
        self.srv_poe = server_poe
        self.item = item

    def __str__(self):
        exp_err = (
                    'Client PoE: {}\n'
                    'Server current datetime sha256 Hash: {}\n'
                    'Client\'s access to following item has expired: {}'
                    ).format(self.cli_poe, self.srv_poe, self.item)
        return exp_err

class PriceMatchError(Exception):
    """Exception raised when price mismatch of order and catalog items

    Attributes:
        trx -- The transaction data/object

    More Info:
        https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    """
    def __init__(self, item, price, cat_entry):
        self.item = item
        self.price = price
        self.cat_entry = cat_entry

    def __str__(self):
        mismatch = ('Price mismatch occured for:\n'
                    '{}: {}\n'
                    'Catalog Entry: {}'
                    ).format(self.item, self.price, self.cat_entry)
        return mismatch

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
        raise PurchaseError(pop, dup_pop, item)

    # generate Proof of Expiration (PoE) hash by scrambling PoP hash
    poe_nonce = cryptic.scramble_hash(dup_pop)

    # encode with current datetime
    dup_poe = cryptic.encode_dtime(poe_nonce)

    # check PoE submitted by client (similar to Proof of Purchase above)
    if poe <= dup_poe:
        # access has expired
        raise ExpirationError(poe, dup_poe, item)

    # give access to file_name at file_dir withe mime type and upload name
    return file_name, file_dir, mimetype, upload_name

def price_match(order, catalog):
    """
        Check that prices in order match prices in catalog
    """
    # iterate through order
    for item, price in order.items():
        # check if catalog item price matches order price
        if catalog[item]['price'] != price:
            # if mismatch found log and raise error
            raise PriceMatchError(item, price, catalog[item])
