import sys
sys.stdin = open('input_13300.txt', 'r')
########################################
"""
여학생인 경우 0
남학생인 경우 1
방에 2명씩 들어갈 수 있고 학년과 성별이 같아야 함
방에 한 명만 들어갈 수도 있음
2차원 카운팅 배열을 만든다
그리고 성별이랑 학년을 카운팅 배열에 넣는다
"""
N, K = map(int,input().split())
student_info = [[0]* 6 for _ in range(2)]
for _ in range(N):
    sex, grade = map(int, input().split())
    student_info[sex][grade-1] += 1

room_count = 0
for i in range(2):
    for j in range(6):
        if student_info[i][j] % K == 0:
            room_count += int(student_info[i][j] / K)
        else:
            room_count += int(student_info[i][j] / K) + 1

print(room_count)



