s = "Automation and Python"
s = s.lower().replace(" ", "")

counts = {}

for ch in s:
    if ch not in counts:
        counts[ch] = 1
    else:
        counts[ch] = counts[ch] + 1

print(counts)
