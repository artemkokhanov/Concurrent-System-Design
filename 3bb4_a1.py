def d(n):
    return sum([i for i in range(1, n) if n % i == 0])

print(d(220))
print(d(284))

assert d(220) == 284
assert d(284) == 220

def a(m):
    return sum([i for i in range(1, m) if d(d(i)) == i and (d(i) != i)])

print(a(1000))

assert a(1000) == 504
