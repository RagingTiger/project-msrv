# using slim pythin 3.8.2 base image
FROM python:3.8.2-alpine3.10

# set workdir
WORKDIR /usr/src/project-msrv

# get src
COPY requirements.txt .
COPY ./packages packages
COPY ./server server

# install requirements
RUN pip3 install -r requirements.txt

# set flask app
ENV FLASK_APP='server'

# set default nonce
ENV NONCE='All work and no play make jack a dull boy'

# setting default port
EXPOSE 5000

# set default command
CMD ["flask", "run", "--host=0.0.0.0"]
