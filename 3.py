def simple_gen():
    yield "Hello"
    yield "World"

gen = simple_gen()
print(next(gen))
print(next(gen))

gen = simple_gen()
for value in gen:
    print(value)