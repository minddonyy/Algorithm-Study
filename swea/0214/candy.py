total_candy = 20

queue = []
queue.append((1,1))
cnt_person = 1
last_person = None

while total_candy > 0:
    # queue에서 줄 ㅅ ㅓ있는 애들한테 나눠줘야한다.
    person, cnt = queue.pop(0)

    print(person,cnt)

    if total_candy - cnt <= 0:
        last_person = person
        break

    total_candy -= cnt # 나눠준액션

    # 캔디를 받은 사람은 다시 줄을 선다.
    queue.append((person, cnt + 1))
    cnt_person = max(cnt_person, person+1)
    queue.append((cnt_person, 1))




print(f"마지막 마이쮸는 {last_person}번")
