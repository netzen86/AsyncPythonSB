def simple_gen():
    while True:
        x = yield
        print(f'Got x={x}. Doubling: {x * 2}')

gen = simple_gen()
next(gen) # Инициализируем
gen.send(2) # Отправляем значение в генератор
gen.send(4)
gen.send(5)
gen.send(6)