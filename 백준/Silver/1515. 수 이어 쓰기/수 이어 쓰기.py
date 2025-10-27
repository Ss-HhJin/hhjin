s = input().strip()
sarr = list(s)
idx = 0
N = 0

while idx < len(sarr):
    N += 1
    num = str(N)
    for ch in num:
        if idx < len(sarr) and ch == sarr[idx]:
            idx += 1

print(N)
