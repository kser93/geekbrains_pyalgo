"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов."""

aliqout_count = [0] * 10
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            aliqout_count[j] += 1

print(aliqout_count[2:])
