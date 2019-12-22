def even_num():
    n = 0;
    while True:
        yield n;
        n += 2;

my_gen = even_num();

print(next(my_gen));
print(next(my_gen));
print(next(my_gen));

a = 225;
print(a);

print(next(my_gen));
