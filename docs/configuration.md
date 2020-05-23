# Configure Shuffle 
Documentation for configuring Shuffle. 

**PS: This is only for on-prem / open-source, not cloud**

# Table of contents
* [Introduction](#introduction)
* [Updating Shuffle](#updating_shuffle)
* [HTTPS](#https)

## Introduction
With Shuffle being Open Sourced, there is a need for a place to read about configuration. There are quite a few options, and this article aims to delve into those.

## Updating Shuffle
As long as you use Docker, updating Shuffle is pretty straight forward. To make sure you're as secure as possible, do this as much as you please.

While being in the main repository:
```
docker-compose down
git pull
docker-compose pull
docker-compose up
```

## HTTPS
HTTPS is enabled by default on port 3443 with a self-signed certificate for localhost. If you would like to change this, the only way (currently) is to add configure and rebuild the frontend. If you don't have HTTPS enabled, check [updating shuffle](#updating_shuffle) to get the latest configuration.

Necessary info:
* Certificates are located in ./frontend/certs. 
* ./frontend/README.md contains information on generating a self-signed cert 
* (default): Privatekey is named privkey.pem
* (default): Fullchain is named fullchain.pem

If you want to change this, edit ./frontend/Dockerfile and ./frontend/nginx.conf.

After changing certificates, you can rebuild the entire frontend by running (./frontend)
```
./run.sh
```
