# Deployment
Deploying a new region takes a lot of effort the first time. We've identifier all the stages related to it which will be outlined in this document. 
The image below outlines most of our single-location architecture in cloud, and will be expanded to handle multi-region entirely in 2022. 

![shuffle_architecture](https://user-images.githubusercontent.com/5719530/194397142-917366f3-8cb5-4524-b074-b581d0525f34.png)

## Cloud
As of October 2022, our entire infrastructure is on Google Cloud Platform.

## Tools
The following tools is our entire stack. The basics works with just the top three, with the rest being usecase specific & for analytics

- AppEngine: Backend & Frontend
- Cloud Functions: Apps & scripts
- Cloud Datastore: Database

- Cloud Run: SSR & Apps
- PubSub: Specific pub/sub-only tasks
- Cloud Tasks: Scheduling tasks
- Cloud Scheduler: Cronjobs & Workflow Schedules
- Cloud Memorystore: Caching
- Cloud Storage: Blob storage
- BigQuery: Extra data analysis
- Error Reporting: Handle incoming errors
- Cloud Logging: Handle Logs
- Cloud Metrics: Create metrics and alerts based on logs

## Process
The process to deploy a new region will be available below

TBD

## Testing
It's important to test the new region. Here's how you can do it and make sure we have both initial manual tests for the region,
as well as continuous deployment of new updates from testing and staging to production.

TBD
