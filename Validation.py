import re

def validateemail(email):
    regexEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regexEmail, email):
        return False
    else:
        return True
def validatetemobile(mobileno):
    rule = re.compile(r'\d{10,12}')
    if re.match(rule, str(mobileno)):
        return False
    else:
        return True
