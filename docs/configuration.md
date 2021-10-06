# Configure Shuffle 
Documentation for configuring Shuffle. 

**PS: This is only for on-prem / open-source, not cloud**

## Table of contents
* [Introduction](#introduction)
* [Updating Shuffle](#updating_shuffle)
* [Production readiness](#production_readiness)
* [Proxy Configuration](#proxy_configuration)
* [HTTPS](#https)
* [Kubernetes](#kubernetes)
* [Database](#database)
* [Network Configuration](#network_configuration)
* [Docker Version error](#docker_version_error)
* [Database migration](#database_migration)
* [Debugging](#debugging)
* [Execution Debugging](#execution_debugging)
* [Known Bugs](#known_bugs)

## Introduction
With Shuffle being Open Sourced, there is a need for a place to read about configuration. There are quite a few options, and this article aims to delve into those.

Shuffle is based on Docker and is started using docker-compose with configuration items in a .env file. .env has the configuration items to be used for default environment changes, database locations, port forwarding, github locations and more. 

## Installing Shuffle
Check out the [installation guide](https://github.com/frikky/shuffle/blob/master/.github/install-guide.md), however if you're on linux:

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
```

**PS: This will NOT update your apps, meaning they may be outdated. To update your apps, go to /apps and click both buttons in the top right corner (reload apps locally & Download from Github)**

## Production readiness
Shuffle is by default configured to be easy to start using. This means we've had to make some tradeoffs which can be enabled/disabled to make it easier to use the first time. This part outlines a lot of what's necessary to make Shuffle security, availability and scalability better.

**Here are the things we'll dive into**
- [Servers](#servers)
- [Hybrid access](#hybrid_configuration)
- [Environment Variables](#environment_variables)
- [Redundancy](#redundancy)
- [Proxies](#proxy_configuration)

### Servers 
When setting up Shuffle for production, we always recommend using a minimum of two servers (VMs). This is because you don't want your executions to clog the webserver, which again clogs the executions (orborus). You can put Orborus on multiple servers with different environments to ensure better availability, or [talk to us about Kubernetes/Swarm](https://shuffler.io/contact)

**Orborus**
Runs all workflows - CPU heavy. If you do a lot of file transfers or memory analysis, make sure to add RAM accordingly.
- Services: Orborus, Worker, Apps
- CPU: 4vCPU
- RAM: 4Gb
- Disk: 10Gb (SSD)

**Webserver**
The webserver is where your users and our API is. It is RAM heavy as we're doing A LOT of caching to ensure scalability.
- Services: Frontend, Backend, Database
- CPU: 2vCPU 
- RAM: 8Gb
- Disk: 100Gb (SSD)

#### Docker configuration 
These are the Docker configurations for the different servers. To use them, put the files in files called docker-compose.yml, and run 
```
docker-compose up -d
``` 

to start the containers.

PS: The data below is based on [this docker-compose file](https://github.com/frikky/Shuffle/blob/master/docker-compose.yml)

**Orborus**
Below is the Orborus configuration. make sure to change "BASE_URL" in the environment to match the Shuffle backend location. It can be modified to reduce or increase load, to add proxies, change backend environment to execute and much more. See [environment variables](#environment_variables) for all options.

**PS**: By default, the environments (executions) are NOT authenticated.

```
version: '3'
services:
  orborus:
    #build: ./functions/onprem/orborus
    image: ghcr.io/frikky/shuffle-orborus:latest
    container_name: shuffle-orborus
    hostname: shuffle-orborus
    networks:
      - shuffle
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - BASE_URL=http://SHUFFLE-BACKEND:BACKEND-PORT
      - SHUFFLE_APP_SDK_VERSION=0.8.90
      - SHUFFLE_WORKER_VERSION=latest
      - ORG_ID=Shuffle
      - ENVIRONMENT_NAME=Shuffle
      - DOCKER_API_VERSION=1.40
      - SHUFFLE_ORBORUS_EXECUTION_TIMEOUT=600
      - SHUFFLE_BASE_IMAGE_NAME=frikky
      - SHUFFLE_BASE_IMAGE_REGISTRY=ghcr.io
      - SHUFFLE_BASE_IMAGE_TAG_SUFFIX="-0.8.60"
      - CLEANUP=true
    restart: unless-stopped
networks:
  shuffle:
    driver: bridge
```

**Webserver**
The webserver should run the Frontend, Backend and Database. Make sure [THIS .env file](https://github.com/frikky/Shuffle/blob/master/.env) exists in the same folder. Further, make sure that Opensearch the right access:
```
sudo sysctl -w vm.max_map_count=262144 			# https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html
sudo chown 1000:1000 -R shuffle-database 		# Requires for Opensearch 
```

docker-compose.yml:
```
version: '3'
services:
  frontend:
    image: ghcr.io/frikky/shuffle-frontend:latest
    container_name: shuffle-frontend
    hostname: shuffle-frontend
    ports:
      - "${FRONTEND_PORT}:80"
      - "${FRONTEND_PORT_HTTPS}:443"
    networks:
      - shuffle
    environment:
      - BACKEND_HOSTNAME=${BACKEND_HOSTNAME}
    restart: unless-stopped
    depends_on:
      - backend
  backend:
    image: ghcr.io/frikky/shuffle-backend:latest
    container_name: shuffle-backend
    hostname: ${BACKEND_HOSTNAME}
    # Here for debugging:
    ports:
      - "${BACKEND_PORT}:5001"
    networks:
      - shuffle
    volumes: 
      - /var/run/docker.sock:/var/run/docker.sock 
      - ${SHUFFLE_APP_HOTLOAD_LOCATION}:/shuffle-apps     
      - ${SHUFFLE_FILE_LOCATION}:/shuffle-files
      #- ${SHUFFLE_OPENSEARCH_CERTIFICATE_FILE}:/shuffle-files/es_certificate
    env_file: .env 
    environment:
      - SHUFFLE_APP_HOTLOAD_FOLDER=/shuffle-apps
      - SHUFFLE_FILE_LOCATION=/shuffle-files
    restart: unless-stopped
    depends_on:
      - opensearch 
  opensearch:
    image: opensearchproject/opensearch:1.0.0
    hostname: shuffle-opensearch
    container_name: shuffle-opensearch
    environment:
      - bootstrap.memory_lock=true 
      - "OPENSEARCH_JAVA_OPTS=-Xms1024m -Xmx1024m" # minimum and maximum Java heap size, recommend setting both to 50% of system RAM
			- plugins.security.disabled=true
      - cluster.routing.allocation.disk.threshold_enabled=false
      - cluster.name=shuffle-cluster
      - node.name=shuffle-opensearch
      - discovery.seed_hosts=shuffle-opensearch
      - cluster.initial_master_nodes=shuffle-opensearch
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536 # maximum number of open files for the OpenSearch user, set to at least 65536 on modern systems
        hard: 65536
    volumes:
      - ${DB_LOCATION}:/usr/share/opensearch/data:rw
    networks:
      - shuffle
    restart: unless-stopped
networks:
  shuffle:
    driver: bridge
```

### Hybrid Configuration
If you want to try using Hybrid Shuffle, giving you access to cloud executions, failovers and backups - [Email us](mailto:frikky@shuffler.io)

### Environment Variables
Shuffle has a few toggles that makes it straight up faster, but which removes a lot of the checks that are being done during your first tries of Shuffle.

Backend:
```
# Set the encryption key to ensure all app authentication is being encrypted. If this is NOT defined, we do not encrypt your apps. If this is defined, all authentications - both old and new will start using this key.
# Do NOT lose this key if specified, as that means you will need to reset all keys.

SHUFFLE_ENCRYPTION_MODIFIER=YOUR KEY HERE

# PS: Encryption is available from Shuffle backend version >=0.9.17
```

Orborus:
```
# Cleans up all containers after they're done. Necessary to help Docker scale. Default=false
CLEANUP=true 	

# Cleans up any containers related to Shuffle that have been up for more than 600 seconds. 
SHUFFLE_ORBORUS_EXECUTION_TIMEOUT=600 

# Decides the max amount of workflows to concurrenly run. Defaults to 10. 
# Example math: 10 workflows * WITH 10 apps / second = 110 containers per second. 
# We recommend starting with 10 and going higher as need be.
SHUFFLE_ORBORUS_EXECUTION_CONCURRENCY=10 

# Configures a HTTP proxy to use when talking to the Shuffle Backend
HTTP_PROXY= 	
# Configures a HTTPS proxy when speaking to the Shuffle Backend
HTTPs_PROXY= 	

# Decides if the Worker should use the same proxy as Orborus (HTTP_PROXY). Default=true
SHUFFLE_PASS_WORKER_PROXY=true

# Decides if the Apps should use the same proxy as Orborus (HTTP_PROXY). Default=false
SHUFFLE_PASS_WORKER_PROXY=true
```

### Redundancy
TBD: We have yet to decide how this should be implemented for Shuffle. Per now, you may configure multiple instances with a load balancer, but there's no easy way to syncronize data between them to ensure they're in the same place.

A good place to start is this blogpost by one of our contributors: https://azgaviperr.github.io/3-nodes-swarm/DockerSwarm/Stacks/Shuffler/

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

### Configuring Kubernetes
To configure Kubernetes, you need to specify a single environment variable for Orborus: RUNNING_MODE. By setting the environment variable RUNNING_MODE=kubernetes, execution should work as expected!

## Network configuration 
In most enterprise environments, Shuffle will be behind multiple firewalls, proxies and other networking equipment. If this is the case, below are the requirements to make Shuffle work anywhere. The most common issue has to do with downloads from Alpine linux during runtime.

**PS:** If external connections are blocked, you may further have issues running Apps. Read more about [manual image transfers here](#manual_docker_image_transfers).

### Domain Whitelisting
These URL's are used to get Shuffle up and running. Whitelisting them for the Shuffle services should make all processes work seemlessly.  

PS: We do intend to make this JUST https://shuffler.io in the future.

```
# Can be closed after install with working Workflows
shuffler.io  													# Initial setup & future app/workflow sync 
github.com														# Downloading apps, workflows and documentation
pkg-containers.githubusercontent.com 	# Downloads from Github Container registry (ghcr.io)
raw.githubusercontent.com 						# Downloads our Documentation raw from github (https://github.com/shuffle/shuffle-docs) 

# Should stay open
dl-cdn.alpinelinux.org						# Used for building apps in realtime
registry.hub.docker.com 					# Downloads apps if they don't exist locally
ghcr.io														# Github Docker registry
auth.docker.io										# Dockerhub authentication
registry-1.docker.io							# Dockerhub registry (for apps)
production.cloudflare.docker.com 	# Protects of DockerHub
```

### Proxy settings
The main proxy issues may arise with the "Backend", along with 3the "Orborus" container, which runs workflows. This has to do with how this server can contact the backend (Orborus), along with how apps can be downloaded (Worker), down to how apps engage with external systems (Apps). 

Environment variables to be sent to the Orborus container:
```
# Configures a HTTP proxy to use when talking to the Shuffle Backend
HTTP_PROXY= 	
# Configures a HTTPS proxy when speaking to the Shuffle Backend
HTTPs_PROXY= 	

# Decides if the Worker should use the same proxy as Orborus (HTTP_PROXY). Default=true
SHUFFLE_PASS_WORKER_PROXY=true

# Decides if the Apps should use the same proxy as Orborus (HTTP_PROXY). Default=false
SHUFFLE_PASS_WORKER_PROXY=true
```

Environment variables for the Backend container:
```
# A proxy to be used if Opensearch / Elasticsearch (database) is behind a proxy. 
SHUFFLE_OPENSEARCH_PROXY

# Configures a HTTP proxy for external downloads
HTTP_PROXY= 	
# Configures a HTTPS proxy for external downloads
HTTPs_PROXY= 	
```

### Manual Docker image transfers
In certain cases you may not have access to download or build images at all. If that's the case, you'll need to manually transfer them to the appropriate server. If the image to transfer is an app, it should be moved to the "Orborus" server. Otherwise; backend server. 

```
# 1. Download the image you want. Go to [hub.docker.com](https://hub.docker.com/r/frikky/shuffle/tags?page=1&ordering=last_updated) and find the image. Download with docker pull. E.g. for Shuffle-tools:
docker pull frikky/shuffle:shuffle-tools_1.1.0

# 2. Save the image to a file to be transferred. 
docker save frikky/shuffle:shuffle-tools_1.1.0 > shuffle_tools.tar

# 3. Transfer the file to a remote server
scp shuffle_tools.tar username@<server>:/path/to/destination/shuffle_tools.tar

# 4. Log into the remote server and find the repository
ssh username@<server>
cd /path/to/destination #same path as above

# 5. Load the file!
docker load shuffle_tools.tar

## All done!

# Transfer between 2 remote hosts:
#scp -3 centos@10.0.0.1:/home/user/wazuh.tar centos@10.0.0.2:/home/user/wazuh.tar
```

## Database
To modify the database location, change "DB_LOCATION" in .env (root dir) to your new location. 

### Database indexes (opensearch)
- workflowapp
- workflowexecution
- workflowapp
- workflow
- apikey
- app_execution_values
- environments
- files
- hooks
- openapi3
- organizations
- schedules
- sessions
- syncjobs
- trigger_auth
- workflowappauth
- users
- workflowqueue-* 

PS: workflowqueue-* is based on the environment used for execution.

## Database migration
With the change from 0.8 to 0.9 we're changing databases from Google's Datastore to Opensearch. This has to be done due to unforeseen errors with Datastore, including issues with scale, search and debugging. The next section will detail how you can go about migrating from 0.8.X to 0.9.0 without losing access to your workflows, apps, organizations, triggers, users etc. 

**Indexes not being migrated**:
- workflowexecutions
- app_execution_values
- files
- sessions
- syncjobs
- trigger_auth
- workflowqueue

```
Before you start:
If you have data of the same kind in the same index within Opensearch, these will be overwritten. 
Example: you have the user "admin" in the index "users" within Opensearch and Datastore; this will be overwritten with the version that's in Datastore.
```

**Requirements**:
- Admin user in Shuffle using Datastore 
- An available Elasticsearch / Opensearch database.

### 1. Set main database to be Datastore
```
- 1. Open .env 
- 2. Scroll down and look for "SHUFFLE_ELASTIC"
- 3. Set it to false; SHUFFLE_ELASTIC=false
```

### 2. Set up Datastore and Opensearch 
In order to run the migration, we have to run both databases at once, connected to Shuffle. This means to run both containers at the same time in the Docker-compose file like the image below, before restarting.

```
docker-compose down
## EDIT FILE
docker-compose pull 
docker-compose up 		# PS: Notice that we don't add -d here. This to make it easier to follow the logs. It's ok as we'll stop the instance later.
```

![Migration-1](https://github.com/frikky/shuffle-docs/blob/master/assets/migration-1.png?raw=true)

### 3. Find your API-key!
Now that you have both databases set up, we need to find the API-key. 
```
1. http://localhost:3000/settings 	# You may need to log in 
2. Copy the API-key
3. Go to next step
```

### 4. Run the migration!
We'll now run a curl command that starts the migration. It shouldn't take more than a few seconds, max a few minutes at scale.

PS: This is NOT a destructive action. It just reads data from one place and moves it to the other. The server will restart after it has finished.

Change the part that says "APIKEY" to your actual API key from the previous step.
```
curl -XPOST -v localhost:5001/api/v1/migrate_database -H 'Authorization: Bearer APIKEY'
```

![Migration-2](https://github.com/frikky/shuffle-docs/blob/master/assets/migration-2.png?raw=true)

### 5. Change database back to Opensearch 
Let's reverse step 1 by choosing elastic as main database
```
- 1. Open .env 
- 2. Scroll down and look for "SHUFFLE_ELASTIC"
- 3. Set it to false; SHUFFLE_ELASTIC=true
```

Got any issue? Ask on [discord](https://discord.gg/B2CBzUm) or [Contact us](/contact). 

## Docker Version error
Shuffle runs using Docker in every step, from the frontend to the workers and apps. For certain systems however, it requires manual configuration of the version of Docker you're running. This has a self-correcting feature to it within Orborus > v0.8.98, but before then you'll have to manually correct for it.

```
Error getting containers: Error response from daemon: client version 1.40 is too new. Maximum supported API version is 1.35
```

To fix this issue, we need to set the version from 1.40 down to 1.35 in the Shuffle enviornment. This can be done by opening the docker-compose.yml file, then changing environment variable "DOCKER_API_VERSION" from 1.40 to 1.35 for the "orborus" service as seen below, then restarting Shuffle.

![Error with Docker version](https://github.com/frikky/shuffle-docs/blob/master/assets/configuration-error-1.png?raw=true)


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

## Hybrid docker image handling 
We currently don't have a Docker Registry for Shuffle, meaning you need some minor configuration to get Orborus running remotely with the right containers. This only applies to containers not on dockerhub, as we automatically push PYTHON containers there when updated (not OpenAPI)

Here's an example of how to handle this with two different servers and Docker
```
ssh user@10.0.0.1
docker save frikky/shuffle:wazuh_api_rest_1.0.0 > wazuh.tar
exit
scp -3 centos@10.0.0.1:/home/user/wazuh.tar centos@10.0.0.2:/home/user/wazuh.tar
ssh user@10.0.0.2
docker load wazuh.tar
```

TBD: We'll make this an API-call for ContainerD later.

## Known Bugs
