from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_wtf import Form
from wtforms.validators import InputRequired
from wtforms import StringField, PasswordField
import os
import BeautifulSoup
from googlevoice import Voice
from googlevoice.util import input
import base64
key = 'abcdefghijklmnopqrstuvwxyz'
key2 = '123456789'
def encrypt(n, plaintext):
	"""Encrypt the string and return the ciphertext"""
	result = ''

	for l in plaintext.lower():
		try:
			i = (key.index(l) + n) % 26
			result += key[i]
		except ValueError:
			result += l

	return result.lower()

def decrypt(n, ciphertext):
	"""Decrypt the string and return the plaintext"""
	result = ''

	for l in ciphertext:
		try:
			i = (key.index(l) - n) % 26
			result += key[i]
		except ValueError:
			result += l

	return result
#from enc import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jackgod'

#class Encryption(Form):
#	encode = StringField('encode', validators=[InputRequired()])
#	decode = StringField('decode', validators=[InputRequired()])











































	





from googlevoice import Voice
from googlevoice.util import input
from psk2 import passwd
from psk2 import Email

	
	
#@app.route('/SMS', methods=['GET','POST'])
#def sms():
#	if request.method == 'POST':
#		text = request.form['text']
#		number = request.form['number']
#		print number
#		return render_template ('sms_show.html', number=number,text=text)
#	return render_template('sms.html')
	
	
	
@app.route('/sms', methods=['GET','POST'])
def SMS():
	#form = Encryption()
	#offset = 5
	if request.method == 'POST':
		text = request.form['text']
		text2 = request.form['number']
		voice = Voice()
		voice.login(Email,passwd)
	
		phoneNumber = text2
		text = text
		print phoneNumber
		print text
		voice.send_sms(phoneNumber, text)
	return render_template('sms.html')
	
	
@app.route('/', methods=['GET','POST'])
def index():
	#form = Encryption()
	offset = 5
	if request.method == 'POST':
		text = request.form['encode']
		text2 = request.form['decode']
		encode3 = base64.b64encode(encrypt(offset, text))
		decode2 = base64.b64decode(text2)
		decode3 = decrypt(offset, decode2)
		return render_template ('encode.html', encode3=encode3,decode3=decode3)
		#return render_template ('decode.html', decode3=decode3)
	return render_template('index.html')
	


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if __name__ == '__main__':
    app.run(host='192.168.1.238',port=5000, debug=False)