
a = []
for integer in range(2320, 10987):
	if integer % 2 == 0 and integer % 11 > 0 and integer % 13 > 0 and integer % 17 > 0 and integer % 19 > 0:
		a.append(integer)
	if integer % 7 == 0 and integer % 11 > 0 and integer % 13 > 0 and integer % 17 > 0 and integer % 19 > 0:
		a.append(integer)

print(f"Всего чисел: {len(a)} \nУникальных чисел: {len(set(a))} \nМаксимальное число: {a[-1]}")