## tl;dr
Example of a `Digital Download` platform/business model using `Flask` in
`Python 3`, `Docker`, and plenty of `Cryptographic` goodness.

## Introduction
The repository depicts an example of how a `Digital Download` platform might be
constructed using `Flask`, `Python 3`, `Docker`, and `Cryptography`, with an
eye towards a `stateless` design. The example chosen for the website, is a
fictitious group of *recording artists* and *musicians* known as `Project MSRV`
(or simply `MSRV` as the fans call them.)

## Design
`TODO` hehehehe

## Usage
There are a few ways to use the repository, and we will document two of those
ways:
  + `Python 3` Virtual Environment Deployment
  + `Docker` Deployment

### Python
**Note**: This requires you to have `VirtualEnv` installed
The simplest way to setup a `Python 3` virtual environment:
```
$ git clone https://github.com/RagingTiger/project-msrv
$ cd project-msrv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

You must set a value for the `NONCE` environment variable (see
[Nonce Environment Variable](#nonce-environment-variable)):
```
$ export NONCE='Never Gonna Give You Up'
```

Finally set the `FLASK_APP` variable to `server` and then run `flask`:
```
$ export FLASK_APP='server'
$ flask run
```
You should see output similar to this:
```
 * Serving Flask app "server" (lazy loading)
 * Environment: production
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```
Open http://localhost:5000 to browse the website.

### Docker
A `Dockerfile` is provided in the repository to build a `Docker` image from.
Prebuilt images are available at
[tigerj/msrv](https://hub.docker.com/r/tigerj/msrv)

#### Run
To simply run the example platform, using the default `NONCE` value (see
[Nonce Environment Variable](#nonce-environment-variable)):
```
$ docker run -d --name msrv -p 5000:5000 tigerj/msrv
```
Then navigate to http://localhost:5000 to browse the platform.

#### Stop
To stop the running container:
```
$ docker stop msrv
```

#### Remove
To remove a stopped container:
```
$ docker rm msrv
```

#### Build
If you would like to build the container (e.g. for your system's architecture):
```
$ git clone https://github.com/RagingTiger/project-msrv
$ cd project-msrv
$ docker build -t msrv .
```
**Note**: naturally you can name the image (after `-t` option) whatever you like
here we simply chose `msrv` for .... well simplicity.

### Docker Image Features
There are some key features to understand about using this example platform:
  + **1**: `NONCE` Environment Variable
  + **2**: Flask Port `5000`

#### Nonce Environment Variable
The `NONCE` value uses a default setting found in the `Dockerfile` and is
necessary for the cryptography. **Note**: if you are planning to use **this
source code** to build your own platform, it is highly recommended to set your
own `NONCE` variable to some unique value. For example when running the `Docker`
image:
```
$ docker run -d \
             --name msrv \
             -e NONCE='Never Gonna Give You Up' \
             -p 5000:5000
             tigerj/msrv
```

#### Flask Port 5000
Flask by default uses port `5000` by default, so when running the `Docker` image
make sure to pass the port `5000` as seen above.

## Adapting
The following depicts some key things to consider when adapting (i.e. meaning to
use the existing repo without changing its fundamental structure) this
`repository` to your own project:
  + **1**: Using pre-existing repo structure

### Pre-Existing Repo Structure
The entire repository reflects the `structure` of the application and this can
be seen in a few specific directories/files:
  + **1**: The `server/media` directory
  + **2**: The `server/config` directory
  + **3**: The `server/templates` directory
  + **4**: The `server/static` directory
  + **5**: The `packages` directory
  + **5**: The `server/__init__.py` file

For actually `adapting` the repo for your own project you are going to only be
interested in the files found in these directories, but you **will not** be
changing the `name` or overall `structures` of these directories/files.

#### Media Directory
As the name implies this is where all your `digital content` (i.e. `files`) will
be stored. While you can rename this, or move this directory if you **truly**
want/need to, it is **highly** recommended for simplicity and ease of use to
not make any changes to the `name` or `location` of this directory.

In fact the only real change to this directory you need to consider is adding
the files you want to be served by the server (and possibly deleting the
`fictitious` music files used by the example).

For example maybe you have a file named `suze_blues.mp3` that you want to add
to your own `server/config/catalog.json` (see [next section](#config-directory))
then you would simply move this file to the `server/media` directory:
```
$ mv suze_blues.mp3 ~/project-msrv/server/media
```
In the [next section](#config-directory) we will discuss how to add the above
`file` as an `item` in your `digital catalog` (i.e. in the file
`server/config/catalog.json`)

#### Config Directory
The only real configuration that the `Flask` app takes is in the form of a
`Digital Catalog` file found at
[`server/config/catalog.json`](https://github.com/RagingTiger/project-msrv/blob/master/server/config/catalog.json).
If we take one of the example entries from this file and look at it we can see
what information is being stored for each `item`:
```
$ cat server/config/catalog.json
.
.
.
{
  "Kung FOO": {
    "fname": "kung_foo.mp3",
    "fdir": "media",
    "price": "1.99",
    "mime": "audio/mpeg",
    "upname": "kf.mp3"
  },
  .
  .
  .
}
```
In the above example `item` found inside the `catalog.json` file we see the
`item name` (e.g. `Kung FOO`) acts as the `key` and a dictionary of
`item attributes` acts as the `value` in the `catalog.json` file.

For adapting this `example` to your own project you need to copy this same
`item scheme` into your own `catalog.json` file. This scheme is as follows:
  + **Item Name**: Also the `key` to each entry in the `JSON` file
  (e.g. `Kung FOO`)
  + **fname**: The `file name` of the resource associated with the `item name`
  (e.g. `kung_foo.mp3`)
  + **fdir**: The `file directory` where resource `fname` is located
  (e.g. `media`)
  + **price**: The `price` of the `item` (e.g. `1.99`)
  + **mime**: The `mimetype` of the `item` (e.g. `audio/mpeg`)
  + **upname**: The `upload name` of the file sent when client downloads
  (e.g. `kf.mp3`)

**A few suggestions** .... basically **don't** change the `fdir` value from
`media` to some other directory. For example if you wanted to build some kind of
self-published music download site and you wanted to add your own entries, then
you might create an entry in your `catalog.json` similar to the one that
follows:
```
{
  "Suzy Sings the Blues": {
    "fname": "suze_blues.mp3",
    "fdir": "media",
    "price": "0.99",
    "mime": "audio/mpeg",
    "upname": "sstb.mp3"
  },
  .
  .
  .
}
```
Here we simply changed:
  + **Item Name**: changed to `Suzy Sings the Blues`
  + **fname**: changed to `suze_blues.mp3`
  + **price**: changed to `0.99`
  + **upname**: changed to `sstb.mp3`

If we changed the `fdir` value we would need to change the `repo structure`
which would mean we were no longer `adapting` the `repository` to our project
but instead `restructuring` the `repository` and that is beyond the scope of
this documentation.
