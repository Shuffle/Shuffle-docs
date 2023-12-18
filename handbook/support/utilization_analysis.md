# Utilization Analysis
As companies get farther with Shuffle, it is important that we can get enough metrics from them to know what they are doing (to an extent). 
This document outlines a few ways to find out how a company uses Shuffle through Shuffle itself.

If we don't have metrics on something which could be useful (e.g. tracking of usage per app/workflow), then tell our development team what may be missing.

## Intro
Using Shuffle onprem vs Cloud shouldn't matter here. They record mostly the same things, but the details of what is important may vary.

Examples:
- Onprem/Hybrid: CPU/Memory utilization may be just as important as Workflow Runs to understand what happened
- Cloud: They may care more about App Runs, as that is our cost metric

## Important datapoints
To understand how someone uses Shuffle, it's important to understand the baseline they have built upon. The following becomes important:

- What Usecases they have built (what do the workflows do?)
- Their apps that are in use
- Notifications - how many? The more they have, the more indicates they have done something
- Utilization of Shuffle (`/admin?admin_tab=billing`). How many executions? What apps / workflows ran most?
- **Onprem/Hybrid**: CPU & Memory utilization on Orborus (`/admin?tab=environments`)
- Using the Workflow Run Debugger to find problems in some specific time (`/workflows/debug`)

Make sure to check out multi-tenancy

### Finding their usecases
TBD

### Finding their apps
TBD

### Exploring Notifications
TBD

### Utilization of Shuffle
TBD

### CPU/Memoyr analysis
TBD

### Using the Workflow Run Debugger
TBD
