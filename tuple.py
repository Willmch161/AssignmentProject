student = {"Name": "Wiliam", 'Age': 20, 'Class': 'Second'}
student['Age'] = 222
student['University'] = "NusaPutraUniversity"

print ("student ['Name'] :", student ['Name'] )
print("student['Age']: ", student['Age'])
print("student['School']: ", student.get('University', 'NusaPutraUniversity'))
