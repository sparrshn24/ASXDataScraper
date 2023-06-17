pip install praw
from praw.models import MoreComments
import requests
import pandas as pd
import pytz
import json
import praw
from datetime import *
from dateutil import parser
from comments import *

reddit = praw.Reddit(
    client_id="******",
    client_secret="******",
    password="*****",
    user_agent="Scraping Aus Financial Subreddits.",
    username="ThEhIGhGrEYmATTER",
)

api = PushshiftAPI(reddit)
subreddit = reddit.subreddit("ASX")

def getPostAsDict(post):
    individual_post={}
    individual_post['Subreddit'] = str(post.subreddit)
    individual_post['URL'] = str(post.url)
    individual_post['Subtext']= post.selftext
    individual_post['Title']=post.title
    individual_post['ID']=post.id
#     individual_post['Kind']=post.kind
    individual_post['Response']=getResponse(post)
    individual_post['Upvote Ratio']=post.upvote_ratio
    individual_post['Time']= datetime.fromtimestamp(post.created).strftime('%Y-%m-%dT%H:%M:%SZ')
                    
    return individual_post

def getResponse(post):
    response=[]
    submission = reddit.submission(post.id)
    submission.comments.replace_more(limit=None)
    flag=False
    for comment in submission.comments.list():
        response_str = str(comment.body)
        blocks = response_str.split("\n")
        for block in blocks:
            if(block!=''):
                response.append(block)
    return response    

date = datetime.now(timezone.utc)
req_date = utc_datetime = datetime(2018,7,31, 12, 0, 0, tzinfo = pytz.utc)
while(date>req_date):
    for submission in subreddit.new(limit=None):
        post_dict = getPostAsDict(submission)
        print(type(post_dict))
        fullname = submission.fullname
        date = datetime.strptime(post_dict['Time'],'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
        time = post_dict['Time']
        path='ASX/'+time[0:13]
        
        print(post_dict)


