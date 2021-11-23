# App development exercises 
App development is hard to get into, but easy once you understand it.

## Introduction

## Python apps 
1. **App setup:** Make an app with the name "Shuffle Learning", and add a custom image to it, then load it into Shuffle
2. **Add an action:** Make an action with the name "hello world", which returns "Hello world"
3. **Using parameters:** Add a new function called "say hi", which takes ONE input parameter, name, and returns "Hi, {name}"
4. **Using option parameters:** Add a new function called "true or false" which takes two options and compares them. Name the parameters "option1" and "option2", and make them use the "options" parameter operator, with the "true and false" values.
5. **Using KV store:** Make a function which sets the current time in the cache/KV store based on a key. Make another action for GETTING a value from the KV store. [See utility functions](https://shuffler.io/docs/app_creation#utility-functions)
6. **Using Files:** Make a function which downloads a malware test file from [eicar.org](https://eicar.com), and uploads it to Shuffle. Make another function which gets the file from shuffle and shows you the value of it.
7. **Custom operations:** Build an app which can run nmap - either from python directly, or as a subprocess in the container. e.g. run it with this input: "nmap 192.168.0.0/24 -T5". This MAY require you to update the Dockerfile.
8. **Publishing:** Make a pull request on the [python-apps](https://github.com/Shuffle/python-apps) repository with your app. Make sure it's "production ready": 
	- Has a README
	- api.yaml mentions YOU as the contact and creator.
	- Has appropriate tags and categories

## OpenAPI / App Creator

## General 
1. Use the **$shuffle_cache** function
2. Use Liquid formatting to get the current timestamp 
