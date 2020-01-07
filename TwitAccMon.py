from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import path
import requests
import smtplib
import datetime
import re

def send_notification(user,action):	
	date = datetime.datetime.now()
	fixed_date = date.strftime("%m-%d-%Y %I:%M %p")

	from_email = '' #Your Email
	to_email = '' #Your Email
	email_user = '' #Your Email
	email_pass = '' #Your Email Password
	smtp_server = '' #Your SMTP Server Ex: smtp.gmail.com
	smtp_port = '' #Your SMTP port

	fromaddr = '{0}'.format(from_email)
	toaddr = '{0}'.format(to_email)

	msg = MIMEMultipart()

	msg['from'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = 'The Twitter Account: {0} Has Been: {1}'.format(user,action)

	body = ('Date/Time Found/Removed Online: {0}'.format(fixed_date) + '\n'
			'Action: {0}'.format(action) + '\n'
			'Account: {0}'.format(user) + '\n'
			'Link: https://twitter.com/{0}'.format(user) + '\n'
	        )

	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('{0}'.format(smtp_server), '{0}'.format(smtp_port))
	server.starttls()
	server.login(email_user, email_pass)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

"""So a user can't be in both lists at the same time"""
def list_health_check(user,check_list):
	if check_list == 'live':
		with open('account_is_live.txt', 'r+') as f:
			live_list = f.read().splitlines()
			if user in live_list:
				live_list.remove(user)
				join_list = '\n'.join(live_list)
				with open('account_is_live.txt', 'w') as f:
					f.write(join_list)
					f.close()
	elif check_list == 'dead':
		with open('account_is_not_live.txt', 'r+') as f:
			dead_list = f.read().splitlines()
			if user in dead_list:
				dead_list.remove(user)
				join_list = '\n'.join(dead_list)
				with open('account_is_not_live.txt', 'w') as f:
					f.write(join_list)
					f.close()

def account_is_200(user):
	check_if_file_exists = path.exists('account_is_live.txt')
	if check_if_file_exists == True:
		with open('account_is_live.txt', 'r') as f:
			live_output = f.read().splitlines()
		if user in live_output:
			pass
			remove_from_list = 'dead'
			list_health_check(user,remove_from_list)
		elif user not in live_output:
			with open('account_is_live.txt', 'a') as f:
				f.write(user + '\n')
				f.close()
				action = 'Activated'
				send_notification(user,action)
				remove_from_list = 'dead'
				list_health_check(user,remove_from_list)
	elif check_if_file_exists == False:
		with open('account_is_live.txt', 'w') as f:
			f.write(user + '\n')
			f.close()
			action = 'Activated'
			send_notification(user,action)		

def account_is_404(user):
	check_if_file_exists = path.exists('account_is_not_live.txt')
	if check_if_file_exists == True:
		with open('account_is_not_live.txt', 'r') as f:
			not_live_output = f.read().splitlines()
		if user in not_live_output:
			pass
			remove_from_list = 'live'
			list_health_check(user,remove_from_list)
		elif user not in not_live_output:
			with open('account_is_not_live.txt', 'a') as f:
				f.write(user + '\n')
				f.close()
				action = 'Removed'
				send_notification(user,action)
				remove_from_list = 'live'
				list_health_check(user,remove_from_list)
	elif check_if_file_exists == False:
		with open('account_is_not_live.txt', 'w') as f:
			f.write(user + '\n')
			f.close()
			action = 'Removed'
			send_notification(user,action)

"""For Session Build"""	
request = requests.Session()

"""Edit This List"""
user_mon_list = ['infosecslut',
				'darksim905']

for user in user_mon_list:
	url = 'https://twitter.com/{0}'.format(user)
	check_if_live = request.get(url)
	if check_if_live.status_code == 200:
		account_is_200(user)
	elif check_if_live.status_code == 404:
		account_is_404(user)
