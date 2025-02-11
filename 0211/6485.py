import sys
sys.stdin = open('input_6485.txt', 'r')
########################################

T = int(input())      # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())

    bus_stop = [0]*5001
    for n in range(1, N+1):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi+1):
            bus_stop[i]+=1

    P = int(input())

    st =[]
    for j in range(P):
        numbers = int(input())
        st.append(numbers)

    print(f"#{tc}", end=" ")
    for k in st:
        print(bus_stop[k], end=" ")
    print()



