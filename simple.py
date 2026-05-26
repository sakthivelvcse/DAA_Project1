import time

def function(txt, pat, m, n):
    # search for pattern in txt; only valid start positions
    for i in range(m - n + 1):
        if txt[i:i+n] == pat:
            return i
    return -1


txt = input("Enter a text : ")
pat = input("Enter a pattern : ")
stime = time.time()
time.sleep(1)
print(function(txt, pat, len(txt), len(pat)))
etime = time.time()
print(etime - stime - 1)

