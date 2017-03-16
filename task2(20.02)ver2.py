l = [1, 2, 3, 8, 14, 89, 45]
number = int(len(l))


for i in range(number // 2):
	l[i], l[number-i-1] = l[number-i-1],l [i]

print(l)
