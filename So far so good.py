s = input()
s = s.split(" ")
s = "".join(s)
r = {}
o = [] #open
c = [] #closed
cur = [] #closed_left_ from_open
for i in range(len(s)):
    if s[i] == "(":
        o.append(i)
    if s[i] == ")":
        c.append(i)
op = max(o) #current_open_index
for i in range(len(c)):
    if c[i] > o[op - 1]:
        cur.append(i)
cl = min(cur) #current_closed
n1 = "" #first_number
n2 = "" #second_number
i = op + 1
while s[i] in "123456789" and i <= cl:
    n1 += s[i]
    i += 1
print(op, cl, n1, n2)
