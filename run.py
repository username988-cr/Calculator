from calculator import add, subtract, multiply, divide, power, validate_operation, get_number

def main():
    print("Простой калькулятор")
    print("1 - сложение")
    print("2 - вычитание")
    print("3 - умножение")
    print("4 - деление")
    print("5 - возведение в степень")
    print("q - выход")

    while True:
        try:
            choice = validate_operation(input("Выберите действие: "))
        except ValueError as e:
            print(e)
            continue

        if choice == "q":
            print("Выход.")
            break

        try:
            a = get_number(input("Введите A: "))
            b = get_number(input("Введите B: "))
        except ValueError as e:
            print(e)
            continue

        try:
            if choice == "1":
                print(add(a, b))
            elif choice == "2":
                print(subtract(a, b))
            elif choice == "3":
                print(multiply(a, b))
            elif choice == "4":
                print(divide(a, b))
            elif choice == "5":
                print(power(a, b))
        except Exception as e:
            print(e)


main()