### 리스트에서 홀수만 추출하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for문과 if문을 사용하여 홀수만 추출하여 새로운 리스트 생성
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

# 결과 출력
print(odd_numbers)  # 출력: [1, 3, 5, 7, 9]

### 1차원 리스트에서 최대/최소값 찾기
# 1차원 리스트
numbers = [5, 2, 8, 4, 1, 9, 6]

# for문과 if문을 사용하여 최댓값과 최솟값 찾기
max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

# 결과 출력
print("최댓값:", max_value)  # 출력: 최댓값: 9
print("최솟값:", min_value)  # 출력: 최솟값: 1

### 리스트 내 중복 제거하기
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']

# for문과 if문을 사용하여 중복 제거하기
unique_fruits = []

for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

# 결과 출력
print(unique_fruits)  # 출력: ['apple', 'banana', 'orange', 'kiwi']

### 리스트에서 짝수와 홀수 분리하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for문과 if문을 사용하여 짝수와 홀수 분리하기
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# 결과 출력
print("짝수:", even_numbers)  # 출력: 짝수: [2, 4, 6, 8, 10]
print("홀수:", odd_numbers)  # 출력: 홀수: [1, 3, 5, 7, 9]

### 리스트의 모든 요소 곱하기
numbers = [1, 2, 3, 4, 5]

# for문을 사용하여 리스트의 모든 요소 곱하기
result = 1

for num in numbers:
    result *= num

# 결과 출력
print("곱셈 결과:", result)  # 출력: 곱셈 결과: 120

### 두 개의 리스트를 조합하여 새로운 리스트 생성하기
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

# zip() 함수와 unpack을 사용하여 두 리스트 조합하기
combined_list = []

for name, score in zip(names, scores):
    combined_list.append([name, score])

# 결과 출력
print(combined_list)  # 출력: [['Alice', 85], ['Bob', 90], ['Charlie', 78]]
