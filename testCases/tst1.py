import re
s='srikanth reddy chelukala'
rs=re.findall(r'r\w{3}',s)
print(rs)