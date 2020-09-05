# Apps
Documentation for apps

PS: App creation and searching is for the on-premise version.

# Table of contents
* [Introduction](#introduction)
* [How they work](#how_they_work)
* [Actions](#actions)
* [Arguments](#arguments)
* [Downloading apps](#updating_apps)
* [Updating apps](#updating_apps)
* [Searching for apps](#searching_for_apps)
* [Create OpenAPI app](#create_openapi_app)
* [Edit OpenAPI app](#edit_openapi_app)
* [Create custom app](#create_custom_app)
* [Upload custom app](#upload_custom_app)
* [Delete app](#delete_app)
* [API](#api)

## Introduction
Apps are the heavy lifters of [workflows](/docs/workflows) within Shuffle. They give access to a library of functions, and are created using OpenAPI or pure Python. Shuffle gives you access to pre-defined integrations located [here](https://github.com/frikky/shuffle-apps). 

A subset of available apps can be found at [https://shuffler.io/apps](https://shuffler.io/apps). 

![Apps view 1](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-1.png?raw=true)

## How they work
Apps are the primary building blocks in workflows. Apps can be auto-generated from [OpenAPI](https://swagger.io/specification/) specifications or using Shuffle's app sdk. To enforce stability and usability, we use a versioning system to prevent sudden updates to apps.

Apps can contain multiple actions, which can take multiple variables. They are made to be able to interact with eachother by using each-others' data. Apps have the ability to be in multiple [environment](/docs/environments) with different data (e.g. different credentials), before passing them on.

PS: In a future iteration, focus will move to an optional hybrid execution model (e.g. use cloud resources).

### Actions
An app can perform more than one task based on predefined actions. These actions are defined by the developer, and are reusable and modifyable by the user of the app. An action should (for now) be a one-to-one representation of the function to run, and usually has arguments for authentication with the target application. Actions can contain multiple arguments.

You can see what actions an app has by going to /apps, then finding the app you're looking for. 

![Apps view 2](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-2.png?raw=true)

### Arguments
Arguments are the variables used to perform an action. Arguments with an orange dot next to them are required, with yellow ones being optional. Arguments should have example text to to indicate the expected value. The first arguments of an app are _usually_ related to authentication or the target URL, where we suggest using [variables](/docs/workflows#variables)

You can see what parameters and action has by going to /apps, selecting an app and then the action.

![Apps view 3](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-3.png?raw=true)

## Updating apps 
**PS: This only applies to onprem**
Going to /apps, there exists a button called "Download from Github" which by default will download apps from the directory https://github.com/frikky/shuffle-apps. You can type in your own repository along with authentication options if applicable.

![Apps view 11](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-11.png?raw=true)

When the modal opens, there are two buttons:
* Submit - Downloads and builds NEW apps
* Force update - Downloads and builds ALL apps
* Cancel - Closes the modal with no action

## Searching for apps
When you set up Shuffle for the first time, it should provide you with 15-20 existing Apps. These are gathered from [shuffle-apps](https://github.com/frikky/shuffle-apps), and will grow over time. 

Searching for apps is done by going to /apps and writing your search term. In the example below, we searched for "TheHive", which ends in TheHive being shown. 

![Apps view 4](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-4.png?raw=true)

A goal for Shuffle is to make it possible to search outside the apps you currently have. This is an [open issue](https://github.com/frikky/Shuffle/issues/24) as of 23.05.2020, but will be worked on.

## Create OpenAPI app
[Further documentation: App Creation](/docs/app_creation)


If you have an OpenAPI config:
* Click the "Generate from OpenAPI", paste the URL or data for your OpenAPI specification, then validate, before submitting. This should show you the app creator.
...

From scratch:
* Click the "Create from scratch" button, then use the editor.

![Apps view 5](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-5.png?raw=true)

App creator:
* Add name, description, authentication, endpoint etc..
* Create Actions.
* Save.
![Apps view 6](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-6.png?raw=true)

## Edit OpenAPI app
TBD: Finish this.

If you've created an app using the editor, or uploaded an OpenAPI specification, it's changeable. Find the app you created by searching for it, then click the "Edit app" button as seen below. You can also delete it.

Required permissions (either or):
* Admin
* App owner / creator

![Apps view 7](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-7.png?raw=true)
TBD

## Create custom app 
TBD: Create for Shuffle. 

Since Shuffle is based on WALKOFF, [their guide works for app development](https://walkoff.readthedocs.io/en/latest/apps.html). 

If you end up using WALKOFF, you need to make ONE edit: 
- Change the first line to: FROM frikky/shuffle:app_sdk as base

This will make it use Shuffle's app SDK, rather than Shuffle's.

## Upload custom app 
If you have a repository (private or public) of custom apps for Shuffle (or WALKOFF), Shuffle can load all the apps by using the "Download from URL" button in the /apps view.

1. Click the "Download from URL" button
![Apps view 9](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-9.png?raw=true)

2. Fill in the github/gitlab URL, and if the repo is private, your username & password. These are used for BasicAuth when running git clone. 
![Apps view 10](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-10.png?raw=true)

3. Hit submit. If it's unsuccessful, it will throw an error, otherwise show a loading icon. This means it's working on getting your apps.

## Delete app 
PS May 2020: There is nothing stopping you from deleting an app that is used by a workflow right now. This might be destructive.

Deleting an app is done by searching for it in /apps. 

Required permissions (either or):
* Admin
* App owner / creator

![Apps view 8](https://github.com/frikky/shuffle-docs/blob/master/assets/apps-view-8.png?raw=true)

## API 
[Click here to see the App API](/docs/api#apps)
