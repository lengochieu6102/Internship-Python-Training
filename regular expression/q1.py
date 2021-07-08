import re

regex='^([\w\.]+)@(\w+)\.(\w+)'
def checkEmail(email):
    if re.search(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

checkEmail('anhkirai326@gmail.com')
checkEmail('my.ownsite@ourearth.org')
checkEmail('anhkirai326.com')