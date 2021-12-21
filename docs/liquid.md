# Liquid 
Documentation for using [Liquid formatting](https://shopify.github.io/liquid/) inside Shuffle, along with examples

**PS: This document will be heavily changed in the start of 2022.**

## Table of contents
* [Introduction](#introduction)
* [Usage and Issues](#usage_and_issues)

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

