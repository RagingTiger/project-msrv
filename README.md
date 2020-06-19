## tl;dr
Example of a `Digital Download` platform/business model using `Flask` in
`Python 3`, `Docker`, and plenty of `Cryptographic` goodness.

## Introduction
The repository depicts an example of how a `Digital Download` platform might be
constructed using `Flask`, `Python 3`, `Docker`, and `Cryptography`, with an
eye towards a `stateless` design. The example chosen for the website, is a
fictitious group of *recording artists* and *musicians* known as `Project MSRV`
(or simply `MSRV` as the fans call them.)

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
