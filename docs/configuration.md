# Configure Shuffle

Documentation for configuring Shuffle.

**PS: This is only for on-prem / open-source, not cloud**

## Table of contents

* [Introduction](#introduction)
* [Updating Shuffle](#updating_shuffle)
* [Production readiness](#production_readiness)
* [Shuffle Scaling](#scaling_shuffle_with_swarm)
* [Distributed Caching](#distributed_caching)
* [No Internet Install](#no_internet_install)
* [Proxy Configuration](#proxy_configuration)
* [HTTPS](#https)
* [IPv6](#ipv6)
* [Kubernetes](#kubernetes)
* [Database](#database)
* [Network Configuration](#network_configuration)
* [Docker Version error](#docker_version_error)
* [Database indexes](#database_indexes)
* [Uptime monitoring](#uptime_monitoring)
* [Debugging](#debugging)
* [Execution Debugging](#execution_debugging)
* [Known Bugs](#known_bugs)
* [Shuffle Server Healthcheck](#shuffle-server-healthcheck)

## Introduction

With Shuffle being Open Sourced, there is a need for a place to read about configuration. There are quite a few options, and this article aims to delve into those.

Shuffle is based on Docker and is started using docker-compose with configuration items in a .env file. .env has the configuration items to be used for default environment changes, database locations, port forwarding, github locations and more.

## Installing Shuffle

Check out the [installation guide](https://github.com/frikky/shuffle/blob/master/.github/install-guide.md), however if you're on linux:

System requirements may be found further down in the [Servers](#servers) section.

```
git clone https://github.com/frikky/Shuffle
cd Shuffle
docker-compose up -d
```

## Updating Shuffle

`From version v1.1 onwards, we will use ghcr.io/shuffle/* registry instead of ghcr.io/frikky/*`

As long as you use Docker, updating Shuffle is pretty straight forward. To make sure you're as secure and up to date as possible, do this as much as you please. To use a specific version of Shuffle, check out [specific version](/docs/configuration#specific_versioning). We recommend always sticking to the "latest" tag, and if you want experimental changes, use the "nightly" tag.

While being in the main repository, here is how to update Shuffle:

```
docker-compose down
git pull
docker pull frikky/shuffle:app_sdk    # Force update the App SDK
docker-compose pull
docker-compose up -d
```

**PS: This will NOT update your apps, meaning they may be outdated. To update your apps, go to /apps and click both buttons in the top right corner (reload apps locally & Download from Github)**

## Specific Versioning

To use a specific version of Shuffle, you'll need to manually edit the Docker-Compose.yml file to reflect the version - usually for the frontend and backend, but sometimes also the other containers. You can [see all our released versions here](https://github.com/orgs/Shuffle/packages). We recommend keeping the same version for the frontend and backend, and **not** to keep them separate, as seen in the image below.

![image](https://user-images.githubusercontent.com/5719530/169809608-325b5e9f-af44-45ab-83e1-c2acbcaf206a.png)

## Production readiness

Shuffle is by default configured to be easy to start using. This means we've had to make some tradeoffs which can be enabled/disabled to make it easier to use the first time. This part outlines a lot of what's necessary to make Shuffle's security, availability and scalability better.

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

These are the Docker configurations for the two different servers described above. To use them, put the information in files called docker-compose.yml on each respective server, to start the containers.

PS: The data below is based on [this docker-compose file](https://github.com/frikky/Shuffle/blob/master/docker-compose.yml)

**Orborus**
Below is the Orborus configuration. make sure to change "BASE_URL" in the environment to match the external Shuffle backend URL. It can be modified to reduce or increase load, to add proxies, and much more. See [environment variables](#environment_variables) for all options.

**PS**: Replace SHUFFLE-BACKEND with the IP of Shuffle backend in the specification below. Using Hostname MAY [cause issues](https://github.com/frikky/Shuffle/issues/537) in certain environments.
**PPS**: By default, the environments (executions) are NOT authenticated.

```
version: '3'
services:
  orborus:
    #build: ./functions/onprem/orborus
    image: ghcr.io/shuffle/shuffle-orborus:latest
    container_name: shuffle-orborus
    hostname: shuffle-orborus
    networks:
      - shuffle
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - BASE_URL=http://SHUFFLE-BACKEND:5001
      - SHUFFLE_APP_SDK_VERSION=1.1.0
      - SHUFFLE_WORKER_VERSION=latest
      - ORG_ID=Shuffle
      - ENVIRONMENT_NAME=Shuffle
      - DOCKER_API_VERSION=1.40
      - SHUFFLE_BASE_IMAGE_NAME=frikky
      - SHUFFLE_BASE_IMAGE_REGISTRY=ghcr.io
      - SHUFFLE_BASE_IMAGE_TAG_SUFFIX="-1.0.0"
      - CLEANUP=true
      - SHUFFLE_ORBORUS_EXECUTION_TIMEOUT=600
    restart: unless-stopped
networks:
  shuffle:
    driver: bridge
```

**Webserver**
The webserver should run the Frontend, Backend and Database. Make sure [THIS .env file](https://github.com/frikky/Shuffle/blob/master/.env) exists in the same folder. Further, make sure that Opensearch the right access:

```
sudo sysctl -w vm.max_map_count=262144             # https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html
sudo chown 1000:1000 -R shuffle-database         # Requires for Opensearch
```

docker-compose.yml:

```
version: '3'
services:
  frontend:
    image: ghcr.io/shuffle/shuffle-frontend:latest
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
    image: ghcr.io/shuffle/shuffle-backend:latest
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
    image: opensearchproject/opensearch:2.3.0
    hostname: shuffle-opensearch
    container_name: shuffle-opensearch
    environment:
      - bootstrap.memory_lock=true
      - "OPENSEARCH_JAVA_OPTS=-Xms4096m -Xmx4096m" # minimum and maximum Java heap size, recommend setting both to 50% of system RAM
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

### Hybrid Cloud Configuration

* Onprem: If you want to try using Hybrid Shuffle, see [Cloud sync documentation](/docs/organizations#cloud_synchronization)
* Cloud: If you want access to on-premises resources and API's, [set up extra Environments](/docs/organizations#environments)

## Scaling Shuffle with Swarm
Orborus can run in Docker-swarm mode, and in early 2023, with Kubernetes. This makes the workflow executions A LOT faster, use less resources, and makes it more scalable across multiple servers. This [is a paid service](https://shuffler.io/pricing2), and requires the [Enterprise / Scale license](https://shuffler.io/pricing2). There are ways to achieve the same by [using multiple environments without swarm](/docs/organizations#environments).

You will be provided with a url to download the Worker image from Shuffle. Orborus does not need changing.

1. Download the new worker you were provided:
```
    wget URL # URL is the url provided by Shuffle
    docker load -i shuffle-worker.zip
    rm shuffle-worker.zip
```

2. Set Orborus to latest in your docker-compose.yml file
```
    image: ghcr.io/shuffle/shuffle-orborus:latest
```

3. Add and change environment variables for Orborus in the docker-compose.yml file. BASE_URL is the external URL of the server you're running Shuffle on (the one you visit Shuffle with in your browser):
```
    SHUFFLE_LOGS_DISABLED=true
    SHUFFLE_WORKER_IMAGE=ghcr.io/shuffle/shuffle-worker-scale:latest
    SHUFFLE_SWARM_NETWORK_NAME=shuffle_swarm_executions
    SHUFFLE_SCALE_REPLICAS=1
    SHUFFLE_SWARM_CONFIG=run
    BASE_URL=http://SERVER-URL:3443
```

4. When all is done, take down the stack and pull it back up AFTER initializing swarm:
```
docker swarm init
docker-compose down
docker-compose up -d
```

PS: In certain scenarios you may need extra configurations, e.g. for network MTU's, docker download locations, proxies etc. See more in the [production readiness](/docs/configuration#production_readiness) section.

### Verify swarm

Run the following command to get logs from Orborus:

```
docker logs -f shuffle-orborus
```

And to check if services have started:

```
docker service ls
```

If the list is empty, or you see any of the "replicas" have 0/1, then something is wrong. In case of any swarm issues, contact us at (support@shuffler.io](mailto:support@shuffler.io) or contact your account representative.

![](Aspose.Words.81096d25-bbff-47b2-a5ee-1ac38ad8ca4e.001.jpeg)

### Environment Variables

Shuffle has a few toggles that makes it straight up faster, but which removes a lot of the checks that are being done during your first tries of Shuffle.

Backend:

```
# Set the encryption key to ensure all app authentication is being encrypted. If this is NOT defined, we do not encrypt your apps. If this is defined, all authentications - both old and new will start using this key. 
# Do NOT lose this key if specified, as that means you will need to reset all keys.

SHUFFLE_ENCRYPTION_MODIFIER=YOUR KEY HERE

# PS: Encryption is available from Shuffle backend version >=0.9.17.
## PPS: There's a [known bug](https://github.com/frikky/Shuffle/issues/528) with Proxies and git

# Set up distributed memcaching. See "Distributed Caching" for more.
SHUFFLE_MEMCACHED=<IP>:PORT

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


### PAID: The environment variables below only work when you've acquired a paid license of Shuffle (not required, but VERY useful when scaling Shuffle):
SHUFFLE_WORKER_IMAGE=ghcr.io/shuffle/shuffle-worker-scale:latest
SHUFFLE_SWARM_NETWORK_NAME=shuffle_swarm_executions
SHUFFLE_SCALE_REPLICAS=1
SHUFFLE_SWARM_CONFIG=run

# Set up distributed caching for Orborus & Worker(s). See "Distributed Caching" for more.
SHUFFLE_MEMCACHED=<IP>:PORT
```

### Distributed Caching
Once you have a Scalable version of Shuffle, using Docker swarm, it becomes important for data to flow correctly throughout the platform. In version 1.1 of Shuffle, we introduce distributed caching [in the form of Memcached](https://hub.docker.com/_/memcached). Memcached helps reduce the load on the database, as well as to ensure all executions are handled adequately. These services are supported:

- Backend
- Orborus
- Worker

To make use of Memcached, you have to start a memcached service locally on a host Shuffle can access, before configuring each service to use it with a single environment variable. The default port is 11211. Here is a quickstart that reserves 1024 Mb of memory:
```
docker run --name shuffle-cache -p 11211:11211 -d memcached -m 1024
```

**PS: This requires swap limit capabilities on the Docker host. [More about running it in Docker here](https://hub.docker.com/_/memcached)**

Once this is up, it will be listening on port 11211. From here, you may set up the `SHUFFLE_MEMCACHED` environment variable on the previously mentioned services. We recommend starting with the backend. Here's an example that fits into your docker-compose file:
```
services:
  image: ghcr.io/shuffle/shuffle-backend:latest
  environment:
    - SHUFFLE_MEMCACHED=10.0.0.1:11211
    ...
  ...
  
```

If you need help with this, [please contact us](mailto:support@shuffler.io).

### Redundancy
You may configure multiple instances with a load balancer and docker-swarm/kubernetes. An official guide for high availability is still in the making. Please [contact us](https://shuffler.io/contact) if this is a need.

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

### Orborus running on a different network

All you'll need to do is allow orborus to have access to the backend port and your setup will work fine.


## HTTPS

HTTPS is enabled by default on port 3443 with a self-signed certificate for localhost. If you would like to change this, the only way (currently) is to add configure and rebuild the frontend. If you don't have HTTPS enabled, check [updating shuffle](#updating_shuffle) to get the latest configuration.

**PS: Another workaround is to set up an [Nginx reverse proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) you can control yourself. See further down for more details**

Necessary info for the truststore to create TLS/SSL certificates:

* Certificates are located in ./frontend/certs.
* ./frontend/README.md contains information on generating a self-signed cert
* (default): Privatekey is named privkey.pem
* (default): Fullchain is named fullchain.pem

If you want to change this, edit ./frontend/Dockerfile and ./frontend/nginx.conf.

After changing certificates, you can rebuild the entire frontend by running (./frontend)

```
./run.sh
```

### Using the Nginx Reverse Proxy for TLS/SSL
If you intend to use Nginx as a Reverse Proxy, the main steps are below. [Here is the basic network architecture for it](https://jamboard.google.com/d/1zJU8yMzbsu-XWeZnch_5MoDwmMNkkN8ZmoGNLCaHPlU/edit?usp=sharing).
1. [Install Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04) on your server (find the correct distro)
2. Make sure you have a VALID certificate that matches your domain/hostname and [add this to your Nginx server](https://phoenixnap.com/kb/install-ssl-certificate-nginx)
3. In the nginx.conf file, under "server", add the following. Make sure to change the "proxy_pass" part
```
		location /api/v1 {
			proxy_pass SHUFFLE FRONTENDIP;
			proxy_buffering off;
			proxy_http_version 1.1;

			proxy_connect_timeout 900;
			proxy_send_timeout 900;
			proxy_read_timeout 900;
			send_timeout 900;
      proxy_ssl_verify off;
    }
```
4. Restart Nginx! `systemctl restart nginx`

## IPv6

Shuffle supports IPv6 in Docker by default, but your docker engine may not. IPv6 can be enabled in Docker by adding it to the /etc/docker/daemon.json file on the host as per this article by Docker:

[https://docs.docker.com/config/daemon/ipv6/](https://docs.docker.com/config/daemon/ipv6/)

## Kubernetes

Shuffle use with Kubernetes is now possible due to help from our contributors. This has not extensively been tested, so please reach out to @frikkylikeme if you're having execution issues.

### Configuring Kubernetes

To configure Kubernetes, you need to specify a single environment variable for Orborus: RUNNING_MODE. By setting the environment variable RUNNING_MODE=kubernetes, execution should work as expected!

## Network configuration

In most enterprise environments, Shuffle will be behind multiple firewalls, proxies and other networking equipment. If this is the case, below are the requirements to make Shuffle work anywhere. The most common issue has to do with downloads from Alpine linux during runtime.

**PS:** If external connections are blocked, you may further have issues running Apps. Read more about [manual image transfers here](#manual_docker_image_transfers).

### Domain Whitelisting

These URL's are used to get Shuffle up and running. Whitelisting them for the Shuffle services should make all processes work seamlessly.  

PS: We do intend to make this JUST https://shuffler.io in the future.

```
# Can be closed after install with working Workflows
shuffler.io                                                      # Initial setup & future app/workflow sync
github.com                                                        # Downloading apps, workflows and documentation
pkg-containers.githubusercontent.com     # Downloads from Github Container registry (ghcr.io)
raw.githubusercontent.com                         # Downloads our Documentation raw from github (https://github.com/shuffle/shuffle-docs)

# Should stay open
dl-cdn.alpinelinux.org                        # Used for building apps in realtime
registry.hub.docker.com                     # Downloads apps if they don't exist locally
ghcr.io                                                        # Github Docker registry
auth.docker.io                                        # Dockerhub authentication
registry-1.docker.io                            # Dockerhub registry (for apps)
production.cloudflare.docker.com     # Protects of DockerHub
```

### Incoming Domain Whitelisting

When using Shuffle in the cloud, the incoming IP by defaut will be be from our cloud functions. The range is not static, and may wary wildly based on region. Here's a list:

```
Default: 107.178.231.0/24
Test: 107.178.232.0/24
Canada: TBD
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

## No Internet Install

This procedure will help you export what you need to run Shuffle on a no internet host.

1. Prerequise
* Both machines has Docker and Docker Compose installed already

* Your host machine already needs the images on it to make them exportable
2. Pull images on original machine

Shuffle need a few base images to work:

- shuffle-frontend
- shuffle-backend
- shuffle-orborus
- shuffle-worker
- shuffle:app_sdk
- opensearch
- shuffle-subflow

```
 docker pull ghcr.io/frikky/shuffle-backend & docker pull ghcr.io/frikky/shuffle-frontend & docker pull ghcr.io/frikky/shuffle-orborus &  docker pull frikky/shuffle:app_sdk & docker pull ghcr.io/frikky/shuffle-worker & docker pull opensearchproject/opensearch:1.3.2 & docker pull registry.hub.docker.com/frikky/shuffle:shuffle-subflow_1.0.0
```

Be careful with the versioning for opensearch, all other are going to use the tag "latest". 
You will also need to download and transfer ALL the apps you want to use. These can be discovered as such:

```
docker images | grep -i shuffle
```

3. Save images and archive them

```
mkdir shuffle-export & cd shuffle-export

docker save ghcr.io/frikky/shuffle-backend > backend.tar
docker save ghcr.io/frikky/shuffle-frontend > frontend.tar
docker save ghcr.io/frikky/shuffle-orborus > orborus.tar
docker save frikky/shuffle:app_sdk > app_sdk.tar
docker save ghcr.io/frikky/shuffle-worker:latest > worker.tar
docker save opensearchproject/opensearch:1.3.2 > opensearch.tar
docker save registry.hub.docker.com/frikky/shuffle:shuffle-subflow_1.0.0 > sublow.tar

git pull https://github.com/Shuffle/python-apps.git

wget https://raw.githubusercontent.com/Shuffle/Shuffle/master/.env
wget https://raw.githubusercontent.com/Shuffle/Shuffle/master/docker-compose.yml

cd .. & tar cvf shuffle-export.tar.gz shuffle-export
```

4. Export data to the targeted machine

Use scp, usb key, ..., to copy the previous archive to the machine. [More about manual transfers here](http://localhost:3002/docs/configuration#manual_docker_image_transfers)

5. Import docker images to host without internet
   
   ```
   tar xvf shuffle-export.tar.gz & cd shuffle-export
   find -type f -name "*.tar" -exec docker load --input "{}" \;
   ```

6. Deploy Shuffle without Internet

Create folders to add the python apps

```
mkdir shuffle-apps
cp -a python-apps/ * shuffle-apps/
```

Now, you just need to configure and install Shuffler like in normal procedure

## Uptime Monitoring

Uptime monitoring of Shuffle can be done by periodically polling the API for userinfo located at /api/v1/getinfo. This is an API that connects to our database, and which will be stuck if we any platform issues occur, whether in your local instance or in our Cloud instance on https://shuffler.io. 

Shuffle has and will not have any planned downtime for services on https://shuffler.io, and have built our architecture around being able to upgrade and roll back without any downtime at all. If this occurs in the future for our Cloud platform, we will make sure to notify any active users. We plan to launch a status monitor for our services in 2022.

**Basic monitoring** can be done with a curl request + sendmail + cronjob as [seen in this blogpost](https://www.programcreek.com/2017/06/automatically-detect-server-downtime-using-linux-cron-job/) with the curl command below. Your personal API key can be found on [https://shuffler.io/settings](https://shuffler.io/settings) or in the same location (/settings) in your local instance.

```
curl https://shuffler.io/api/v1/getinfo -H "Authorization: Bearer apikey"
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
  
  ```

Before you start:
If you have data of the same kind in the same index within Opensearch, these will be overwritten.
Example: you have the user "admin" in the index "users" within Opensearch and Datastore; this will be overwritten with the version that's in Datastore.

**Requirements**:

- Admin user in Shuffle using Datastore
- An available Elasticsearch / Opensearch database.

### 1. Set main database to be Datastore

- 1. Open .env

- 2. Scroll down and look for "SHUFFLE_ELASTIC"

- 3. Set it to false; SHUFFLE_ELASTIC=false
     
     ```
     
     ```

### 2. Set up Datastore and Opensearch

In order to run the migration, we have to run both databases at once, connected to Shuffle. This means to run both containers at the same time in the Docker-compose file like the image below, before restarting.

```
docker-compose down
## EDIT FILE
docker-compose pull
docker-compose up         # PS: Notice that we don't add -d here. This to make it easier to follow the logs. It's ok as we'll stop the instance later.
```

![Migration-1](https://github.com/frikky/shuffle-docs/blob/master/assets/migration-1.png?raw=true)

### 3. Find your API-key!

Now that you have both databases set up, we need to find the API-key.

```
1. http://localhost:3000/settings     # You may need to log in
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

To fix this issue, we need to set the version from 1.40 down to 1.35 in the Shuffle environment. This can be done by opening the docker-compose.yml file, then changing environment variable "DOCKER_API_VERSION" from 1.40 to 1.35 for the "orborus" service as seen below, then restarting Shuffle.

![Error with Docker version](https://github.com/frikky/shuffle-docs/blob/master/assets/configuration-error-1.png?raw=true)

## Debugging

As Shuffle has a lot of individual parts, debugging can be quite tricky. To get started, here's a list of the different parts, with the latter three being modular / location independent.

| Type                                        | Container name        | Technology       | Note                                                                                                       |
| ------------------------------------------- | --------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------- |
| Frontend                                    | shuffle-frontend      | ReactJS          | Cytoscape graphs & Material design                                                                         |
| Backend                                     | shuffle-backend       | Golang           | Rest API that connects all the different parts                                                             |
| Database                                    | shuffle-database      | Google Datastore | Has all non-volatile information. Will probably move to elastic or similar.                                |
| Orborus                                     | shuffle-orborus       | Golang           | Runs workers in a specific environment to connect locations. Defaults to the environment "Shuffle" onprem. |
| Worker                                      | worker-id             | Golang           | Deploys Apps to run Actions defined in a workflow                                                          |
| app sdk                                     | appname_appversion_id | Python           | Used by Apps to talk to the backend                                                                        |
| worker-8a666e4f-e544-440e-bf0f-4220e7cc9e25 |                       |                  |                                                                                                            |

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

## Docker socket

For now, the docker socket is required to run Shuffle. Whether you run with Kubernetes or another clustering technology, Shuffle WILL need access to ContainerD, which is what the docker socket provides.  

**Usage of the socket**:

* Backend (Not required, but used for app management)
* Orborus (Required, deploying Workers)
* Worker    (Required, deploying Apps. Apps DONT have access to the socket.)

**API's in use**

* Backend: Create, Make, Export docker images. No direct container management.
* Orborus: Download and Remove images. Make, List and Remove containers. Make, List and Remove services.
* Worker: Download and Remove images. Make, List and Remove containers. Make, List and Remove services.

## Hardening

This is a section to expand on hardening possibilities of the Shuffle environment, seeing as may use a lot of access, and allows for remote code execution.

TBD - expand these topics:

* Docker rootless
* Docker proxy
* Docker image regex
* Locked down server image (don't allow other commands than Docker)

## Database configuration

**TBD:** Everything below is tbd including swarm

1. Disable security options for docker-compose
2. Set username & password for opensearch to default admin:admin
3. Set to use https by default (https://shuffle-opensearch:9200)
4. Remove 9200 from being exposed


## Shuffle Server Healthcheck

There are multiple things to check in the Shuffle server to ensure that the health of server is in a good state:  

- Disk Space 
- Memory 
- Elasticsearch service state 

For this, the scripts have been prepared with the alerting mechanism which will check if everything is proper or not. 

### Disk Space Script 

This script will determine whether or not the disc space is more than 75% full. If so, an alert will be sent to your Webhook URL. Replace the script's <Webhook-URL> with your Webhook URL. 


```
#!/bin/sh
df -H | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }' | grep -v overlay | while read output;
do
  #echo $output
  usep=$(echo $output | awk '{ print $1}' | cut -d '%' -f1  )
  partition=$(echo $output | awk '{ print $2 }' )
  if [ $usep -ge 75 ]; then
    curl -X POST -H 'Content-type: application/json' --data '{"Alert":"Almost out of disk space","Server":"Local-Lab Shuffle Server"}' <Webhook-URL>
  fi
done
```

### Memory Check Script 

This script will determine whether or not the memory utilization is more than 70%. If so, an alert will be sent to your Webhook URL. Replace the script's <Webhook-URL> with your Webhook URL. 


```
#check server health
STATUS="$(curl http://172.17.14.102:3001/api/v1/_ah/health)"
if [ "${STATUS}" = "OK" ]; then
    :
else
    curl -X POST -H 'Content-type: application/json' --data '{"Alert":"There is a problem with this server(172.17.14.102), status is not OK"}' <Webhook-URL>
    exit 1
fi
```

### Elasticsearch Service Script 

This script will determine whether or not the Elasticsearch service is running or not. If not so, an alert will be sent to your Webhook URL. Replace the script’s <Elasticsearch-IP> with the Elasticsearch IP of your environment. Replace the script's <Webhook-URL> with your Webhook URL. 

```
#check server health
STATUS="$(curl <Elasticsearch-IP>)"
if [ "${STATUS}" = "OK" ]; then
    :
else
    curl -X POST -H 'Content-type: application/json' --data '{"Alert":"There is a problem with this server(172.17.14.102), status is not OK"}' <Webhook-URL>
    exit 1
fi
~
```

### Cron Jobs to automate the Process 

You can set a cron job to execute the scripts on every 15 minutes and the whole process can be automated. 

```
*/15 * * * * bash /root/diskspacecheck.sh
*/15 * * * * bash /root/healthchech.sh
*/15 * * * * bash /root/memorycheck.sh
```
