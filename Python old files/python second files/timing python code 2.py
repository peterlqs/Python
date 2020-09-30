import timeit
stmt ="""
fun(100)
"""
setup ="""
def fun(n):
    return [str(num) for num in range(n)]
"""
print(timeit.timeit(stmt,setup,number = 100000))
stmt2 ="""
fun2(100)
"""
setup2 ="""
def fun2(n):
    return list(map(str,range(n)))
"""
print(timeit.timeit(stmt2,setup2,number=100000))