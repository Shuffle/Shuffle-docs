# Introduction
This document outlines information related to how to audit Shuffle infrastructure. It is specifically targeted at users who have used Shuffle for a while, 
and who are looking to be in production, but may need our teams' help. It should be a "simple" checklist to see if what they are doing makes sense.

The goal with this document is to make it easy to have automation infrastructure that follows all of these criteria:
- Stable: Should work the same at all times
- Secure: The infrastructure has been locked down

This is NOT a yes/no checklist, but is meant to inform you of potentially important measures to take on your Shuffle infrastructure. 

## Workflows
The goal of workflow auditing is to make them work the same at all times.

- [] EXECUTING: Are there any workflows runs with status EXECUTING? Fix them. (/workflows/debug)
- [] ABORTED: Are there any workflows runs with status ABORTED? Fix them. (/workflows/debug)
- [] Notifications: Do you have outstanding notifications? Fix them. (/admin?admin_tab=priorities)
- [] Unused Workflows: Are Webhooks or Schedules running with data for non-important workflows?
- [] Is the queue held up, or is it at 0 (/admin?tab=environments)?
- [] Are all apps you want to work, working (actions missing, weird auth...)?
- [] Conditions: Do every workflow have good conditions to cover edgecases? (e.g. authorization timeouts leading to 403s)
- [] Backups: Do you have a backup git repository set up for Workflow revisions?
- [] Authentication: Are you using Authentication Storage instead of cleartext Auth?
- [] Cache: Are you using Cache extensively? If cache keys go above 1Mb the workflow may start slowing down or stop due to network congestion.
- [] Files: Are you using Files in your workflows? If the files are more than 20Mb, we suggest mounting them in rather than the API.

## Architecture
Architecture auditing is here to ensure you can achieve high availability and have good disaster recovery. 

- [] Is it running on one, or multiple servers (failover)?
- [] Is Orborus on a different server than the backend?
- [] Is vm max_map_count set on servers with Opensearch?
- [] Have you disabled Swap on servers with Opensearch?
- [] Are there multiple instances (nodes) of Opensearch? 
- [] Do you have NFS for Opensearch to handle scaling?
- [] Do you have Log forwarding enabled?
- [] Do you have detections in the Log forwarding for [ERROR]?  

## Storage & Memory
Storage and Memory management is always difficult, as we don't know how much is required until workflows have ran for a while.

- [] Do you have enough storage available? We recommend >500Gb of storage when scaling, as to not have random crashes due to full disk.
- [] Is enough memory assigned to Opensearch instance(s) for indexing? It should have about half the memory of the server assigned. 
- [] Are you using distributed caching and is it assigned to Backend(s) and Orborus(s)? (memcached in docker-compose.yml file)
- [] Do you have a [workflow retention manager workflow](https://shuffler.io/workflows/a621b818-3fea-49f2-83e2-814edda48770?queryID=9174110e354921cc133a6d203fb587e5)?
- [] Are you checking the indexes of Opensearch if they make sense? `curl -k http://localhost:9200/_cat/indices?v`
- [] Do you have too many files on disk in the `shuffle-files` repository? 

## Security
There are a lot of areas related to security in any platform. For Shuffle, it is important to both audit the user side, and the infrastructure side.

- [] Encryption Modifier: Do you have an encryption modifier set in .env?
- [] Did you change the Username and Password, or change to certificate auth for Opensearch? 
- [] Are ports exposed that shouldn't be outside of debugging? (Opensearch 9200, Backend 5001, Frontend HTTP 3001)
- [] Are you using HTTP (port 5001/3001) instead of HTTPS (port 3443)?
- [] Do you have an nginx reverse proxy for local certificate management?
- [] Does the server have internet? [It may not be necessary](https://shuffler.io/docs/configuration#Domain%20Whitelisting).
- [] Are [proxy configurations](https://shuffler.io/docs/configuration#Internal%20vs%20External%20proxy) set up appropriately (if necessary)?
- [] Are you using MFA for all users?
- [] Are you using SSO for sign-on? 
- [] Are your webhooks locked down with authentication headers?
- [] Are you exposing Webhooks through shuffler.io (cloud) instead of your local instance (hybrid mode)?
- [] Are you using the [latest version of Shuffle](https://github.com/Shuffle/Shuffle/releases)? We continuously fix security flaws, both on the workflow and user side.

## Scale
Scaling Shuffle can be a difficult on your own without a checklist. These configurations are mostly on the Orborus side, and will help make things more managable according to your infrastructure.

- [] Do you have any outstanding workers not finishing and closing down? This indicates workflows not finalizing properly.
- [] Do you have enough CPU/Memory to run what you want to run without any problems?
- [] Is the `CLEANUP` or `SHUFFLE_CONTAINER_AUTO_CLEANUP` environment set to true? This cleans up containers on the fly.
- [] Are Logs disabled for apps? Logging and sending logs makes workflows slower. Disable with `SHUFFLE_LOGS_DISABLED=true`
- [] Have you changed the max concurrent workflows that can run? Default is 7. `SHUFFLE_ORBORUS_EXECUTION_CONCURRENCY=5`
- [] Is the health API working? Check `/api/v1/health` and `/api/v1/health/stats`
- [] Environment stats: Have you disabled these at scale? `SHUFFLE_STATS_DISABLED=true`
- [] Are you running in Swarm/K8s instead of the default setup? 
- [] Are Reruns and Aborts running as expected? Check Workflow run debugger (/workflows/debug) for old workflow runs in EXECUTING or ABORTED mode. If they are NOT aborted but instead EXECUTING, then this is not working as expected.
- [] Are you surpassing 500.000 App runs in a month? At this point, [it gets hard to scale on your own](https://shuffler.io/pricing?tab=onprem).

Got any other potential bottlenecks? [Contact us](https://shuffler.io/contact)
