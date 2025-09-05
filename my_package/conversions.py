def convert_to_integer():
    try:
        value = input('Input value: ')
        result = int(value)
        return result
    except ValueError:
        print('Error!')
        return None
