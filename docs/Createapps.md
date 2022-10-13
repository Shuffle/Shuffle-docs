# Creating Shuffle Apps 
Documentation for Shuffle Apps

## Installation guide

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) installed.
2. Download Shuffle
```
git clone https://github.com/frikky/Shuffle
cd Shuffle
```
3. Run docker-compose.
```
docker-compose up -d
```
NOTE - after run this docker compose command go to your docker and stop the shuffle-frontend container

## Creating app using OpenAPI

1. go to the https://shuffler.io/
2. If you are new in shuffle click on register input username and password click submit
3. click on Apps 
    - here see App creator panel in this have 2 option CREATE FROM OPENAPI or CREATE FROM SCRATCH
4. click on CREATE FROM OPENAPI 
    - open one popup menu is 'create a new app'
    - Paste in the URI for the OpenAPI Or upload a - YAML or JSON specification
5. click on CREATE FROM SCRATCH
    - input general information
        - image 
        - name
        - description

    - input API information
        - base URL
        - Authentication

    - Action
        - Actions are the tasks performed by an app usually single URL paths for REST API's.

## Creating app using Python code
1. setup shuffle on your local machine steps given above "Installation guide".
2. copy your app folder and paste that copied folder into this shuffle-apps folder 
3. For test this apps run your local shuffle and test the apps
    - login with username as admin and password as admin
    - click into apps 
    - into apps click the buttton reload app locally 


