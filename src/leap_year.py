from tkinter import BooleanVar


def is_leap_year()->bool:

    year : int= int(input("Ingrese un año: "))  # type: ignore
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                print(f"El año {year} es bisiesto")
                return True
            else:
                print(f"El año {year} no es bisiesto")
                return False
        else:
            print(f"El año {year} es bisiesto")
            return True
    else:
        print(f"El año {year} no es bisiesto")
        return False

