import time
def fun(n):
    return [str(num) for num in range(n)]
def fun2(n):
    return list(map(str,range(n)))
start = time.time()
result = fun2(10000)
end = time.time()
elapsed = end - start
print(elapsed)