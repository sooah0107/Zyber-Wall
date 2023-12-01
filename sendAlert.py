import pickle
from twilio.rest import Client
from getResp import driver

sender="+19289388580"

receiver=""
with open("receiver.pkl","rb") as f:
    receiver=pickle.load(f)

account_sid = 'ACf825c74ad8822f62310461e580133e4f'
auth_token = 'e5433654b951cb9ae16a6303966ee106'

client = Client(account_sid, auth_token)
resp=""
def send(vLink):
    #print("King2---------------")
    global resp
    client.messages.create(from_=sender,to=receiver,body='Your child device wants to access '+vLink+"\nPlease reply 1 or 0 :\n1 : Allow\n0 : Block")
    
    resp=driver()
    return resp
