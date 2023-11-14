# Shuffle Sales
This document is made to be a practical guide to handling sales in Shuffle

## What?
With Shuffle being a rather complex automation platform, we have made continuous efforts to improve it iteratively. We practice something called "Product-led growth", meaning we are building a platform that requires less direct sales efforts, and more product development. This document will outline how to handle leads captured from our website https://shuffler.io , and not cold leads. This means we got to cover two parts:
- Shuffle as a product
- The sales process itself

**Relevant sales platforms:**
- [Google Sheets - Find new leads](https://docs.google.com/spreadsheets/d/1-nHOAtAq-5pqaSwjlAmSvG4LxoazCxZViYkf10jnPFA/edit)
- [Gmail - Send and track emails :)](https://gmail.com)
- [Drift - Support & chat](https://app.drift.com)

- [Github Organization projects - Track leads over time](https://github.com/shuffle)
- [Google Drive - Customer Storage](https://drive.google.com)
- [Docusign - contract management](https://docusign.com) 
- [Stripe - payments](https://stripe.com)

**Useful info:**
- We get 40-70 new signups to https://shuffler.io per week, and hundreds of downloads of the open source platform
- Average license cost is $15.000/year, growing towards $20.000 going into 2024
- [Licensing](https://shuffler.io/pricing) is based on how much someone uses Shuffle, split into the following:
    * shuffler.io users: How many apps they run 
    * Open Source: How many CPU cores they run Shuffle on
- Additional things to sell:
    * Training - $4999 for 2 days, 4 hours each

**With pricing being based on usage, this means two things:**
- We have a huge incentive to help our customers solve automation problems. Product-led growth is the only way.
- Our customers may hit a limit at where they can't run Shuffle anymore without a license (mainly due to SLA's)

## Sales Process
As we're just doing inbound sales, the process is rather simple. The following links from within an account may be helpful to configure their account. You can only see these if your account has support access.

<img width="985" alt="helpful sales links" src="https://github.com/Shuffle/Shuffle-docs/assets/5719530/38e8c1f8-bc38-460f-b00b-a534944c4f0f">

Here are the basic steps when we get **INBOUND messages**:
1. Customer asks for demo/POV. Show Shuffle, with the main goal to learn why and what they want to automate. If you need it; **Sample Powerpoint**
2. If necessary, give the possibility of a free POV. This is to help them initially get set up with Apps and Workflows. 
3. If they don't have one already, Create an organization for them in [Shuffle Cloud](https://shuffler.io). This is where the customer can get billing management and such done well. When inside the organization, invite the appropriate users with their Email(s). **Make sure to select the appropriate stage they are in**. By selecting "POV" or "Customer", they will have an extra license show up in the License tab! PS: Select "Open Source" + "Customer" to get them an Onprem contract.

<img width="588" alt="image" src="https://github.com/Shuffle/Shuffle-docs/assets/5719530/befa8c87-0fbb-4e45-a14e-2d6c1a77d3f2">

Make a folder for them, and prepare a contract / NDA though [Google Drive](https://drive.google.com/drive/folders/1zVvwwkbQXW3p-DJYa0GBDzFo_ZnV_I_5). They may provide their own NDA as well in certain cases. This stage can take a lot of time, especially with public companies due to compliance needs.  

5. Get them to the finish-line. This means: Help them fullfil their POV by giving access to licenses and the support they want. Set up a subscription for them through Stripe.

<div style="display=flex;">
   <img width="717" alt="image" src="https://github.com/Shuffle/Shuffle-docs/assets/5719530/560c98cc-02e8-437a-8dc8-a772f08c3711">
</div>

6. Customer Success! Check in with your customers once in a while. It is normal that onboarding for the first 1-2 months take up more support work, while anything after that is not very

## Finding Leads
Below is a step by step guide to check out leads in Shuffle, aiming to get each one down to about 5 minutes. This is not meant to be exhaustive, so use some common sense as well! Remember that the main goal is to improve Shuffle as a platform to, and not to always go for a single customer no matter what. Useful information product-wise are things like:
- Where do most people get stuck? (pages/workflows/apps etc..)
- Were they able to solve any problems themselves? (which ones..?)
- Do you see the same apps and problems over and over? 

If you notice anything related to these questions, make sure to note it down so we can fix more of it on the product side.

**Steps:**
1. Start by finding a lead in the [spreadsheet leads](https://docs.google.com/spreadsheets/d/1-nHOAtAq-5pqaSwjlAmSvG4LxoazCxZViYkf10jnPFA/edit).
    - Leads here are based on our current userbase, and is based on our own AI algorithms. 
    - Leads are updated daily, so if you can't get to them all one day, then they may change the next (which is fine)

2. Take note of whether the lead you chose has any "Support tickets" or "Drift messages". 
    - This indicates whether we have spoken with them in the past. 
    - If we have, make sure to read those messages, as context is gold when reaching out.

3. Click the lead itself, directing you to https://shuffler.io. If the links don't work for you, then you don't have access and should email [frikky@shuffler](mailto:frikky@shuffler.io) asking for access. If you have support access, you will get temporary read access to that organization.
    - Register on https://shuffler.io/register if you haven't

4. Check the following for the lead and use what you learn to decipher if they did ok or not:
    - [App Framework - Check apps in use](https://shuffler.io/welcome?tab=2)
    - [Workflows - Check what workflows they made](https://shuffler.io/workflows)
    - [App Authentication - Check which apps they actually authenticated](https://shuffler.io/admin?tab=app_authentication)

5. With this knowledge, go back to [the admin panel](https://shuffler.io/admin) and click the "Sales mail" button in the top right. This should open a ready-filled email for the customer. Make sure to use what you learned from the previous steps to modify this for relevancy. 
    - This button also tags the lead as "contacted", which will take them off future lists
    - If the button doesn't open an email, download the extension "Mailto: for Gmail" 

6. When all is filled out, hit send! :)




If you need more details, or want a walkthrough the first time, reach out to binu or frikky.
