import smtplib

fromaddy = 'jonathanschen@gmail.com'
toaddy = 'jonathan.chen@duke.edu'
msg = 'This is just a test, im a super hacker now'

username = 'jonathanschen'
password = 'Pingan82'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(fromaddy, toaddy, msg)
server.quit()