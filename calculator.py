def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Witaj w kalkulatorze!")
    while True:
        print("\nWybierz operację:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Zakończ")

        choice = input("Wybierz opcję (1/2/3/4/5): ")

        if choice == '5':
            print("Dziękujemy za skorzystanie z kalkulatora. Do widzenia!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Podaj pierwszą liczbę: "))
                num2 = float(input("Podaj drugą liczbę: "))

                if choice == '1':
                    print(f"Wynik dodawania: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Wynik odejmowania: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Wynik mnożenia: {multiply(num1, num2)}")
                elif choice == '4':
                    try:
                        print(f"Wynik dzielenia: {divide(num1, num2)}")
                    except ValueError as e:
                        print(e)
            except ValueError:
                print("Proszę podać poprawne liczby.")
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()