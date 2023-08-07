# 1. 빈 리스트 생성하기
empty_list = []
print(empty_list)  # 출력: []

# 리스트에 값 추가
empty_list.append(10)
empty_list.append(20)
empty_list.append(30)
print(empty_list)  # 출력: [10, 20, 30]

# 2. 리스트 인덱싱과 슬라이싱
# 리스트 생성
numbers = [1, 2, 3, 4, 5]

# 리스트 인덱싱
print(numbers[0])  # 출력: 1
print(numbers[2])  # 출력: 3

# 리스트 슬라이싱
print(numbers[1:4])  # 출력: [2, 3, 4]
print(numbers[:3])  # 출력: [1, 2, 3]
print(numbers[2:])  # 출력: [3, 4, 5]

# 3. 리스트 반복문 활용하기
# 리스트 생성
fruits = ['apple', 'banana', 'orange']

# for 반복문으로 리스트 출력
for fruit in fruits:
    print(fruit)

# 출력:
# apple
# banana
# orange


# 4. 리스트 내포 (List Comprehension)
# 기존 방법: 리스트에 1부터 5까지 제곱 값을 저장하기
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(squares)  # 출력: [1, 4, 9, 16, 25]

# 리스트 내포를 이용한 방법
squares = [num ** 2 for num in range(1, 6)]
print(squares)  # 출력: [1, 4, 9, 16, 25]

# 5. 리스트 내장 메서드 활용하기
# 리스트 생성
numbers = [5, 2, 8, 4, 1]

# 리스트 정렬하기
numbers.sort()
print(numbers)  # 출력: [1, 2, 4, 5, 8]

# 리스트 뒤집기
numbers.reverse()
print(numbers)  # 출력: [8, 5, 4, 2, 1]

# 리스트에서 값 제거하기
numbers.remove(5)
print(numbers)  # 출력: [8, 4, 2, 1]

# 리스트 길이 구하기
length = len(numbers)
print(length)  # 출력: 4

# 6. 다차원 리스트
# 2차원 리스트 생성
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 행과 열 순회
for row in matrix:
    for element in row:
        print(element)

# 출력:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


# 7. 리스트 병합하기
# 두 개의 리스트를 병합하여 새로운 리스트 생성
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print(merged_list)  # 출력: [1, 2, 3, 4, 5, 6]

# 8. 리스트에서 최소값과 최대값 찾기
# 리스트에서 최댓값과 최솟값 찾기
numbers = [10, 5, 7, 24, 2]

max_value = max(numbers)
min_value = min(numbers)

print("최댓값:", max_value)  # 출력: 최댓값: 24
print("최솟값:", min_value)  # 출력: 최솟값: 2


# 9. 중첩된 리스트 평탄화 (Flatten)
# 중첩된 리스트를 평탄화하는 함수 정의
def flatten_list(nested_list):
    flattened = [item for sublist in nested_list for item in sublist]
    return flattened


# 중첩된 리스트
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# 리스트 평탄화
flattened_list = flatten_list(nested_list)
print(flattened_list)  # 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 10. 리스트 요소 개수 세기
# 리스트에서 특정 요소의 개수 세기
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi']

banana_count = fruits.count('banana')
kiwi_count = fruits.count('kiwi')
grape_count = fruits.count('grape')

print("바나나 개수:", banana_count)  # 출력: 바나나 개수: 2
print("키위 개수:", kiwi_count)  # 출력: 키위 개수: 1
print("포도 개수:", grape_count)  # 출력: 포도 개수: 0

# 11. 리스트 요소 거꾸로 뒤집기
# 슬라이싱을 이용한 리스트 요소 거꾸로 뒤집기
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # 출력: [5, 4, 3, 2, 1]

# 리스트 내장함수인 reverse() 메서드를 사용한 리스트 요소 거꾸로 뒤집기
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # 출력: [5, 4, 3, 2, 1]

# reversed() 함수 사용하기
my_list = [1, 2, 3, 4, 5]
reversed(my_list)
print(my_list)  # 출력: [5, 4, 3, 2, 1]

# 12. 리스트에서 특정 값의 인덱스 찾기
# 리스트에서 특정 값의 인덱스 찾기
fruits = ['apple', 'banana', 'orange', 'kiwi']

# 'banana'의 인덱스 찾기
index_banana = fruits.index('banana')
print("바나나의 인덱스:", index_banana)  # 출력: 바나나의 인덱스: 1
