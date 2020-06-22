# API 
Documentation for Shuffle API v1.0

# Table of contents
* [Introduction](#introduction)
* [Authentication](#authentication)
* [Responses](#responses)
* [Workflows](#workflows)
* [Apps](#apps)
* [Users](#users)

## Introduction
Shuffle is a platform to build and execute [workflows](/docs/workflows) to help with automation and reduce burnout. It's built with an API structure in mind, and everything done has an API endpoint. The listed API's are built and generated with our own [OpenAPI creator](/docs/apps#create_openapi_app). All API's listed will use the https://shuffler.io endpoint, but you can change it for your local instance.

**Cloud:**: https://shuffler.io/api/v1
**Onprem:**: https://<endpoint>:<port>/api/v1

<b>PS:</b> API's are due to change before the full release, but nothing major at this point.

## Authentication
Shuffle uses [Bearer auth](https://swagger.io/docs/specification/authentication/bearer-authentication/) for authentication. This means that every request you send to the API, you need to send it with the header "Authorization: Bearer <APIKEY>".  

While logged in, you can go to https://shuffler.io/settings to get your APIkey. Keep this safe. 

**Get all apps example**
```
curl https://shuffler.io/api/v1/apps -H "Authorization: Bearer APIKEY"
```

**Authentication failure**
Status code: 401
```
{"success": false}
```


## Responses
Shuffle responses follow the response codes listed below. The data you can expect is mostly in the following json form, whether success or failure.

```
{
	"success": <true/false>,
	"reason": "You failed to do something"
}
```


| Code 	 | Description   |
| ------ | ------------- |
| 200    | Successful request. Usually contains information about the success. |
| 401    | Not authorized, or an error occurred. Usually contains a reason for the error. |
| 405    | Method not allowed. We use GET/POST/PUT/DELETE |
| 500    | A backend error occurred. |

**TBD: Add proper example responses for each.**



## Workflows
Workflows are used to execute your automations, and has endpoints related to creation, triggers, saving and deleting, aborting and listing.

### List all workflows
Return a list of all existing workflows

Method: GET

```
curl https://shuffler.io/api/v1/workflows -H "Authorization: Bearer APIKEY"
```


### List workflow executions
Returns a list of executions for a given workflow

Method: GET

```
curl https://shuffler.io/api/v1/workflows/{workflow_id}/executions -H "Authorization: Bearer APIKEY"
```


### Get specific workflow
Returns a given workflow

Method: GET

```
curl https://shuffler.io/api/v1/workflows/{workflow_id} -H "Authorization: Bearer APIKEY"
```


### Create new workflow
Creates a basic workflow with a given name and description. Returns a startpoint for a workflow. 

Method: POST

```
curl -XPOST https://shuffler.io/api/v1/workflows -H "Authorization: Bearer APIKEY" -d '{"name": "Example API workflow", "description": "Description for the workflow"}'
```

**Success response**
```
{"actions":[],"branches":[],"triggers":[],"schedules":null,"id":"25cb3cc6-f343-4511-827f-b60557043327","is_valid":true,"name":"Example API workflow","description":"Description for the workflow","start":"","owner":"4669463f-f98e-4d86-891d-76edac4356c6","sharing":"private","execution_org":{"name":"","org":"","users":null,"id":""},"workflow_variables":null}
```


### Save a workflow
Saves a workflow with a given WORKFLOW_ID. Requires WORKFLOW_ID from [Create new workflow](/docs/API#create_new_workflow) to match in the parameter and the data sent.

**PS: This function is destructive and does not check everything, but will return if there are missing apps or similar**

Method: PUT

```
curl -XPUT http://shuffler.io/api/v1/workflows/WORKFLOW_ID -H "Authorization: Bearer APIKEY" --data '{"actions":[],"branches":[],"triggers":[],"schedules":null,"id":"WORKFLOW_ID","is_valid":true,"name":"Example workflow","description":"Description for the workflow","start":"","owner":"4669463f-f98e-4d86-891d-76edac4356c6","sharing":"private","execution_org":{"name":"","org":"","users":null,"id":""},"workflow_variables":null}'
```

**Success response** 
```
{"success": true}
```


### Delete a workflow
Deletes a workflow with a given ID.

Method: DELETE

```
curl -XDELETE http://shuffler.io/api/v1/workflows/apcb3cc6-f343-4511-827f-b60557043327 -H "Authorization: Bearer APIKEY" 
```

**Success response** 
```
{"success": true}
```


### Execute workflow
Executes a given workflow with optional arguments "execution_argument" and "start". Start is the node to execute from.  

Methods: POST, GET

```
curl -XPOST https://shuffler.io/api/v1/workflows/{workflow_id}/execute -H "Authorization: Bearer APIKEY" -d {"execution_argument": "DATA TO EXECUTE WITH", "start": "",}
```

**Success response** 
```
{"success": true, "execution_id": "6e58639e-a24f-4af8-b62b-d6fcc2bc10f4", "authorization": "26fb304f-92c9-4ca5-9735-9173ce80569e"}
```


### Get execution results
Gets an execution based on results from [Execute workflow](/docs/api#execute_workflow). Requires execution_id and authorization parameters. You can only use the authorization key in the data itself to get the ID, not in the header. To track progress, call this every few seconds and look for updates to "results" (json["results"]).

Methods: POST

```
curl -XPOST https://shuffler.io/api/v1/streams/results -d '{"execution_id": "ad9baac7-dc30-42da-bb1f-18b84309cfb7", "authorization": "62b3de56-9de0-4983-ad72-e63c42d123f8"}'
```

**Success response** 
```
{"type":"workflow","status":"ABORTED","start":"","execution_argument":"DATA TO EXECUTE WITH","execution_id":"ad9baac7-dc30-42da-bb1f-18b84309cfb7","workflow_id":"8f3c6a10-f5ca-432c-aef9-c5e038166c45","last_node":"","authorization":"62b3de56-9de0-4983-ad72-e63c42d123f8","result":"","started_at":1591074812,"completed_at":1591074857,"project_id":"shuffle","locations":["europe-west2"],"workflow":{"actions":[{"app_name":"testing","app_version":"1.0.0","app_id":"c567fc10-9c15-403e-b72c-6550e9e76bc8","errors":null,"id":"de10798e-2c66-4e0c-bfdd-8b645a8e3748","is_valid":true,"isStartNode":true,"sharing":true,"private_id":"","label":"testing_1","small_image":"","large_image":"","environment":"Shuffle","name":"repeat_back_to_me","parameters":[{"description":"message to repeat","id":"","name":"call","example":"","value":"232.21.10.12","multiline":true,"action_field":"","variant":"STATIC_VALUE","required":true,"schema":{"type":"string"}}],"position":{"x":-326.750381666118,"y":52.50022245682308},"priority":0},{"app_name":"Virustotal","app_version":"1.0.0","app_id":"e5d625cee91f5f8328f2f4ef09ef313e","errors":null,"id":"bdec0a1c-381c-4e90-ba04-db40db98406c","is_valid":true,"isStartNode":false,"sharing":false,"private_id":"e5d625cee91f5f8328f2f4ef09ef313e","label":"Virustotal_1","small_image":"","large_image":"","environment":"Shuffle","name":"get_ip_report","parameters":[{"description":"The apikey to use","id":"","name":"apikey","example":"","value":"","multiline":false,"action_field":"VT APIKEY","variant":"WORKFLOW_VARIABLE","required":true,"schema":{"type":"string"}},{"description":"Generated by shuffler.io OpenAPI","id":"","name":"ip","example":"","value":"128.0.0.11","multiline":false,"action_field":"","variant":"STATIC_VALUE","required":true,"schema":{"type":"string"}}],"position":{"x":-657.9998647811465,"y":52.000953074820615},"priority":0}],"branches":[{"destination_id":"bdec0a1c-381c-4e90-ba04-db40db98406c","id":"7ad84769-3e7f-48af-af73-802bc93b5c2c","source_id":"de10798e-2c66-4e0c-bfdd-8b645a8e3748","label":"","has_errors":false,"conditions":null}],"triggers":null,"schedules":null,"id":"8f3c6a10-f5ca-432c-aef9-c5e038166c45","is_valid":true,"name":"VT testing","description":"Helo","start":"de10798e-2c66-4e0c-bfdd-8b645a8e3748","owner":"4669463f-f98e-4d86-891d-76edac4356c6","sharing":"private","execution_org":{"name":"","org":"","users":null,"id":""},"workflow_variables":[{"description":"","id":"ec16e9a6-5d13-46ba-8613-ebf301569f44","name":"VT APIKEY","value":""}]},"results":null}
```


### Abort workflow

Aborts an execution based on a WORKFLOW_ID and EXECUTION_ID. Can only be done while the status is "EXECUTING".

Methods: GET

```
curl https://shuffler.io/api/v1/workflows/{workflow_id}/executions/{execution_id}/abort -H "Authorization: Bearer APIKEY"
```

**Success response** 
```
{"success": true}
```




## Apps 
Apps are the building blocks used in [workflows](/docs/apps#workflows), as they contain the actions to be executed. First of all, there are two types of apps:

* Generated from OpenAPI
* Self-made with Python

Here's how to distinguish them for now:
* OpenAPI: app.activated & app.generated = true, and app.private_id length > 0
* Normal: Opposite of OpenAPI

### Get apps
Returns a list of existing apps that you have access to, including private ones.

Methods: GET

```
curl https://shuffler.io/api/v1/apps -H "Authorization: Bearer APIKEY"
```


### Search existing apps 
Returns a list of apps that are hidden in the backend, e.g. OpenAPI apps loaded from [Security API's](https://github.com/frikky/OpenAPI-security-definitions). Requires the search parameter. 

Example: {"search": "secure"} will match both "secureworks" and "Cisco openVuln", because Secureworks has "secure" in its name and Cisco uses "secure" in its description.

Methods: POST

```
curl https://shuffler.io/api/v1/apps/search -H "Authorization: Bearer APIKEY" -d '{"search": "APPNAME"}'
```

**Success response** 
```
{"success": true, "reason": [{apps here}]
```


### Download REMOTE apps
Describes how to download remote apps from a Github repository, including private ones.

## Users 
Below are the endpoints related to user creation, editing, listing, apikey generation and more. 

**PS: These are NOT accurate for https://shuffler.io yet.**

### List users
Lists all available users. Requires admin rights.

Methods: GET

```
curl https://shuffler.io/api/v1/users -H "Authorization: Bearer APIKEY" 
```

**Success response** 
List of users

### Register a new user 
Registers a user based on the username and password provided. If it's the first user, it can be done by anyone, otherwise only admins.

Methods: POST

```
curl https://shuffler.io/api/v1/users/register -H "Authorization: Bearer APIKEY" -d '{"username": "username", "password": "P@ssw0rd"}'
```


**Success response** 
```
{"success": true}
```

### Update a user
Updates a user. Requires admin rights. 

Supported fields: 
* username 
* role (admin/user)

Methods: PUT

```
curl https://shuffler.io/api/v1/users/register -H "Authorization: Bearer APIKEY" -d '{"user_id": "USERID", "role": "user"}'
```


**Success response** 
```
{"success": true}
```

### Deactivates a user
Deactivates a user. This exists instead of a deletion method. Requires admin rights.

Method: DELETE 

```
curl -XDELETE https://shuffler.io/api/v1/users/{userid} -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success": true}
```

### Get new apikey
Re-generates a new apikey. Requires admin for POST. GET changes YOUR apikey. The API-key will always be 36 in length ([uuid](https://en.wikipedia.org/wiki/Universally_unique_identifier))

Methods: GET, POST (admin)

```
curl https://shuffler.io/api/v1/users/generateapikey -H "Authorization: Bearer APIKEY" -d '{"user_id": "id"}
```


**Success response** 
```
{"success": true, "username": "username", "verified": false, "apikey": "new apikey"}
```
