try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Invalid data type!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except KeyboardInterrupt:
    print()
    print("User interrupted the execution!")
else:
    print(f"O resultado é: {r:.1f}")
finally:
    print("Volte sempre!")
