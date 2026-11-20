class User:
    def __init__(self):
        pass

    def get_user_id(self):
        pass

def get_user_data():
    pass



import time

n = 1_000_000_000

# 1) sum(range)
start = time.perf_counter()
s = sum(range(1, n + 1))
t = (time.perf_counter() - start) * 1000
print(f"sum(range): natija = {s}, vaqt = {t:.4f} ms")

# 2) for sikl
start = time.perf_counter()
s = 0
for i in range(1, n + 1):
    s += i
t = (time.perf_counter() - start) * 1000
print(f"for sikl:   natija = {s}, vaqt = {t:.4f} ms")

# 3) Formula
start = time.perf_counter()
f = n * (n + 1) // 2
t = (time.perf_counter() - start) * 1000
print(f"Formula:    natija = {f}, vaqt = {t:.6f} ms")
