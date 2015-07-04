# What is this?

A program that can be run on a regular schedule (ex: cronjob), and sends
notifications to a pushbullet channel when new offers are posted to the
kickfurther site.

# Usage:

1. Set the following enviroment variables:
a. FB_SUB = The firebase subdomain to store state in
b. PB_KEY = The pushbullet api key to use
c. PB_CHAN = The pushbullet channel to post to (the tag name). This must have been created under your account.
2. Run the following: ```python kicknotify/run.py```
