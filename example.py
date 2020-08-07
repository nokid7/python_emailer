#!/usr/bin/env python3
import emails

sender = 'from_email@example.com'
to = 'to_email@example.com'
subject = 'The Subject of the email goes here'
body = 'The Body of the email should go here.'
#attachment = '/tmp/processed.pdf' #optional field, add path to the file to be attached

message = emails.generate_email(sender,to,subject, body, attachment)
emails.send_email(message)