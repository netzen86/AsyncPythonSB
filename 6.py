def wrapper(data):
    for one_item in data:
        yield one_item

def wrapper_yield(data):
    yield from data


g1 = wrapper('abcd')
g2 = wrapper_yield('abcd')
print(list(g1), list(g2))