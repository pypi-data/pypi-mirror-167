# knok_knok: Pushing Notifications Now Becomes Simple!

## What is it?

**knok_knok** is an easy-to-use python package for sending push notifications across andriod and ios devices.  
  
**Tired of looking around for solutions to send your notifications?**  
  
No more worries now, **knok_knok** does all the heavy lifting of research and bug-fixes for you. Let's get started. 

## Our Features include

  - sending push notifications for the fcm tokens provided. Be it a token for an android device or an ios device, it doesn't matter.
  - sending notifications to any number of devices at a time
  - multiple notifications on a single device getting collapsed on the notification bar.
  - sending notifications that redirects the user somewhere
  - GCM has been deprecated so if you are someone who is migrating from GCM to FCM, you can also give us a try.

## Getting Started
The source code is currently hosted on GitHub at:
https://github.com/ajaysharma132/knok-knok

Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/knok-knok).

```sh
# PyPI
pip install knok-knok
```

for sending a push notification, all you need to do is - 
 - build a data_map containing the information for your notification message
 - provide a list of fcm tokens for the devices you want to trigger a push notification

```sh
# data_map
{
    "title": "Hello",
    "body": "World !",
    "url": "https://www.google.com/"
}  
```
title - represents the title of the your notification  
body - represents the body/text/message of your notification  
url - is for the link you want the user to redirect to..  

```sh
# tokens
[
    'token1', 
    'token2',
    'token3',
]
And so on... You can provide any number of tokens
```

Now, instantiate the FCMClient providing your FCM_API_KEY as -

```sh
# FCMClient instance
from knok_knok import FCMClient
client = FCMClient(FCM_API_KEY)
```

And use the send function to send your notifications as -

```sh
# send notification
client.send(data_map, tokens)
```

**you see, it's that simple!!**