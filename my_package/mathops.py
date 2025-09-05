def devide_number():
    try:
        a = float(input('Input first number: '))
        b = float(input('Input second number: '))
        result = a / b
        print(f'Result devide: {result}')
        return result
    except ZeroDivisionError:
        print('Error: Cant divide with zero')
        return None
    except ValueError:
        print("Error: input must be a number")
        return None
