# Debugging
Debugging is a big part of making Shuffle work well everywhere, especially at scale. Herein we will talk a little bit more about it, and have samples for how to fix it.

## executions
execution debugging comes in many forms. Most of the time it's either of these:
1. A connection/network issue
2. App deployment issue
3. Authentication issue
4. Authorization issue

And problems for each of these can arise in each of these steps:
- Backend -> Orborus -> Worker -> App

For each of these, there are multiple ways to dig into them. Here's a few:

### Connection or network issue
As the image below shows, it says "Connection Refused". Here's what you do:
1. Check connectivity between Orborus & the backend
2. ...

![image](https://user-images.githubusercontent.com/5719530/185935832-ec11dfc8-282c-467f-b306-4c65913465c7.png)
