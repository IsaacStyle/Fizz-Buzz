def fizz_buzz(num):
    count = 1
    while count <= num:
        count += 1
        if count % 3 == 0 and count % 5 == 0:
            print(f"{count} = fizzbuzz")
        elif count % 3 == 0:
            print(f"{count} = fizz")
        elif count % 5 == 0:
            print(f"{count} = buzz")


fizz_buzz(100)