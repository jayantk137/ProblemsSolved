n =int(input())
s = input()
li = dict()
k = []
max =1
for i in range(n-2):
    if s[i:i+2] in li:
        li[s[i:i+2]] += 1
        if li[s[i:i+2]] > max :
            max = li[s[i:i+2]]
    else:
        li[s[i:i+2]] = 1

for key,value in li.items():
    if value >= max :
        k.append(key)
k.sort()

print(k[0])
