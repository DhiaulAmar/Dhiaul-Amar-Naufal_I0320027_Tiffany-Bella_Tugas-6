for i in range(10, 25):
    check = False
    a = 2;
    while i % a != 0:
        if a == i - 1:
            print("%d adalah bilangan prima" % i)
            check = True
        a = a + 1;
    if not check:
        print("%d bukan prima" % i)