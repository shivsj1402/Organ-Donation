FROM python:3.6-alpine

# Update
RUN apk update

# Prepare the basic tools
RUN apk update && apk add nano postgresql postgresql-client postgresql-dev postgresql-contrib gcc musl-dev

# Get latest pip
RUN pip install --upgrade pip

COPY ./requirements.txt /home/organdonation/

# Install requirements from the file, its dependencies
# and remove unnecessary libs and cached files
RUN apk add --update build-base gcc python-dev \
&& pip install --upgrade virtualenv \
&& pip install --upgrade -r /home/organdonation/requirements.txt \
&& rm -rf /var/cache/apk/* \
&& rm -rf /root/.cache/pip

# Copying required files
COPY ./setup.py /home/organdonation/
COPY ./app.py /home/organdonation/
COPY ./organdonationwebapp /home/organdonation/organdonationwebapp

# Running initial setup
WORKDIR /home/organdonation