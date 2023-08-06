# Send e-mail example

from net import Mail

# Set parameters
username = 'xxxxxxx@host.com'  # username to login SMTP server
password = 'xxxxxxxxxx'      # password to login SMTP server
receiver = 'xxxxxxxx@host.com'  # receiver e-mail address

mail = Mail(username, password)  # Create mail object

# Send mail with attachment file '1.jpg'
mail.send([receiver], 'My Subject', "This is body", ['1.jpg'])
