# 3rd party libs
import flask

# custom lib
from packages import app_conf
from packages import catalog
from packages import cryptic

# create Flask instance
app = flask.Flask(__name__)

# setup initial app
app_conf.init(app)

# define route decorators
@app.route('/')
def front_page():
    return flask.render_template('index.html')

@app.route('/catalog')
def digital_catalog():
    # get digital catalog babay
    contents = catalog.get_contents(app)

    # render catalog page with catalog dictionary
    return flask.render_template('catalog.html', catalog=contents)

@app.route('/download/<pop>/<poe>/<item>')
def purchase_dwnldr(pop, poe, item):
    # check access and return file name, dir, mime type, and upload name
    try:
        fname, fdir, mtype, upname = catalog.get_item(app, pop, poe, item)
    except:
        # return standard 404 status code for curious hackers
        flask.abort(404)

    # if the client gets this far they deserve a prize
    return flask.send_from_directory(fdir,
                                     fname,
                                     mimetype=mtype,
                                     attachment_filename=upname,
                                     as_attachment=True)
