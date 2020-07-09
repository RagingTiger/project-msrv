# Base Python image for building uWSGI
FROM python:3.8.2-slim-buster AS builder

# Install libs for compiling uwsgi
RUN apt-get update && apt-get -y install \
    build-essential && \
    pip install uwsgi

# Now beginning final production image
FROM python:3.8.2-slim-buster AS production

# set workdir
WORKDIR /project-msrv

# get uWSGI from builder image
ARG PYTHON_VERS=python3.8
ARG PYTHON_DIR=/usr/local/lib/${PYTHON_VERS}/site-packages/
COPY --from=builder ${PYTHON_DIR} ${PYTHON_DIR}
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# get src
COPY uwsgi.ini .
COPY requirements.txt .
COPY ./packages packages
COPY ./server server

# install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# set flask app
ENV FLASK_APP='server'

# set default nonce
ENV NONCE='All work and no play make jack a dull boy'

# setting default port
EXPOSE 5000

# set default command
CMD ["uwsgi", "uwsgi.ini"]
