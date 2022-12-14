from initialize_db.req_sender import send_request

import pandas as pd
import os

print(os.getcwd())

students_data = pd.read_csv('tests/dummy_data.csv')
# print(students_data.iloc[:,1])

for i in range(10):
    print(students_data.loc[i,"name"])

body = """
mutation createNewStudent 
{
createStudent(student: {
    name:"S17",
    email:"173@b.c",
    mobileNo:"1724231232",
    enrollNo:"21C22017"
}) {
    name
    email
    mobileNoInteger
    enrollNo
    class_ {
    name
    }
}
}

"""

# print(send_request(body))


