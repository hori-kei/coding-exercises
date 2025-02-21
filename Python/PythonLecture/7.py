for i in range(1, 31):
    if i % 15 == 0:
        print(f"{i} : FizzBuzz")
    elif i % 5 == 0:
        print(f"{i} : Buzz")
    elif i % 3 == 0:
        print(f"{i} : Fizz")
    else:
        print(i)
