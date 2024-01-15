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
- [] Is the queue held up, or is it at 0 (/admin?tab=environments)?
- [] Are all apps you want to work, working (actions missing, weird auth...)?
- [] Conditions: Do every workflow have good conditions to cover edgecases? (e.g. authorization timeouts leading to 403s)
- [] Backups: Do you have a backup git repository set up for Workflow revisions?
- [] Authentication: Are you using Authentication Storage instead of cleartext Auth?

## Architecture
Architecture auditing is here to ensure you can achieve high availability and have good disaster recovery. 

- [] Is it running on multiple servers?
- [] Is Orborus on a different server than the backend?
- [] Is vm max_map_count set on servers with Opensearch?
- [] Are there multiple instances (nodes) of Opensearch? 
- [] Do you have NFS for Opensearch to handle scaling?

## Storage & Memory
- [] Are you using distributed caching?
- [] Do you have enough memory to run your workflows efficiently? 
- [] Do you have enough storage for Opensearch?

## Security

- [] Encryption Modifier: Do you have an encryption modifier set in .env?
- [] Are ports exposed that shouldn't be? (Opensearch 9200, Backend 5001..)
- [] Are you using HTTPS instead of HTTP?
- [] Do you have an nginx reverse proxy to handle certificate management?
- 


## Scale
