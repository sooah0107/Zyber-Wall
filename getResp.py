from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
#from flask_ngrok import run_with_ngrok
import os
from threading import Thread

app = Flask(__name__)
#run_with_ngrok(app)
message_body=""
#os.system("ngrok http 5000")

@app.route('/sms', methods=['POST','GET'])
def sms():
    print("sms function started")
    global message_body
    message_body = request.form['Body']
    #print(message_body)
    resp = MessagingResponse()
    resp.message("We got your Response")
    #print("\n\nthis is the message recived\n"+str(message_body)+"\n\n")'''
    return str(resp)

@app.route('/test', methods=['POST','GET'])
def test():
    print("Testing Function")
    return("<p>Testing</p>")

def ngrokStart():
    os.system("start cmd /k ngrok http 5000")
    return

def flaskStart():
    app.run()
    return message_body
def driver():
    Thread(target = flaskStart).start()
    Thread(target = ngrokStart).start()
driver()
