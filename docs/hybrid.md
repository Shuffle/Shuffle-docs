# Hybrid
Documentation for how to get integrate onpremise and cloud 

# Table of contents
* [Introduction](#introduction)
* [About](#about)
* [Setup](#setup)
* [Troubleshooting](#troubleshooting)

## Introduction
A hybrid solution in Shuffle terms means that you will have access to run all workflows on in your own environment. Our integration is easy to set up, and gives access for your cloud solutions to talk to your on-premise solutions in near realtime. As described in [workflows](/docs/workflows) and [apps](/docs/apps), all actions can be set to run in the environment of your choice. The environments are defined by you (except cloud), and can be in multiple locations. 

## About
The hybrid solution, Orborus, is a docker container that runs batch jobs for your company, looking for jobs assigned to the execution environment you have assigned to it. It polls for new executions on a regular basis, and creates a worker for each workflow execution. It works together with a cloud worker to finish every workflow in a timely manner, and if it doesn't tries to give a reason as to why.

## Setup 
We use [Docker](https://www.docker.com/) and [Google cloud functions](https://cloud.google.com/functions/) extensively, and this is no different. 

1. Go to your server, and make sure you [have docker installed and started](https://docs.docker.com/install/), before moving on.
2. While logged in, go to [settings](https://shuffler.io/settings) and copy the field "ORG_ID"
3. COPY, then EDIT (after =) in the ORG_ID= below, before running the command on your server
```bash
docker stop orborus && docker rm orborus && docker run \
	--env "ORG_ID=" \
	--env "DOCKER_API_VERSION=1.37" \
	-v /var/run/docker.sock:/var/run/docker.sock \
	--name orborus \
	-d frikky/shuffle:orborus
```

### Troubleshooting / known issues
* Does your server have access to https://shuffler.io and https://hub.docker.com/? 
```
curl https://shuffler.io
curl https://hub.docker.com
```
* Does it say "client version too new" when you run the following command?
```
docker logs orborus | head
```

Please contact us if you have an issue with any of the above.
