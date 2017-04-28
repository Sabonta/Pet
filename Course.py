def main():

    course_num = input("Enter a course number: ")

    room = room_num()
    instructor = instructor_names()
    times = meeting_time()
    print('The course', course_num, 'is located in room number', room.get(course_num), 'with',
          instructor.get(course_num), 'at', times.get(course_num))

def room_num():

    course_room = {'CS101': '3004', 'CS102': '4501', 'CS103' : '6755', 'NT110':'1244', 'CM241': '1411'}

    return course_room


def instructor_names():
    course_namees = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103' : 'Rich', 'NT110':'Burke', 'CM241': 'Lee'}

    return course_namees


def meeting_time():
    course_times = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103' : '10:00 a.m.', 'NT110':'11:00 a.m.',
                    'CM241': '1:00 p.m.'}
    return course_times

main()