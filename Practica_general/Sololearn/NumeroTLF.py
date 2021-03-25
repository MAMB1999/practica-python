import re
pattern = r"^[189]{1}\d{7}$"
rex = re.match(pattern,"82145277")
if bool(rex):
    print("Valid")
else:
    print("Invalid")
