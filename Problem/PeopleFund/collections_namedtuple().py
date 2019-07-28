from collections import namedtuple


n, categories = int(input()), input().split()
students = namedtuple('students', categories)
print(sum(int(students._make(input().split()).MARKS) for _ in range(n)) / n)


"""
without namedtuple

stu, marks = int(input()), input().split().index("MARKS")
print (sum([int(input().split()[marks]) for _ in range(stu)]) / stu)
"""
