#!/usr/bin/env python
import os
os.environ["MKL_THREADING_LAYER"] = "GNU"

with open('cat0_text.txt', 'r') as cat0_text:
        cat0_summ=cat0_text.read()
with open('cat1_text.txt', 'r') as cat1_text:
        cat1_summ=cat1_text.read()
#with open('cat2_text.txt', 'r') as cat2_text:
#       cat2_summ=cat2_text.read()
#net_text=[cat0_summ, cat1_summ,cat2_summ]
net_text=[cat0_summ, cat1_summ]
from abstractive_summarization import summarize
summaries = summarize(net_text)
for j in [0,1]:
        summaries[j]=''.join([i for i in summaries[j] if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='1' and i<='9') or(i==' ' or i=='.' or i=='!' or i==':' or i=='-' or i=='\n' or i=='0' or i==',' or i=='$' or i=='?' or i=='/')])

with open('end_summary.txt', 'w') as f:
        for item in summaries:
                f.write("%s. " % item)

with open('end_summary.txt', 'r') as f:
        summ_str=f.read()

tweet_summs=[]
i=0
j=280
switch=0
print(len(summ_str))

while (switch==0):
        j=i+280
        if (j >= len(summ_str)):
                j=len(summ_str)-1
                tweet_summs.append(summ_str[i:j])
                switch=1
#               print(summ_str[i:j])
        elif (summ_str[j]=='.'):
                tweet_summs.append(summ_str[i:j])
#               print(summ_str[i:j])
                i=j+1
        else:
                while (summ_str[j] != '.'):
                        j=j-1
                tweet_summs.append(summ_str[i:j])
#               print(summ_str[i:j])
                i=j+1

print(tweet_summs)

from push_tweet import *

for tweet in tweet_summs:
        push_tweet(tweet)
'''
from flask import Flask
from flask_mail import Mail, Message

app= Flask(__name__)

mail_settings = {
        "MAIL_SERVER" : 'smtp.gmail.com',
        "MAIL_USE_TLS" : False,
        "MAIL_USE_SSL" : True,
        "MAIL_PORT" : 465,
        "MAIL_USERNAME" : 'enter sender's mail id here',
        "MAIL_PASSWORD" : 'enter sender's mail password here'
}

app.config.update(mail_settings)
mail=Mail(app)

if __name__== '__main__':
        with app.app_context():
                msg = Message(sender=app.config.get("MAIL_USERNAME"), recipients=["enter recipient1's email id", "enter recipient2's email id", "... etc"])
                       
                msg.subject = "Earthquake Tweet Summary"
                msg.body = summ_str     

                mail.send(msg)

'''
	

