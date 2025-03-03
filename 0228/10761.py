import sys
sys.stdin = open("input_10761.txt", "r")

'''
조건

시작점은 0
버튼의 개수는 (1~100)
K 버튼은 시작점에서 K만큼 떨어져있음
버튼 1칸씩 움직일 때 1초
버튼을 누를 때 1초
아무것도 안 하는 경우도 있다

0x Bx 형태로 어떤 값이 나열
0x: 0가 x를 누르러 가야 함을 의미
Bx: B가 x를 누르러 가야 함을 의미
0와 B는 본인이 누르는 버튼을 알고 있다.
    => 동시에 이동이 가능함
근데 수열 순서에 따라 앞선 로봇이 버튼을 누르지 않으면 뒷 순서 로봇은 버튼을 누를 수 없다.
즉 누를 때까지 기다려야 한다.

수열대로 행동할 때 가장 짧은 시간을 구하는 것이 목적! 

입력
T : tc
N : 버튼의 개수 (1~100)
0 x B x : 주어짐 ( 1<= x <= 100)


0 5 B 4 / 0 5 B 5
=> 0 5칸을 이동하는 동안 B는 버튼을 누르기 위해 대기

0 3 B 5
=> 0가 이동하고 버튼을 눌러도 B는 대기를 하지 않아도 됨
=> 남는 시간에 0는 이동할 수 있음

B 3 B 2 0 5

작업자의 순서! 
이동하는 거리!
버튼 누르는 시간

이전에 이동한 로봇이 현재 이동 로봇이랑 같은지!아닌지!
이전에 이동한 로봇이 같은 경우 
거리는 누적돼서 체크

이전에 이동한 로봇이 다른 경우
거리의 차이로 시간이 남아 대기하는지 아니면 남는 이동이 있는지 확인

이전에 이동한 로봇이 현재 로봇보다 더 많이 움직인 경우!
버튼만 누르면 됨

이전에 이동한 로봇이 ㅎ현재 로봇보다 더 적게 움직인 경우!
남은 거리만큼 추가 이동이 필요
추가로 이동할 거리를 계산
= 현재 로봇이 이동할 횟수 - 이전 로봇이 이동 횟수

이전에 이동한 로봇이 ㅎ녀재 이동할 로봇과 같은 경우
(이동할 거리를 누적) 


'''

T = int(input())
for tc in range(1, T+1):
    N, *work_list = list(map(lambda x: int(x) if x.isnumeric() else x, input().split()))

    before_robot = [None, 0] # 이전에 이동한 작업 로봇을 저장 (블루인지 오렌지인지 로봇, 거리)
    # 두 로봇의 현재 위치
    location = {
        'B':1,
        'O':1
    }
    result = 0 # 현재 작업량
    # 이전에 이동한 로봇이 같은 로봇인지 아닌지
    for i in range(N):
        robot = work_list[i*2] # 짝수 번째가 작업자으 ㅣ위치
        target = work_list[i*2+1] #현재 작업자의 목표 버튼 위치

        #이동거리
        move = abs(location[robot] - target)
        location[robot] = target

        # 이전에 이동한 로봇이 다른 로봇인 경우
        if robot != before_robot[0]:
            if move < before_robot[1]:
                result+=1
                before_robot = [robot, 1]

            else:
                remain = move - before_robot[1] + 1
                result += remain
                before_robot = [robot, remain]
        else:
            result+= move+1
            before_robot[1]+= move+1


    print(f"#{tc} {result}")
