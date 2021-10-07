array = [1, 2, 3, 5, 5, 5]
delta = 4

min_num = min(array)
count = 0
if min_num + delta == array[0]:
	count += 1
if min_num + delta == array[1]:
	count += 1
if min_num + delta == array[2]:
	count += 1
if min_num + delta == array[3]:
	count += 1
if min_num + delta == array[4]:
	count += 1
if min_num + delta == array[5]:
	count += 1	

print('Найдено', count, 'числа')

