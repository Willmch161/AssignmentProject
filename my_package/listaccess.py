def access_list():
    fruits = ['mango', 'orange', 'grape', 'watermelon']
    try:
        index = int(input("Input index (1–3): "))
        print(f'Fruit in index {index}: {fruits[index]}')
        return fruits[index]
    except IndexError:
        print('Error: Index diluar jangkauan.')
        return None
    except ValueError:
        print('Error: must input with number for index')
        return None
