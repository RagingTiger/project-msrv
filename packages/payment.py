# custom lib
from . import catalog

# custom classes
class TrxLookUpError(Exception):
    """Exception raised when trasaction look up fails

    Attributes:
        trx -- The transaction data/object

    More Info:
        https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    """
    def __init__(self, trx):
        self.trx = trx

    def __str__(self):
        return 'Look up of transaction --> {} failed'.format(self.trx)

# custom funcs
def verify_trx(trx):
    """
        Check if transaction is legitimate
    """

    # verify if trx object is real
    return True

def validate(trx_data, inventory):
    """
        Validate purchase info
    """
    # verify transaction is real
    if not verify_trx(trx_data):
        raise TrxLookUpError(trx_data)

    # get items from trx_data
    items = trx_data

    # make sure prices in order match catalog price
    catalog.price_match(items, inventory)

    # create order dict with item name and file name (see: config/catalog.json)
    order = {key: inventory[key]['fname'] for key in items}

    # return order items
    return order
