students = {
    2021001: ['김철수', '사회과학계'],
    2021004: ['고수진', '커뮤니케이션학'],
    2021013: ['강민아', '신문방송학'],
    2021025: ['남정은', '사회과학계'],
    2021033: ['남궁선', '사회학'],
    2021100: ['이미지', '정치외교학'],
    2021127: ['박현수', '수학'],
    2021139: ['한희수', '생명과학'],
    2021151: ['차연희', '화학'],
    2021124: ['정종현', '물리학'],
    2021157: ['지수지', '수학']
}

student_id = int(input('학번을 입력하시오 : '))

if student_id in students:
    print("{}은(는) 이미 수강생 명단에 있습니다".format(student_id))
else:
    info = input('이름과 전공을 입력하세요 : ').split()
    students[student_id] = info
    print(students)