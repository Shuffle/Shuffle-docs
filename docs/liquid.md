# Liquid 
Documentation for using [Liquid formatting](https://shopify.github.io/liquid/) inside Shuffle, along with examples

**PS: This document will be heavily changed in the start of 2022.**

## Table of contents
* [Introduction](#introduction)
* [Usage and Issues](#usage_and_issues)
* [Shuffle's Implementation of Liquid](#Shuffle's_Implementation_of_Liquid)

LiquidPy examples: https://pwwang.github.io/liquidpy/wild/

## Introduction
With the introduction of version 0.9.0 of Shuffle, we [Liquid formatting](https://shopify.github.io/liquid/) was implemented. Liquid is a templating language, allowing you to perform a lot of useful formatting operations. Common usecases involve directly writing python code or using their Liquids filters to do commong things like Regex Replace and check size. 

Shuffle uses the Python library [Liquidpy](https://github.com/pwwang/liquidpy). If you find something that should work in Liquid, but doesn't work in Shuffle, [please make an issue](https://github.com/pwwang/liquidpy/issues/new). 

## Availability
Liquid parsing is available in any field **used for execution** in Workflows, except for directly in Execution Arguments. See below.

**Works** non-exhaustive:
- App Parameters
- Conditions
- Workflow Variables
- Execution Variables

Does **NOT** work:
- Node name
- Triggers

## Usage and Issues
Liquid is available to anyone using Shuffle, with any app, in any text field belonging to that app. 

On Success:

On Failure:

## Shuffle's Implementation of Liquid
Generally in Liquid you output content using two curly braces e.g. {{ variable }} and perform logic statements by surrounding them in a curly brace percentage sign e.g. {% if statement %}.


## Example use of Liquid in a Shuffle workflow 

1. Loading up a list of IP's stored in a file uploaded to Shuffle.

https://user-images.githubusercontent.com/31187099/147345617-d9877652-161e-48f2-94d4-97c4e92e073a.png

2. The list is loaded up but the whitespace starting up the list will cause parsing problems while trying to use the list.

https://user-images.githubusercontent.com/31187099/147345630-ccd6dfcc-61a0-4c48-9fb5-f14293347fe3.png

3. So we employ the use of liquid formatting to clean up the list and then use it in our workflow, in our case its just a basic strip and everything is ready for use

https://user-images.githubusercontent.com/31187099/147345651-608e7020-6407-40c5-b959-68583d894b67.png

4. We then continue an error free session with a clean list, utilizing it in our workflow

https://user-images.githubusercontent.com/31187099/147345723-05731f54-1d1a-43b8-bfe9-79ee1a7c9c3c.png
