import sys
sys.stdin = open("input.txt", "r")

def is_palindrome(word, left, right):

    if left >= right:
        return True

    if word[left] != word[right]:
        return False

    return is_palindrome(word, left+1, right-1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = input().strip()
    word_len = len(word)

    result = 1

    for idx in range(word_len // 2):
        if word[idx] != word[word_len -1 -idx]:
            result = 0
            break

    result = is_palindrome(word,0, word_len-1)
    print(f"#{test_case} {result}")
