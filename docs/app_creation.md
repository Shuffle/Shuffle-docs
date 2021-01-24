# Apps
Documentation for app creation. 

**PS: This is not finished, but is based on [WALKOFF](https://walkoff.readthedocs.io/en/master/apps.html). We will document it before 1.0 launch.**

# Table of contents
* [Introduction](#introduction)
* [Manual creation (python3.7)](#manual)
* [Development Instructions](#development_instructions)
* [App editor](#app_editor)

## Introduction
Apps are how you complete work in Shuffle. At a high level, you define a Workflow that starts based on a schedule, or some expected event (webhook received, etc), and that in turn runs one or more apps. An app takes input (argument data to act on, credentials, etc), uses that to complete some data, and returns resulting data to Shuffle to store, display, or feed into another app for further processsing.

The underlying design of Apps in Shuffle are based on [WALKOFF](https://walkoff.readthedocs.io/en/master/apps.html) with minor differences. Most of the documentation below will therefore be close to their approach.

[More about apps](/docs/apps)

The premise behind all apps that run in Shuffle, is that they each run in an isolated Docker container, for security purposes. When you provide arguments to an app in a Shuffle workflow, when the workflow is run, and your app is reached, it is launched as a new container, given the argument data, and the container destroyed when completed.

## Why create a custom app?
There are many prebuilt apps in Shuffle, and all complete some action. There may an integration you need that doesn't exist yet. This guide will walk you through the process.
Always remember the key components of the app:
	What functions are available in the app?
	What arguments are needed for the app to function? - e.g. authentication arguments, json data structure arguments.
	What is the output of this function, and what are we doing with that resulting data? e.g. send an email, create a ticket, send to another app for conditional processing.
	
	

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
	+-- another_app_1 
	+-- another_app_2
```

### Development Instructions
These instructions will indicate how to make an app for Virustotal and make it available in Shuffle. We recommend building them following our step by step instructions. 

1. Setup

Start by developing your app and its functions in a standalone script outside of WALKOFF – this way you can get basic functionality down before dealing with WALKOFF.

Note: all functions that you expect to turn into actions must be written for asyncio (i.e. async def function_name())

EXAMPLE: Below is example code that can be used to interact with VirusTotal’s Api as a standalone script

## App Editor
TBD: Finish app editor: OpenAPI
