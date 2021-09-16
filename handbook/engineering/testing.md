# Testing
**PS: This is a work in progress, and is far from finished**

This document outlines our testing and CI/CD pipeline thoughts, and how it is vs. how it can and should be. 

## Introduction
As Shuffle has grown, we've added a lot of features, which in turn also introduce bugs. These are in the frontend, backend, worker, orborus, App SDK, apps themselves, workflows and more. Shuffle is growing increasingly complex, which means we need a way to stablize between versions. This is where CI/CD and a SDLC (of sorts) comes into play. This document intends to outline each of the areas mentioned above, and how we are vs. how we would ideally like to handle them.

## What do we want?
1. (2021 Q2-Q3) We want to end up in a place where we don't have random issues that breaks Shuffle for our users. E.g. when an app is uploaded to Github, we should make sure it works, and doesn't have simple coding or formatting errors. We want them to work, and be easily sharable. These apps should further upload their contents to https://shuffler.io, as this is where people find whether we have an integration or not.
2. (2021 Q4) We want to validate each API-call for Shuffle. Does it have any errors?
3. (2022 Q1) We want to validate each Workflow 
4. (2022 Q2) We want to validate each App action

## Bugs and features
As we build Shuffle, features that are created in the frontend can make an app break. This has to do with how data is used and transformed, among other things. Here's the overarching structure of Shuffle:

Frontend -> Backend -> Orborus (workflow execution) -> Worker -> App SDK -> User-made app

This means that when you execute a single workflow, it goes through at least 6 layers that can potentially break. The question quickly becomes "How can we handle this?". Especially when data is user-generated. How? We'll start bottom-up. 

This means starting with a user-made App that's uploaded to Github in one of our public repositories; [Python](https://github.com/frikky/shuffle-apps) and [OpenAPI](https://github.com/frikky/security-openapis). 

## How?
As we're hosting everything on Github, it would be natural to use Github actions. This has the possibility of tracking our progress as we make new updates, and we can make our own scripts to validate everything. As of this writing (Mar. 17. 2021) we only have a single workflow for [uploading new apps to Dockerhub](https://github.com/frikky/Shuffle-apps/blob/master/.github/workflows/ci.yaml).

So how do we test if the new functionality actually works? We need to do a few things, all leading to Workflows and testing them:
* Creating Workflows that validate if App SDK works  
* Create simple test-cases for each app.  

### Apps - OpenAPI
OpenAPI apps are defined [here](https://github.com/frikky/security-openapis) and are YAML or JSON files that are loaded into Shuffle the first time it's started. We currently run [this](https://github.com/frikky/security-openapis/blob/master/upload.py) script manually to upload them. The issue is that they're uploaded without any real validation.

Here's the basic CI/CD for this: 
1. Create a workflow that loops through the NEW or EDITED files in the folder. Validate the OpenAPI or JSON-Schema in some basic way. 
2. Add workflow secrets for https://shuffler.io API to the github folder
3. Use the upload.py script (or similar) to upload the file(s). The Shuffle backend handles distribution.

### Apps - Python
Python based Shuffle apps use a format based on WALKOFF, which has a certain folder structure. The full system for this is a bit more complicated however, as it involves actually reading and validating the data BEFORE uploading. This is currently done using a script called [stitcher.go](https://github.com/frikky/shuffle-shared/blob/main/app_upload/stitcher.go) which loops through the folder and builds out the full structure.

Why is it done this way? Because that's what the Open Source backend of Shuffle does as well, and we want these functions to do the same for both open source, cloud and when running it manually. Now.. how do you use it manually?
1. Open the file and use the first lines of the script to configure it. The important parts: The endpoint to use (https://shuffler.io), your API-key and the folder where the apps are located.
2. Run the file. It should now start uploading all the folders and files one by one, including all versions of them.

Now, how do we translate this into a CI/CD pipeline? That's exactly what we need to figure out..

### Workflow execution (Orborus, Workers & App SDK)
TBD: Have multiple complex workflows ran automatically in a test build for every new version of Shuffle. These should test e.g. newly built apps, app sdk functionality like conditions and JSON parsing, Liquid formatting, loops and more.

### App SDK 
TBD: There are different versions with different operating systems. Should probably move it to it's own repo.

### Backend 
TBD: Run a test for whether API's return data as expected in a test environment.

### Frontend
TBD: Run tests for whether each view and component works, and can reach out to the backend properly. 
