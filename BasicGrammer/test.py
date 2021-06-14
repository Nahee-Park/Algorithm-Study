# sum() 합
result_sum = sum([2, 3, 4, 5, 6])
print(result_sum)

# min() max() 최소 최대
result_min = min(3, 5, 1, 2, 6)
result_max = max(3, 5, 1, 2, 6)
print(result_min)
print(result_max)

# eval() 실제 계산 결과
print(eval("(2+3)*4"))

# sorted 오름차순
print(sorted([1, 2, 3, 9, 8, 7, 6]))
print(sorted([1, 2, 3, 9, 8, 7, 6], reverse=True))

# sorted() with key
array = [('나히', 22), ('민지', 19), ('엄마', 49)]
print(sorted(array, key=lambda x: x[1]))
