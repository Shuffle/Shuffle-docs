# Shuffle API 
Documentation for Shuffle API v1.0. Will be generated from OpenAPI by Shuffle version 1.0.0 and be replicable in our [API Explorer](https://shuffler.io/apps/edaa73d40238ee60874a853dc3ccaa6f)

## Table of contents
* [Introduction](#introduction)
* [Authentication](#authentication)
* [Responses](#responses)
* [Workflows](#workflow_api)
* [Apps](#app_api)
* [App Authentication](#app_authentication_api)
* [Users](#user_api)
* [Files](#file_api)
* [Datastore (Cache)](#datastore_api)
* [Notifications](#notifications)
  [Priorities - TBA](#priorities)
* [Environments - TBA](#environments)
* [Organizations - TBA](#organizations)
* [Integration Layer - TBA](#integration_layer)


## Introduction
Shuffle is a platform to build and execute [workflows](/docs/workflows) to help with automation and reduce burnout. It's built with an API structure in mind, and everything done has an API endpoint. The listed API's are built and generated with our own [OpenAPI creator](/docs/apps#create_openapi_app). All API's listed are for both versions of Shuffle (cloud/onprem), unless otherwise specified. Our OpenAPI specification can be [downloaded here](https://shuffler.io/apps/edaa73d40238ee60874a853dc3ccaa6f). Below are the base URL's for the API.

**Cloud:** https://shuffler.io/api/v1

**Onprem:** https://<endpoint>:<port>/api/v1

<b>PS:</b> API's are due to change before the full release, but nothing major at this point.

## Authentication
Shuffle uses [Bearer auth](https://swagger.io/docs/specification/authentication/bearer-authentication/) for authentication. This means that every request you send to the API, you need to send it with the header "Authorization: Bearer <APIKEY>". If Shuffle is multi-tenancy configured, you may have multiple organizations. If you want to specify the organization to use, you may add the header "Org-Id: <ORGID>". It will otherwise use the current active organization.

While logged in, you can go to https://shuffler.io/settings or /settings in your local instance to get your APIkey. Keep this safe. 

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



## Workflow API
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




## App API
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

### Delete an app 
Deletes an app if you have access to delete it.

Methods: DELETE

```
curl -XDELETE https://shuffler.io/api/v1/apps/{app_id} -H "Authorization: Bearer APIKEY"
```

### Upload a python app 
Uploads a python app. You should upload a zip file with the following like file structure. This has to be done for each individual version of the app. The app uploaded is available to everyone in the organization.

To zip an app, go to the folder's version, e.g. shuffle-tools/1.2.0, then type in the following (\*nix):
```
zip app.zip -r appname/version/*
```

This will give you the following structure.
``` 
App.zip
├── src
│   ├── app.py
├── api.yaml
├── Dockerfile
├── requirements.txt
```       

Methods: POST

```
curl https://shuffler.io/api/v1/apps/upload -H "Authorization: Bearer APIKEY" -F 'shuffle_file=@./your_file/file_path/app.zip'
```
**Success response** 
```
{"success": true, "id": "798f1234c4fb8b4a6300da3c546af45a"}
```	
	
### Get App Authentication
Get a list of all app authentication

Methods: GET

```
curl https://shuffler.io/api/v1/apps/authentication -H "Authorization: Bearer APIKEY"
```

**Success response** 
```
{"success": true, "data": []}
```

### Set Authentication Everywhere
When you have an authentication available, it is possible to set it everywhere using an API. This will update all your current workflows that uses that app to use the specified authentication.

Methods: POST

```
curl -XPOST https://shuffler.io/api/v1/apps/authentication/{authentication_id}/config -H "Authorization: Bearer APIKEY" -d '{"action"
: "assign_everywhere", "id": "authentication_id"}'
```

**Success response**
```
{"success": true}
```

### Delete App Authentication
Delete an authentication. PS: This does NOT change the ID of every workflow that utilizes the app.

Methods: DELETE

```
curl https://shuffler.io/api/v1/apps/authentication/{authentication_id} -H "Authorization: Bearer APIKEY"
```

**Success response** 
```
{"success": true}
```

### Add App Authentication
Add authentication to an app, available through e.g. the Workflow editor, or authentication explorer. When adding this, make sure the app has an ID (uuid) and name attached to it, and that the fields are matching the apps' description.

Method: PUT

```
curl -XPUT https://shuffler.io/api/v1/apps/authentication -H "Authorization: Bearer APIKEY" '{"app":{"name":"Jira","is_valid":true,"id":"1836c9786bb54748bd8913c0617d50fd","link":"","app_version":"1.0.0","sharing_config":"","generated":true,"downloaded":false,"sharing":false,"verified":false,"invalid":false,"activated":true,"tested":false,"hash":"","private_id":"1836c9786bb54748bd8913c0617d50fd","description":"The Jira app for creating and managing issues from shuffle workflow.","environment":"Shuffle","small_image":"","large_image":"","contact_info":{"name":"","url":""},"reference_info":{"documentation_url":"","github_url":""},"folder_mount":{"folder_mount":false,"source_folder":"","destination_folder":""},"actions":[],"authentication":{"type":"","required":true,"parameters":[{"description":"","id":"","name":"username_basic","example":"username","multiline":false,"required":false,"in":"","schema":{"type":"basic"},"scheme":"basic"},{"description":"","id":"","name":"password_basic","example":"*****","multiline":false,"required":false,"in":"","schema":{"type":"basic"},"scheme":"basic"},{"description":"The URL of the app","id":"","name":"url","example":"https://api-url","value":"https://api-url","multiline":false,"required":true,"in":"","schema":{"type":"string"},"scheme":""}],"redirect_uri":"","token_uri":"","refresh_uri":"","scope":null,"client_id":"","client_secret":""},"tags":["Case Management"],"categories":["Cases"],"created":0,"edited":0,"last_runtime":0,"versions":null,"loop_versions":null,"owner":"2b3a37f3-fdd2-4965-b78d-f5d2fe9a2572","public":false,"reference_org":"","reference_url":"","action_file_path":"","documentation":""},"fields":[{"key":"username_basic","value":"asd"},{"key":"password_basic","value":"qwe"},{"key":"url","value":"https://api-url"}],"label":"Auth for Jira","usage":[{"workflow_id":"a816852a-e197-4b02-ba4f-0b67bb1baf3d"}],"id":"04825afa-e37b-44ce-a571-a67c2e2fb956","active":true}'
```

**Success response** 
```
{"success": true, "id": "app_id"}
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
{"success": true, "reason": [{apps here}]}
```


### Download REMOTE apps
Describes how to download remote apps from a Github repository, including private ones.

## User API
Below are the endpoints related to user creation, editing, listing, apikey generation and more. 

### List users
Lists all available users. Requires admin rights.

Methods: GET

```
curl https://shuffler.io/api/v1/users/getusers -H "Authorization: Bearer APIKEY" 
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
curl https://shuffler.io/api/v1/users/updateuser -H "Authorization: Bearer APIKEY" -d '{"user_id": "USERID", "role": "user"}'
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
curl https://shuffler.io/api/v1/users/generateapikey -H "Authorization: Bearer APIKEY" -d '{"user_id": "id"}'
```


**Success response** 
```
{"success": true, "username": "username", "verified": false, "apikey": "new apikey"}
```

## App Authentication API
App Authentication is an API for handling authentication of apps themselves. You can interact with it through a workflow, an app, the admin panel, or the /apps/authentication UI. To use an authentication after it's made, it has to be mapped to an action in a workflow by it's ID.

### Create a new authentication
To use authentication, you first have to make one. Use the `configuration` fields for an app (get the app first to find these), and add them as fields with key:value in the request. 

Methods: POST 

```
curl https://shuffler.io/api/v1/apps/authentication -H "Authorization: Bearer APIKEY" -d '{"app":{"name":"Elasticsearch","app_version":"1.0.0","id":"971706758e274c2e4083f2621fb5a6f7"},"fields":[{"key":"username_basic","value":"asd"},{"key":"password_basic","value":"asd"},{"key":"url","value":"asd"}],"label":"Auth for Elasticsearch","id":"80dcedb1-bd43-4253-b837-a0470ce6681e","active":true}'
```


**Success response** 
```
{"success": true, "id": "80dcedb1-bd43-4253-b837-a0470ce6681e"}
```

### List auth
Gets all app auth

Methods: GET 

```
curl https://shuffler.io/api/v1/apps/authentication -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
[{"app":{"name":"Elasticsearch","app_version":"1.0.0","id":"971706758e274c2e4083f2621fb5a6f7"},"fields":[{"key":"username_basic","value":"asd"},{"key":"password_basic","value":"asd"},{"key":"url","value":"asd"}],"label":"Auth for Elasticsearch","id":"80dcedb1-bd43-4253-b837-a0470ce6681e","active":true, "usage": []}]
```

### Delete an authentication
Deletes an authentication. 

Methods: DELETE

```
curl -XDELETE https://shuffler.io/api/v1/apps/authentication/{authentication_id} -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success": true}
```

## Datastore API
Datastore is a persistent storage mechanism you can use for workflows to talk to each other between executions, or for normal storage. Below are the endpoints related to datastore (cache) creation, listing, deletion and more. This API is available to Python apps by using self.set_cache("key", "value") and self.get_cache("key")

### Add a key
To add or edit a cache key use 

Methods: POST, PUT

```
curl https://shuffler.io/api/v1/orgs/{org_id}/set_cache -H "Authorization: Bearer APIKEY" -d '{"key":"hi", "value":"1234"}'
```


**Success response** 
```
{"success": true}
```

### Get a key
Search for a cache key. For keys set in a workflow, it may unavailable with the normal API, and require execution_id & authorization in the JSON body.

Methods: POST

```
curl https://shuffler.io/api/v1/orgs/{org_id}/get_cache -H "Authorization: Bearer APIKEY" -d '{"org_id": "ORG_ID", "key": "hi"}'
```


**Success response** 
```
{"success":false,"workflow_id":"99951014-f0b1-473d-a474-4dc9afecaa75","execution_id":"f0b2b4e9-90ca-4835-bdd4-2889ef5f926f","org_id":"2e7b6a08-b63b-4fc2-bd70-718091509db1","key":"hi","value":"1234"}
```


### List all keys
List existing datastore (cache) keys

Methods: GET

```
curl https://shuffler.io/api/v1/orgs/{org_id}/list_cache -H "Authorization: Bearer APIKEY"
```


**Success response** 
```
{"success":true,"keys":[{"success":false,"workflow_id":"99951014-f0b1-473d-a474-4dc9afecaa75","execution_id":"f0b2b4e9-90ca-4835-bdd4-2889ef5f926f","org_id":"2e7b6a08-b63b-4fc2-bd70-718091509db1","key":"hi","value":"1234"}]}
```

### Delete a key
Deletes a key, completely removing all references to it

Methods: DELETE

```
curl -XDELETE https://shuffler.io/api/v1/orgs/{org_id}/cache/{cache_key} -H "Authorization: Bearer APIKEY"

```


**Success response** 
```
{"success": true}
```

## File API
Below are the endpoints related to file creation, uploading, downloading, listing and more. This API is available to Python apps by using self.set_files(files) and self.get_file(file_id)

### Create a file
Creating a file is necessary before uploading one. This is to prepare the file location which is always per-organization only. Use "global" for the workflow_id if it's not associated with one.

Methods: POST 

```
curl https://shuffler.io/api/v1/files/create -H "Authorization: Bearer APIKEY" -d '{"filename": "file.txt", "org_id": "your_organization", "workflow_id": "workflow_id", "namespace": "category", "labels": ["label1", "label2"]}'
```


**Success response** 
```
{"success": true, "id": "e19cffe4-e2da-47e9-809e-904f5cb03687"}
```

### Upload a file
Uploads a file to an ID created with the "Create a file" API function. This is only possible once and can't be overwritten.

Methods: POST 

```
curl https://shuffler.io/api/v1/files/{file_id}/upload -H "Authorization: Bearer db0373c6-1083-4dec-a05d-3ba73f02ccd4" -F 'shuffle_file=@./your_file/file_path/with_a_file.txt'
```


**Success response** 
```
{"success": true, "id": "e19cffe4-e2da-47e9-809e-904f5cb03687"}
```

### List files
Gets the meta for all files (up to 1000)

Methods: GET 

```
curl https://shuffler.io/api/v1/files -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
[{"id":"e19cffe4-e2da-47e9-809e-904f5cb03687","type":"","created_at":1614015359,"updated_at":1614015521,"meta_access_at":0,"last_downloaded":0,"description":"","expires_at":"","status":"active","filename":"file.txt","url":"","org_id":"b199646b-16d2-456d-9fd6-b9972e929466","workflow_id":"global","workflows":null,"download_path":"shuffle-files/b199646b-16d2-456d-9fd6-b9972e929466/global/e19cffe4-e2da-47e9-809e-904f5cb03687","md5_sum":"3917d8dbd72e73a2db92ad5bb6544940","sha256_sum":"3f25c3613d658ecdd7ee9b7777193ffb084ebe43e641f6daa3c3181f0b631c08","filesize":1061,"duplicate":false,"subflows":null}, {"id":"e19cffe4-e2da-47e9-809e-904f5cb03687","type":"","created_at":1614015359,"updated_at":1614015521,"meta_access_at":0,"last_downloaded":0,"description":"","expires_at":"","status":"active","filename":"file.txt","url":"","org_id":"b199646b-16d2-456d-9fd6-b9972e929466","workflow_id":"global","workflows":null,"download_path":"shuffle-files/b199646b-16d2-456d-9fd6-b9972e929466/global/e19cffe4-e2da-47e9-809e-904f5cb03687","md5_sum":"3917d8dbd72e73a2db92ad5bb6544940","sha256_sum":"3f25c3613d658ecdd7ee9b7777193ffb084ebe43e641f6daa3c3181f0b631c08","filesize":1061,"duplicate":false,"subflows":null}]
```

### Download a file
Gets the file CONTENT of a file 

Methods: GET 

```
curl https://shuffler.io/api/v1/files/{file_id}/content -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
THIS IS SOME TEXT INSIDE A TEXTFILE HELLO :)
```

### Get file meta data
Gets metadata for a file, as well as some security relevant info like MD5 and Sha256 sum. 

Methods: POST 

```
curl https://shuffler.io/api/v1/files/{file_id} -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"id":"e19cffe4-e2da-47e9-809e-904f5cb03687","type":"","created_at":1614015359,"updated_at":1614015521,"meta_access_at":0,"last_downloaded":0,"description":"","expires_at":"","status":"active","filename":"file.txt","url":"","org_id":"b199646b-16d2-456d-9fd6-b9972e929466","workflow_id":"global","workflows":null,"download_path":"shuffle-files/b199646b-16d2-456d-9fd6-b9972e929466/global/e19cffe4-e2da-47e9-809e-904f5cb03687","md5_sum":"3917d8dbd72e73a2db92ad5bb6544940","sha256_sum":"3f25c3613d658ecdd7ee9b7777193ffb084ebe43e641f6daa3c3181f0b631c08","filesize":1061,"duplicate":false,"subflows":null}
```

### Delete a file
Deletes a file. The file meta is left intact, but the file itself is removed from existence. Status is changed to "deleted".

Methods: DELETE

```
curl -XDELETE https://shuffler.io/api/v1/files/{file_id} -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success": true}
```

### Edit an existing file
Edit an active file with existing content (/upload) for first uploads. The file meta is left intact, except for the hash sums, sizing and timestamps. This function is meant to be used together with [file categories](#get_file_category) to e.g. handle Detection rules.

Methods: PUT

```
curl -XPUT https://shuffler.io/api/v1/files/{file_id}/edit -H "Authorization: Bearer APIKEY" -d 'this is the new content of the file'
```


**Success response** 
```
{"success": true}
```

### Get file category
Gets all files in a namespace zipped. The point of this function is to be able to load in multiple files at once in order to e.g. run detections. By adding the query ids=true, it will instead give you a list of all the files. When receiveing file it will automatically deduplicate files with the same Sha256 hash.

Methods: GET

```
curl https://shuffler.io/api/v1/files/namespaces/{category} -H "Authorization: Bearer APIKEY"
```

**?id=true**
```
{"success": True, "list": [{
	"name": "Filename",
	"id": "file_uuid",
},
{
	"name": "Filename2",
	"id": "file_uuid2",
}]}
```

**Success response** 
```
<ZIPFILE WITH ALL FILES IN CATEGORY>
```


## Triggers
Triggers in Shuffle have their own custom usage and APIs. 

### Get all schedules
Get all schedules

Methods: GET 

```
curl https://shuffler.io/api/v1/workflows/schedules -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
[{"id":"cabaaffc-db53-4e19-ad8b-4f5fc0dc49c9","start_node":"","seconds":0,"workflow_id":"7b8ffd74-5e67-4700-bf79-751d1ac7e5e4","argument":"{\"start\":\"\",\"execution_source\":\"schedule\",\"execution_argument\":\"{\\\"example\\\": {\\\"json\\\": \\\"is cool\\\"}}\"}","wrapped_argument":"{\"start\":\"\",\"execution_source\":\"schedule\",\"execution_argument\":\"{\\\"example\\\": {\\\"json\\\": \\\"is cool\\\"}}\"}","appinfo":{"sourceapp":{"foldername":"","name":"","id":"","description":"","action":""},"destinationapp":{"foldername":"","name":"","id":"","description":"","action":""}},"finished":false,"base_app_location":"","org":"37217426-f794-429c-a0f9-548f7055af45","createdby":"","availability":"","creationtime":1641573762,"lastmodificationtime":1641573762,"lastruntime":1641573762,"frequency":"*/15 * * * *","environment":""}]
```

### Schedule a workflow
Schedule a workflow to run at certain intervals. The node in the workflow must exist.

Methods: POST 

```
curl -XPOST https://shuffler.io/api/v1/workflows/{workflow_id}/schedule -H "Authorization: Bearer APIKEY" -d '{"name":"Schedule","frequency":"*/25 * * * *","execution_argument":"{\"example\": {\"json\": \"is cool\"}}","environment":"cloud","id":"cabaaffc-db53-4e19-ad8b-4f5fc0dc49c9"}'
```


**Success response** 
```
{"success":true}
```

### Stop a workflow schedule
Stop a schedule from running

Methods: DELETE 

```
curl -XDELETE https://shuffler.io/api/v1/workflows/{workflow_id}/schedule/{schedule_id} -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success":true}
```

### Create and start webhook
Start a new webhook

Methods: POST 

```
curl -XPOST https://shuffler.io/api/v1/hooks -H "Authorization: Bearer APIKEY" -d '{"name":"Webhook_1","type":"webhook","id":"db434f8c-a9cb-47ec-abf8-ad8fb10e5809","workflow":"7b8ffd74-5e67-4700-bf79-751d1ac7e5e4","start":"6601f07f-92f2-45d3-88bf-328db7bfdfa0","environment":"cloud","auth":""}'
```


**Success response** 
```
{"success":true}
```

### Delete and stop webhook
Stop a running webhook from being available

Methods: DELETE 

```
curl -XDELETE https://shuffler.io/api/v1/hooks/{webhook_id} -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success":true, "reason": "Stopped webhook"}
```

### Create Outlook Subscription
TBA

### Delete Outlook Subscription
TBA

### Create Gmail Subscription
TBA

### Get Gmail Subscription
TBA

### Delete Gmail Subscription
TBA


## Notifications 
Below are the API's associated with Notifications in Shuffle. These can be listed, marked as read, and cleared.

### Get all notifications
Get all notifications assigned to your user from your organizations 

Methods: GET 

```
curl https://shuffler.io/api/v1/notifications -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success":true,"notifications":[{"image":"","created_at":1638898114,"updated_at":1638898114,"title":"Error in Workflow \"Shuffle Workflow helloooo\"","description":"Node shuffle_tools_1 in Workflow Shuffle Workflow Winner announcement was found to have an error. Click to investigate","org_id":"","user_id":"","tags":null,"amount":1,"id":"057bf2b5-d29d-4bb4-bf2f-d8a6ee882dfe","reference_url":"/workflows/1693bf4a-b0f4-46dd-8257-448cbc6b0e9b?execution_id=74adf061-f949-4392-9e2d-1fd5e3381037\u0026view=executions\u0026node=ef683a39-4c2b-4c83-ad2d-d28a922e44b4","org_notification_id":"60a22356-1028-4226-b755-51804e3a25a2","dismissable":true,"personal":true,"read":false}]}
```

### Mark all notifications as read
Clears all notifications

Methods: GET 

```
curl https://shuffler.io/api/v1/notifications/clear -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success":true}
```

### Mark notification as read
Marks a single notification as read

Methods: GET 

```
curl https://shuffler.io/api/v1/notifications/{notificationId}/markasread -H "Authorization: Bearer APIKEY" 
```


**Success response** 
```
{"success":true}
```

## Environments 
TBA

## Organization API
Below are the endpoints related to organization creation, editing, listing and more. These will probably not be live until 1.0.0.

**TBA**



## Integration Layer
The Integration Layer of Shuffle is a way to interact with apps a new way. It utilizes Apps that are categorized and labeled, and gives access to API's for specific actions for each of those labels. Behind the scenes there is always a workflow for each of these, and Shuffle wants to give granular control of each individual Workflow if wanted. 

### Get Active Categories
To find what categories with what apps you have that are active, run this API. It will return with what categories and actions for those categories you have available. This is based on the current organization.
	
Methods: GET 

```
curl https://shuffler.io/api/v1/apps/categories -H "Authorization: Bearer APIKEY"
```


**Success response** 
```
[{"name":"Cases","color":"","icon":"cases","action_labels":["Create ticket"], "app_labels": 
	[{
		"app_name":"PagerDuty","large_image":"","id":"50af6d9f18134b90aabca9180b37ea01","labels":[{"category":"Cases","label":"Create ticket"}]
	]}
}]
```
		
### Run a Category Action
Runs the category action in a standardized format.
	
Methods: POST 

```
curl -XPOST https://shuffler.io/api/v1/apps/categories/run -H "Authorization: Bearer APIKEY" -d '{
	"app_name": "PagerDuty",
	"category": "cases",
	"label": "create_ticket",
	"fields": [{
		"key": "title",
		"value": "This is the title"
	}, {
		"key": "description",
		"value": "This is the description"
	}, {
		"key": "source",
		"value": "Shuffle"
	}]
}'
```






