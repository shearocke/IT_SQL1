import smtplib  #standard mail network protocol

email = 'goodshepherdiot@gmail.com' # your email
password = 'P@ssword#1' # your email password
send_to_email = 'rockeshea72@gmail.com' # who we are sending the message to
message = 'yay it worked!'  # the message in the email

server = smtplib.SMTP('smtp.gmail.com', 587) #connect to the server
server.starttls() #use TLS(Transport Layer Security)
