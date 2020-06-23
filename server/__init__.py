# 3rd party libs
import flask

# custom lib
from packages import app_conf
from packages import catalog
from packages import cryptic
from packages import error
from packages import payment

# create Flask instance
app = flask.Flask(__name__)

# setup initial app
app_conf.init(app)

# define route decorators
@app.route('/')
def front_page():
    return flask.render_template('index.html')

@app.route('/cart')
def view_cart():
    return flask.render_template('cart.html')

@app.route('/checkout')
def checkout():
    return flask.render_template('checkout.html')

@app.route('/catalog')
def digital_catalog():
    # get digital catalog babay
    contents = catalog.get_contents(app)

    # render catalog page with catalog dictionary
    return flask.render_template('catalog.html', catalog=contents)

@app.route('/download/<pop>/<poe>/<item>')
def purchase_dwnldr(pop, poe, item):
    try:
        # check access and return file name, dir, mime type, and upload name
        fname, fdir, mtype, upname = catalog.get_item(app, pop, poe, item)

    except Exception as err:
        # print out error
        error.print_error(err, 'Download access failed with')

        # return standard 404 status code for curious hackers
        flask.abort(404)

    # if the client gets this far they deserve a prize
    return flask.send_from_directory(fdir,
                                     fname,
                                     mimetype=mtype,
                                     attachment_filename=upname,
                                     as_attachment=True)

@app.route('/purchases', methods=['POST'])
def view_purchases():
    try:
        # make sure payment is legit
        order = payment.validate(flask.request.form, app.config['DIGI_CATALOG'])

    except Exception as err:
        # print out error
        error.print_error(err, 'Payment validation failed with')

        # return 418 status code for sh!ts and gigs
        flask.abort(418)

    else:
        # create download links
        downloads = cryptic.gen_download_links(app.config['NONCE_HASH'], order)

    # render purchases page with all the yummy download links
    return flask.render_template('purchases.html', downloads=downloads)
