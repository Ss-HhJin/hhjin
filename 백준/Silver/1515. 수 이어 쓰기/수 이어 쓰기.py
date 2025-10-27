s = input().strip()
sarr = list(s)
idx = 0
n = 0

while idx < len(sarr):
    n += 1
    num = str(n)
    for i in num:
        if idx < len(sarr) and i == sarr[idx]:
            idx += 1

print(n)
