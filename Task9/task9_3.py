numbers = list(map(int, input().split()))
numbersUniq = set()
for i in numbers:
    print('YES' if i in numbersUniq else 'NO')
    numbersUniq.add(i)
