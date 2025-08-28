"""lists of lists"""

classroom = [
    [
        "João",
        "Adriana",
    ],
    [
        "Otávio",
    ],
    [
        "Marcus",
        "Luiz",
        "Pedro",
        (0, 10, 20, 30, 40),
    ],
]

print(classroom[0])
print(classroom[2][1])
print(classroom[2][3][2])

for clas in classroom:
    print(clas)
    for student in clas:
        print(student)
