result = []
n = int(input('введите число от 3 до 20: '))
for i in range(1, 21):
    for j in range(1, 21):
        m = i + j
        if n % m == 0 and i < j:
            result.append(i)
            result.append(j)
print(*result)
