#!/usr/bin/env python
###########################################
########## Reading email content ##########
######## Author Name: Pavel Sur ###########
###########################################

import poplib
from email import *
from email.parser import Parser
import imaplib
import traceback
import sys

mailServer = 'mail.rebaca.com'
mailId = 'pavel.sur@rebaca.com'
mailPw = 'taXc0d3r!'
desiredText = "My test"

mail = poplib.POP3(mailServer)
print mail.getwelcome()
mail.user(mailId)
mail.pass_(mailPw)
mailInformation = mail.stat()
print "mail stat", mailInformation

#setInformation = mail.list(True)
#print "setInformation", setInformation

numberOfEmail = mailInformation[0]
print "numberOfEmail", numberOfEmail

numOfMessage = len(mail.list()[1])
print "numOfMessage", numOfMessage
 
print "******************************************"

for i in range(numberOfEmail, 0, -1):
	print i

	try:

		(server_msg, body, octets) = mail .retr(i + 1)
		#print "######################################"
		#print body
		#print "######################################"
		mailLine = message_from_string("\n".join(body))
		#process_mail(mailLine)
		print "######################################"
		print mailLine['Subject']
		print "######################################"

		if mailLine['Subject'] == desiredText:
			print "*******************************************"
			print mailLine['From']
			print mailLine['Date']
			print mailLine.get_payload()[ 0 ].get_payload()
			print "*******************************************"
			break

	except:
		print "======================================="
        #__printException(e)
        print str(sys.exc_info()[1])
        print "======================================="
        continue	
     

mail.quit()
