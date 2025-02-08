#!pip install facebook-sdk
import facebook as fb

# Get Access token - Follow the video on how to get access token for your fb account
access_token = "yourAPI"

# The Graph API allows you to read and write data to and from the Facebook social graph
asafb = fb.GraphAPI(access_token)

# Post a message in the facebook page
asafb.put_object("me","feed",message = "This is automated post!")



