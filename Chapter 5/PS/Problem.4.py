# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(s)
print(len(s))  #output: 2
# 20 = 20.0 lenght will be counted same i.e. 1