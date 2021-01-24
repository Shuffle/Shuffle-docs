# Apps
Documentation for app creation. 

**PS: This is not finished, but is based on [WALKOFF](https://walkoff.readthedocs.io/en/master/apps.html). We will document it before 1.0 launch.**

# Table of contents
* [Introduction](#introduction)
* [Manual creation (python3.7)](#manual)
* [Development Instructions](#development_instructions)
* [App editor](#app_editor)

## Introduction
Apps are how you complete work in Shuffle. At a high level, you define a Workflow that starts based on a schedule, or some expected event (webhook received, etc), and that in turn runs one or more apps. An app takes input (argument data to act on, credentials, etc), uses that to complete some work, and returns resulting data to Shuffle to store, display, or feed into another app for further processsing.

The underlying design of Apps in Shuffle are based on [WALKOFF](https://walkoff.readthedocs.io/en/master/apps.html) with minor differences. Most of the documentation below will therefore be close to their approach.

[More about apps](/docs/apps)

The premise behind all apps that run in Shuffle, is that they each run in an isolated Docker container, for security purposes. You provide arguments to an app in a Shuffle workflow, and when the workflow is run, your app is reached in the control flow, it will be launched as a new container. Shuffle then sends the apps argument data, and the container destroyed when the app's work is completed.

## Why create a custom app?
There are many prebuilt apps in Shuffle, and all complete some action. There may an integration you need that doesn't exist yet. This guide will walk you through the process.
Always remember the key components of the app:
* What functions are available in the app?
* What arguments are needed for the app to function? - e.g. authentication arguments, json data structure arguments.
* What is the output of this function, and what are we doing with that resulting data? e.g. send an email, create a ticket, send to another app for conditional 		processing.
	
	

## Manual 
The minimal directory structure for a Shuffle application is as follows:

```
Shuffle
+-- apps
	+-- app_name (virustotal)
		+-- version_number (1.0.0)
			|-- api.yml   				# Has the full app configuration - must match app.py 
			|-- Dockerfile				# Contains Shuffle build instructions 
			|-- requirements.txt 	# Extra packages to be used by the app 
			+-- src 							
				+-- app.py 					# The base python file for everything related to your application
				+-- yourcustom_app.py				# More complex apps can have an entire directory stucture, imported and called by app.py
	+-- another_app_1 
	+-- another_app_2
```

### Development Instructions

In our example, we are going to develop an app that connects to an api for office365, pulls some log data, and returns it as a json data structure.
We first think about the 3 primary elements:<br>
* What actions / functions will we create?
	* We will have a function to poll the last 10 minutes of audit logs from the office api
	* We will have a funtion to poll the last 23 hours of audit logs from the office api -- testing only purposes
* What arguments are needed for the app to run?
	* We need some arguments for authentication (Based on office365 authentication, we have planType,tenantID,clientID,clientSecret)
	* Note that your app may also receive json_data structure arg as part of a prior app action, you are note limited here.
* What is the output data?
	* We expect a json data structure that contains one audit log entry per json object.

With our 3 elements in mind, lets build the script on your own. This example is python3, but some additional work would allow any app type/language. For now the expectation is that you would build this in python3.

Build your python functions with the expected arguments, and ensure it returns the expected output. Once the code works in your environment, you can then integrate into Shuffle apps directory to integrate as an app.

With your python script built, we must build a directory structure, some metadata files, and modify a base app.py file to run your code from Shuffle.
In your shuffle server, there is a shuffle-apps directory, typically under the top level dir where you cloned the github repo.

/Shuffle/shuffle-apps/

This directory contains a list of folders, one per app in Shuffle. There is a template app called python-playground that we will clone and edit.
First make your app folder, note this folder should not contain spaces.
```
cd /Shuffle/shuffle-apps
mkdir office365mgmt
cp -R /Shuffle/shuffle-apps/python-playground/* .
```
The directory structure under the app folder should match the expected above.
The above will make your app folder, and copy the template files from python-playground to your app, you will modify these shortly.
Now using winscp, or some other method, upload your python app to the /src/ directory of your apps folder.

Now that your app's .py script is uploaded under /Shuffle/shuffle-apps/office365mgmt/src, you'll tell Shuffle how to use it.

We will modify 3 files:
* api.yaml
* requirements.txt -- Specify any modules that your app uses, which will be installed via pip
* src/app.py -- The base app that is called by Shuffle, which in turn will call your python script's functions

### api.yaml

api.yaml is what provides shuffle information about your app. Here we define your apps name, description, author info, actions (functions available), and the paremeters that each function takes.

I will show you the office365mgmt app settings, but feel free to explore other apps api.yaml to see other obscure options.

* name: Office365 Mgt Api -- This is your apps display name as seen in Shuffle GUI. You can put whitespace here, but _ may be better
* description: Some description -- Your apps description that will display in Shuffle GUI
* contact_info: If you are maintaining this, please share your details with users

Code Snippet
```
app_version: 1.0.0
name: Office365 Mgt API
description: Collect AzureActiveDirectory,Exchange,Sharepoint,General, DLP audit logs
contact_info:
  name: "@RobertEvans"
  url: https://shuffler.io
  email: rob.evans512@gmail.com
```
#### Authentication

The next section for me is authentication, my app needs some data to obtain an api token. Not all apps need this step, but if yours requires a key, secret, or password, it is recommended to use a specialized "authentication" declaration in api.yaml, so those credentials are stored safely, and not displayed in cleartext in your Shuffle workflow.

Here I define that my app requires authentication, and a list of parameters, which is a list of arguments specified by -name. The name value can be anything your want, but note this is the name of the argument when passed to app.py, and ultimately your app.

My app expects 4 arguments, that I consider privileged information that should be stored as an authentication object. When this app is run, this credential object once configured in Shuffle will be sent to the app to use.

My first argument is a string called "planType". In my workflow if the office365 account I have is Enterprise, I'd populate that, and it would get sent to the app to use.
* name: case sensitive authentication argument name
* description: The description shoulds common values for this argument
* example: The example is a placeholder syntax in absence of a value in user interface. 
* required: specifies whether it is mandatory to run the app
* schema: The type of variable can be specified, string is the only one tested but ideally any type could be used here. You can do type casting in your app from string later.
```
authentication:
  required: true
  parameters:
    - name: planType
      description: Enterprise, GCC , GCCHigh, DoD
      example: "Enterprise"
      required: true
      schema:
        type: string
    - name: tenantID
      description: xxxx-xxxx-xxxx-xxxx
      example: "xxxx-xxxx-xxxx-xxxx"
      required: true
      schema:
        type: string
    - name: clientID
      description: xxxx-xxxx-xxxx-xxxx
      example: "xxxx-xxxx-xxxx-xxxx"
      required: true
      schema:
        type: string
    - name: clientSecret
      description: xxxx-xxxx-xxxx-xxxx
      example: "*****"
      required: true
      schema:
        type: string
	
```

#### Actions

```
actions:
  - name: run_o365poller
    description: Run office365 audit poller for defined interval
    parameters:
      - name: json_data
        description: The JSON to handle
        required: false
        multiline: true
        example: 'No args for now, insert credentials and get returned data'
        schema:
          type: string
      - name: PollInterval
        description: The selected python function to run
        required: true
        multiline: true
        example: '1'
        options:
          - poll_10min
          - poll_23hours
        schema:
          type: string
    returns:
      schema:
        type: string
large_image: data:image/png;base64,
Here is a excerpt of the template code:
```
app_version: 1.0.0
name: Python3 playground
description: A test app made for you to personally change the code
contact_info:
  name: "@frikkylikeme"
  url: https://shuffler.io
  email: frikky@shuffler.io
actions:
  - name: run_python_script
    description: Runs a python script defined by YOU
    parameters:
      - name: json_data
        description: The JSON to handle
        required: true
        multiline: true
        example: '{"data": "testing"}'
        schema:
          type: string
      - name: function_to_execute
        description: The selected python function to run
        required: true
        multiline: true
        example: '1'
        options:
          - function_1
          - function_2
        schema:
          type: string
    returns:
      schema:
        type: string
large_image: data:image/jpg;base64,/9j/4AAQSkZJR
```


### requirements.txt

### src/app.py



### Old Development Instructions
These instructions will indicate how to make an app for Virustotal and make it available in Shuffle. We recommend building them following our step by step instructions. 

1. Setup

Start by developing your app and its functions in a standalone script outside of WALKOFF – this way you can get basic functionality down before dealing with WALKOFF.

Note: all functions that you expect to turn into actions must be written for asyncio (i.e. async def function_name())

EXAMPLE: Below is example code that can be used to interact with VirusTotal’s Api as a standalone script

## App Editor
TBD: Finish app editor: OpenAPI
