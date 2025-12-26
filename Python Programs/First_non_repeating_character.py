s = "swiss"
seen = ""
a = {}

for ch in s:
    if ch not in seen:
        seen = seen + ch
        a[ch] = 1
    else:
        a[ch] += 1

for ch in s:
    if a[ch] == 1:
        print(ch)
        break
