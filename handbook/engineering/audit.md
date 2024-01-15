# Introduction
This document outlines information related to how to audit Shuffle infrastructure. It is specifically targeted at users who have used Shuffle for a while, 
and who are looking to be in production, but may need our teams' help. It should be a "simple" checklist to see if what they are doing makes sense.

The goal with this document is to make it easy to have automation infrastructure that follows all of these criteria:
- Stable: Should work the same at all times
- Secure: The infrastructure has been locked down

## Workflows
The goal of workflow auditing is to make them work the same at all times.

[] EXECUTING: Are there any workflows runs with status EXECUTING? Fix them.
[] ABORTED: Are there any workflows runs with status ABORTED? Fix them.

- [] Notifications: Do you have outstanding notifications? Fix them.
- [] Is the queue held up, or is it at 0 (/admin?tab=environments)?
- [] Are all apps you want to work, working (actions missing, weird auth...)?
- [] Conditions: Do every workflow have good conditions to cover edgecases? (e.g. authorization timeouts leading to 403s)

## Architecture

## Storage

## Security

## Scale
