"""def hello_fn():
    return "hello world"
print(len(hello_fn()))
print(hello_fn().upper())
print(hello_fn().lower())"""

#pass arguments
"""def fn(greeting,n='s'):
    return '{}, {}'.format(greeting,n)
print(fn('Hello',n='r'))"""

#advanced
"""def std_info(*args,**kwargs):
    print(args)
    print(kwargs)
std_info('c','python',name='rs',age=20)"""
#leap year
m_d=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(y):
    return y%4==0 and (y%100!=0 or y%400==0)
def is_month(y,m):
    if not 1<=m<=12:
        return "invalid month"
    if m == 2 and is_leap(y):
        return 29
    return m_d[m]
#print(is_leap(2024))
print(is_month(2024,2))