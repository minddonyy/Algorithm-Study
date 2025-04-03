import sys
sys.stdin = open("input.txt", "r")

switch_count = int(input())
switch_status = list(map(int, input().split()))
student_count = int(input())

student_info = [list(map(int, input().split())) for _ in range(student_count)]



for i in range(switch_count):
    for j in range(student_count):
        if student_info[0][j] == 1:


