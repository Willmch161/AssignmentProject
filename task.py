def convertionTointeger():
    try:
        value = (input('input value:'))
        result = int(value)
        return result
    except ValueError:
        print('Error!!')
print(convertionTointeger())

def AccessList():
    fruits = ['mango', 'orange', 'grape', 'watermelon']
    try:
        index = int(input("Input index (1-3)"))
        print(f'Fruit in index {index}:{fruits[index]}')
        return fruits[index]
    except IndexError:
        print ('Error: Index diluar jangkauan.')
        return None
    except ValueError:
        print('Error: must input with number for index')
        return None
    
def devideNumber():
    try:
        a = float(input('Input first number:'))
        b = float(input('Input second number:'))
        result = a / b
        print('Result devide: {result}')
        return result
    except ZeroDivisionError:
        print('Error: Cant devide with zero')
        return None
    except ValueError:
        print("Error: input must with number")
        return None
        
    