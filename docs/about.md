# About Shuffle
Shuffle started as a project in mid-2019 because of a few automation related problems that needed more attention in the [CERT/SIRT](https://en.wikipedia.org/wiki/Computer_emergency_response_team) community. Available automation solutions in the security industry are trying to do everything at once; handle tickets, indicators, threat intel and much more in a single platform, while our goal is to build the best solution to fit all your existing tools following the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well): "Do One Thing and Do It Well". 


## Mission
To make every security operations center share their processes, automations and detections in a standardized way. Cybersecurity is not a competiton between companies, and shouldn't treated as such.

## Open Source
Focus for Shuffle has moved to an entirely open ecosystem. This includes, but is not limited to; the Shuffle product, open workflows, open apps, open standards (OpenAPI, Swagger).

## Roadmap
This roadmap is meant more as a guide than as the exact order of operations. It's mainly focused on the Open Source side of Shuffle, but also focuses on the creator and growth aspects of Shuffle.

- [Slides for 2022-2023](https://docs.google.com/presentation/d/1eqfeYOgfGV8srb_0Cox4ZDK_KuykiwB8LpxHHrTgw5o/edit?usp=sharing)

* 0.1 - 0.5: Created basic features for automation, as well as use cases and frontend. This was before the project was open sourced.
* 0.6 - Usability: High focus on the workflow and app editor, as well as bugfixing after open sourcing. 
* 0.7 - Improve: First larger release of Shuffle. Focus on users, schedules, app authentication and a better overview in general through the admin view.
* 0.8 - Integrate (current): Hybrid cloud features and file control 
* 0.9 - Features: Search engine for apps, workflows, executions etc. GCP (Storage & Functions) integration usage for cloud.
* 1.0 - Launch: Categorized apps, proper use-cases, and a real tutorial mapped to use-cases. Enterprise-ready (SSO/SAML, MFA, Reporting, Statistics, Replayability)
* **1.1 - [Creator onboarding](https://github.com/Shuffle/Shuffle/releases/tag/1.1.0):** Workflow, App & Usecase discovery. Stability & Scalability everywhere with multi-region deployments. HUGE focus on on-boarding and workflow templates. Expected release Q4 2022.
* 1.2 - Usability: Autocompletes, Suggestion engines, Dashboards, Auditing. Lambda & EKS integrations. Partnerships with top 5 relevant tools in each [App Category](https://shuffler.io/welcome?tab=2). Threat Intel management with Shuffle Datastore. Expected release Q2 2023. 
* 1.3 - **Current release** Scale support, workflow statistics, stabilization and tracking.  Expected release Q4 2023.
* 1.4 - **In development:** Realtime Workflow Collaboration (+support workflow support cloud->onprem), Workflow Generation based on text, MSSP Tenant & Workflow Management, Dynamic Authentication, Vaults, Improved Coding Editor with Code Generator & Shuffle Functions, Improved Trigger management and branding, Hybrid Workflow Access. Expected release Q2 2024. 
* 1.5 - Detection & Standardization: **Schemaless**, Creator Earnings, Mitre Att&ck, Yara, Sigma, Ansible, OSQuery, Sublime emails. OASIS OpenC2 & CACAO fully working. Support for JSON-schema & Postman Collections. Expected release Q4 2024.
    
## Blogposts
* [Introducing Shuffle](https://medium.com/security-operation-capybara/introducing-shuffle-an-open-source-soar-platform-part-1-58a529de7d12)
* [Getting started with Shuffle](https://medium.com/@Frikkylikeme/getting-started-with-shuffle-an-open-source-soar-platform-part-2-1d7c67a64244)

## Problems Shuffle solves 
These included, but were not limited to (no specific order):
* [Alert fatigue](https://en.wikipedia.org/wiki/Alarm_fatigue) by giving analysts the tools to automate most alerts
* Remove menial tasks, decreasing employee turnover
* Quick integrations with new tools - OpenAPI
* Giving you a clear overview of your environment by tracking integration usage

Regards,

Fredrik Ødegårdstuen - [@frikkylikeme](https://twitter.com/Frikkylikeme) - [frikky@shuffler.io](mailto:frikky@shuffler.io)
