# Configure Shuffle 
Documentation for configuring Shuffle. 

**PS: This is only for on-prem / open-source, not cloud**

# Table of contents
* [Introduction](#introduction)
* [Updating Shuffle](#updating_shuffle)
* [Proxy Configuration](#proxy_configuration)
* [HTTPS](#https)
* [Kubernetes](#kubernetes)
* [Database](#database)
* [Debugging](#debugging)
* [Execution Debugging](#execution_debugging)
* [App Debugging](#app_debugging)
* [OpenAPI Debugging](#openapi_debugging)

## Introduction
With Shuffle being Open Sourced, there is a need for a place to read about configuration. There are quite a few options, and this article aims to delve into those.

Shuffle is based on Docker and is started using docker-compose with configuration items in a .env file. .env has the configuration items to be used for default environment changes, database locations, port forwarding, github locations and more. 

## Installing Shuffle
Check out the [installation guide](https://github.com/frikky/shuffle/blob/master/install-guide.md), however if you're on linux:

```
git clone https://github.com/frikky/Shuffle
cd Shuffle
docker-compose up -d
```

## Updating Shuffle
As long as you use Docker, updating Shuffle is pretty straight forward. To make sure you're as secure and up to date as possible, do this as much as you please.

While being in the main repository:
```
docker-compose down
git pull
docker-compose pull
docker-compose up -d
docker pull frikky/shuffle:app_sdk
docker pull frikky/shuffle:worker
```

**PS: This will NOT update your apps, meaning they may be outdated. To update your apps, go to /apps and click both buttons in the top right corner (reload apps locally & Download from Github)**

## Proxy configuration
Proxies are another requirement to many enterprises, hence it's an important feature to support. There are two places where proxies can be implemented:
* Shuffle Backend: Connects to Github and Dockerhub.
* Shuffle Orborus: Connects to Dockerhub and Shuffle Backend.

**PS: Orborus settings are also set for the Worker**

To configure these, there are two options:
* Individual containers
* Globally for Docker

### Global Docker proxy configuration
Follow this guide from Docker: https://docs.docker.com/network/proxy/

### Individual container proxy
To set up proxies in individual containers, open docker-compose.yml and add the following lines with your proxy settings (http://my-proxy.com:8080 in my case).

**PS: Make sure to use uppercase letters, and not lowercase (HTTP_PROXY, NOT http_proxy)**

![Proxy containers](https://github.com/frikky/shuffle-docs/blob/master/assets/proxy-containers.png?raw=true)

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

## Kubernetes  
Shuffle use with Kubernetes is now possible due to help from our contributors. This has not extensively been tested, so please reach out to @frikkylikeme if you're having execution issues.

### Configuring Kubernetes:
To configure Kubernetes, you need to specify a single environment variable for Orborus: RUNNING_MODE. By setting the environment variable RUNNING_MODE=kubernetes, execution should work as expected!

## Database
The Shuffle database has a single configuration right now: it's location. The location was initially /etc/shuffle, but is now ./etc/shuffle to not have permission errors. To fix the issue, type ./shuffle-database

To modify the database location, change "DB_LOCATION" in .env (root dir) to your new location. 



## Debugging
As Shuffle has a lot of individual parts, debugging can be quite tricky. To get started, here's a list of the different parts, with the latter three being modular / location independant.

| Type     | Container name    | Technology       | Note |
| -------- | ----------------  | ---------------- | ---- |
| Frontend | shuffle-frontend  | ReactJS          | Cytoscape graphs & Material design |
| Backend  | shuffle-backend   | Golang           | Rest API that connects all the different parts |
| Database | shuffle-database  | Google Datastore | Has all non-volatile information. Will probably move to elastic or similar. |
| Orborus  | shuffle-orborus   |Golang 						| Runs workers in a specific environment to connect locations. Defaults to the environment "Shuffle" onprem. |
| Worker   | worker-id         | Golang 					| Deploys Apps to run Actions defined in a workflow |
| app sdk  | appname_appversion_id | Python           | Used by Apps to talk to the backend |
worker-8a666e4f-e544-440e-bf0f-4220e7cc9e25

### Execution debugging
Execution debugging might be the most notable issue you might explain. This is because there are a ton of reasons that it might crash. Before going into techniques to find what's going on, you'll need to understand what exactly happens when you click the big execution button.

**Frontend click -> Backend verifies and deploys executions -> (based on environments) orborus deploys a new worker -> worker finds actions to execute -> your app is executed.**

1. A workflow is executed
2. The backend verifies whether you can execute and deploys to environment
3. Orborus is listening to environment and deploys worker if it's the correct one
4. Worker deploys actions if they have the right environment 
5. App executes and returns data back to the execution

As previously stated, a lot can go wrong. Here's the most common issues:
* Networking (firewalls / proxies)
* Badly formed apps. 
* Bad environment

#### General debugging
This part is mean to describe how to go about finding the issue you're having with executions. In most cases, you should start from the top of the list previously described in the following way:


1. Find out what environment your action(s) are running under by clicking the App and seeing "Environment" dropdown. In this case (and default) is "Shuffle". Environments can be specified / changed under the path /admin
![Check execution 3](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_3.png?raw=true)

2. Check if the workflow executed at all by finding the execution line in the shuffle-backend container. Take note that it mentions environment "Shuffle", as found in the previous step.
```
docker logs -f shuffle-backend
```

![Check execution 1](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_1.png?raw=true)

3. If it executed, check whether Orborus is running, before checking it's logs for "Container \<container_id\> is created. The container_id is the worker it has deployed. Take not of the environment again at the end of the line. If you don't see this line, it's most likely because it's running in the wrong environment.

Check if shuffle-orborus is running
```
docker ps # Check if shuffle-orborus is running
```

Find whether it was deployed or not
```
docker logs -f shuffle-orborus  # Get logs from shuffle-orborus
```

![Check execution 2](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_2.png?raw=true)

Check environment of running shuffle-orborus container.
```
docker inspect shuffle-orborus | grep -i "ENV"
```

Expected env result where "Shuffle" corresponds to the environment
![Check execution 4](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_4.png?raw=true)

4. Check whether the worker executed your app. Remember that we found \<container_id\> previously by checking the logs of shuffle-orborus? Now we need that one. Workers are and will always be verbose, specifically for the reason of potential debugging.

Find logs from a docker container
```
docker logs -f CONTAINER_ID
```

![Check execution 5](https://github.com/frikky/shuffle-docs/blob/master/assets/check_execution_5.png?raw=true)

As can be seen in the image above, is shows the exact execution order it takes. It starts by finding the parents, before executing the child process after it's finished. Take note of the specific apps being executed as well. It says "Time to execute \<app_id\> with app \<app_name:app_version\>. This indicates the app THAT WILL be executed. The following lines saying "Container \<container_id\> is the container created with this app. 

5. App debugging in itself might be the trickiest. There are a lot of factors like branches, bad workflow building etc that might come into play. This builds on the same concept as the worker, where you pass the container ID it specified.

Get the app logs
```
docker logs -f CONTAINER_ID # The CONTAINER_ID found in the previous worker logs
```

As you will notice, app logs can be quite verbose (optional in a later build). In essence, if you see "RUNNING NORMAL EXECUTION" in the end, there's a 99.9% chance that it worked, otherwise some issue might have occurred. 

Please [notify me](https://twitter.com/frikkylikeme) if you need help debugging app executions ASAP, as I've done a lot of it, but it's more tricky than the other steps.

TBD: Finish app debugging properly

### App debugging
TBD - this is the process of checking MANUAL [app creation](/docs/apps#create_custom_app)

### OpenAPI debugging
TBD - this is the process of checking potential [OpenAPI app bugs](/docs/apps#create_openapi_app)
