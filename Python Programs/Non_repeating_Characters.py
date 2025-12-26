s = "Automation and Python"

s = s.lower().replace(" ", "")

seen = ""

for ch in s:
    if ch not in seen:
        print(ch)
        seen = seen + ch
