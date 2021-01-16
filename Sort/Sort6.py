#  성적이 낮은 순서로 학생이름 출력
n = int(input())
students = [['', 0]for _ in range(n)]
for i in range(n):
     students[i][0], students[i][1] = input().split()
     students[i][1] = int(students[i][1])

students = sorted(students, key=lambda score: score[1])

for student in students:
    print(student[0], end=' ')
