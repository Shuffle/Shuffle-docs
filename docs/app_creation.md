# Apps
Documentation for app creation. 

**PS: This is not finished, but is based on [WALKOFF](https://walkoff.readthedocs.io/en/master/apps.html). We will document it before 1.0 launch.**

# Table of contents
* [Introduction](#introduction)
* [Manual creation (python3.7)](#manual)
* [Development Instructions](#development_instructions)
* [App editor](#app_editor)

## Introduction
Apps in Shuffle are based on the same format as [WALKOFF](https://walkoff.readthedocs.io/en/master/apps.html) with minor differences. Most of the documentation below will therefore be close to their approach.

[More about apps](/docs/apps)

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
