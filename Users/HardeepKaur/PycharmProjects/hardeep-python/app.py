
# def age_program():
#     user_age = input("please enter you age: ")
#     age_Seconds = int(user_age) * 364 * 24 * 60 * 60
#     print("your age in seconds is {}".format(age_Seconds))
#
# age_program()

import pymongo

uri =  "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['hardeepstack']
collection = database['students']

students = [student['age'] for student in collection.find({})]

print(students)
# student_list = []
#
# for student in students:
#     student_list.append(student)

