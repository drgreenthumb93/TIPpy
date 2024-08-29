# use python runtime
FROM python:3.9-slim

# install TOR
RUN apt-get update && apt-get install -y tor && rm -rf /var/lib/apt/lists/*

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# expose ports for TOR
EXPOSE 9050 9051

# start TOR and the script
CMD tor & python ./TIPpy_docker.py
