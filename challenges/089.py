from random import choice, uniform

NAMES = [
    "Ana",
    "Bruno",
    "Carlos",
    "Daniel",
    "Eduarda",
    "Felipe",
    "Gabriel",
    "Helena",
    "Isabela",
    "João",
    "Karina",
    "Lucas",
    "Mariana",
    "Nicolas",
    "Olivia",
    "Paulo",
    "Rafael",
    "Sofia",
    "Thiago",
    "Vinicius",
    "Yasmin",
    "Amanda",
    "Beatriz",
    "Caio",
    "Diego",
    "Elisa",
    "Fernanda",
    "Giovana",
    "Henrique",
    "Igor",
    "Juliana",
    "Larissa",
    "Mateus",
    "Natália",
    "Otávio",
    "Patrícia",
    "Renato",
    "Samuel",
    "Tatiane",
    "Vanessa",
]

LAST_NAMES = [
    "Silva",
    "Santos",
    "Oliveira",
    "Souza",
    "Lima",
    "Costa",
    "Ferreira",
    "Almeida",
    "Rodrigues",
    "Pereira",
    "Carvalho",
    "Gomes",
    "Martins",
    "Rocha",
    "Barbosa",
    "Ribeiro",
    "Alves",
    "Melo",
    "Teixeira",
    "Cardoso",
]

students = []
id = 1


for student_id in range(1, 101):
    name = f"{choice(NAMES)} {choice(LAST_NAMES)}"
    grades = [round(uniform(0, 10), 1), round(uniform(0, 10), 1)]
    average = round(sum(grades) / 2, 1)

    students.append([student_id, name, grades, average])


ADDING_STUDENT_TEXT = "============ Adding Student ============"
REPORT_TITLE_TEXT = "============ Students Report ==========="
GRADE_VIEW_TITLE = "============ Student Grade ============="


# print(ADDING_STUDENT_TEXT)
# while True:
#     name = input("Name: ")
#     grade_1 = float(input("Grade 1: "))
#     grade_2 = float(input("Grade 2: "))
#     q = input("Finish (s/N): ")
#     print()
#
#     student = []
#     student.append(id)
#     student.append(name)
#     student.append([grade_1, grade_2])
#
#     average = 0
#     for grade in student[2]:
#         average += grade
#
#     average /= len(student[2])
#     student.append(average)
#
#     id += 1
#
#     students.append(student)
#
#     if q == "s" or q == "S":
#         break
#
# print(len(ADDING_STUDENT_TEXT) * "=")
# print()

longest_name = 0
longest_id = len(str(students[-1][0]))

for student in students:
    longest_name = max(len(student[1]), longest_name)

id_head = " ID".ljust(longest_id + 2, " ")
name_head = " NAME".ljust(longest_name + 2, " ")
average_head = " AVERAGE"

print(REPORT_TITLE_TEXT)
print(
    len(id_head) * "─"
    + "┬"
    + len(name_head) * "─"
    + "┬"
    + (len(average_head) + 1) * "─"
)
print(f"{id_head}│{name_head}│{average_head}")
print(
    len(id_head) * "─"
    + "┼"
    + len(name_head) * "─"
    + "┼"
    + (len(average_head) + 1) * "─"
)
for student in students:
    print(f"{student[0]:{longest_id + 1}} ", end="│ ")
    print(f"{student[1]:{longest_name}} ", end="│ ")
    print(f"{student[3]}")

print(
    len(id_head) * "─"
    + "┴"
    + len(name_head) * "─"
    + "┴"
    + (len(average_head) + 1) * "─"
)

while True:
    id = input("Show student's grades (q to exit) ID: ")
    if id == "q":
        break

    id = int(id)

    for student in students:
        if student[0] == id:
            print(f"╔{(longest_name + 12) * '═'}╗")
            print(f"║ NAME: {student[1].ljust(longest_name + 4)} ║")
            print(f"║ GRADE 1: {str(student[2][0]).ljust(longest_name)}  ║")
            print(f"║ GRADE 2: {str(student[2][1]).ljust(longest_name)}  ║")
            print(f"╚{(longest_name + 12) * '═'}╝")

print()
