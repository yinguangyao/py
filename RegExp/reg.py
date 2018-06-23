import re
s = r'ABC\-001'
print(re.match(r'^\d{3}\-\d{3, 8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3, 8}$', '010 12345'))
test = "a b c"
print(re.split(r'\s+', test))