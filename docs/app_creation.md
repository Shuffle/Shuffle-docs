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
	What functions are available in the app?
	What arguments are needed for the app to function? - e.g. authentication arguments, json data structure arguments.
	What is the output of this function, and what are we doing with that resulting data? e.g. send an email, create a ticket, send to another app for conditional 		processing.
	
	

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
We first think about the 3 primary elements:
	What actions / functions will we create?
		We will have a function to poll the last 10 minutes of audit logs from the office api
		We will have a funtion to poll the last 23 hours of audit logs from the office api -- testing only purposes
	What arguments are needed for the app to run?
		We need some arguments for authentication (Based on office365 authentication, we have planType,tenantID,clientID,clientSecret)
		Note that your app may also receive json_data structure arg as part of a prior app action, you are note limited here.
	What is the output data?
		We expect a json data structure that contains one audit log entry per json object.

With our 3 elements in mind, lets build the script on your own. This example is python3, but some additional work would allow any app type/language. For now the expectation is that you would build this in python3.

Build your python functions with the expected arguments, and ensure it returns the expected output. Once the code works in your environment, you can then integrate into Shuffle apps directory to integrate as an app.

With your App built, we must build a directory structure, some metadata files, and modify a base app.py file to run your code.
In your shuffle server, there is a shuffle-apps directory, typically under the top level dir where you cloned the github repo.

/Shuffle/shuffle-apps/

This directory contains a list of folders, one per app in Shuffle. There is a template app called python-playground that we will clone and edit.
First make your app folder, note this folder should not contain spaces.
```
cd /Shuffle/shuffle-apps
mkdir office365mgmt
cp -R /Shuffle/shuffle-apps/python-playground/* .
```
The directory structure under the app folder such match the expected above.
The above will make your app folder, and copy the template files from python-playground to your app, you will modify these shortly.
Now using winscp, or some other method, upload your python app to the /src/ directory of your apps folder.






### Old Development Instructions
These instructions will indicate how to make an app for Virustotal and make it available in Shuffle. We recommend building them following our step by step instructions. 

1. Setup

Start by developing your app and its functions in a standalone script outside of WALKOFF – this way you can get basic functionality down before dealing with WALKOFF.

Note: all functions that you expect to turn into actions must be written for asyncio (i.e. async def function_name())

EXAMPLE: Below is example code that can be used to interact with VirusTotal’s Api as a standalone script

## App Editor
TBD: Finish app editor: OpenAPI
