data = []
while True:
  menu = int(input('Enter Menu: '))
  if menu == 1:
    insert = input('Enter Student Name: ')
    data.append(insert)
  elif menu == 2:
    if data:
      print('=== List of Student ===')
      for i, datas in enumerate(data):
        print(i, datas)
    else :
      print('Data Not Available')
  elif menu == 3:
    edit = int(input('Enter number you want to edit: '))
    if 0 <= edit < len(data):
      update = input('Update Data: ')
      data[edit] = update
      print('Data Updated')
    else:
      print('Invalid number')
  elif menu == 4:
    delete = int(input('Enter number you want to delete: '))
    if 0 <= edit < len(data):
      data.pop(delete)
      print('Data Deleted')
    else:
      print('Invalid number')
  elif menu == 5:
    print('Do you want to exit?')
    choose = input('Enter Yes or No: ')
    if choose == 'Yes':
      print('See you later!')
      break
    else:
      print('Continue input data')
  else:
    print('Invalid input, Input(1-5)')