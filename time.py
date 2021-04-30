from datetime import datetime, date, time

filename = 'date.txt'
#Выводим текущую дату
now = datetime.now() 
date1 = str(now.date())

with open(filename, 'r') as f:
	#Создаем список из строк и читаем из файла
	event = f.readlines()
	date2 = event[0]
	#Форматируем даты для дальнейшей работы
	split1 = date1.split('-')
	split2 = date2.split('.')
	now_split2 = date(int(split2[0]), int(split2[1]), int(split2[2]))
	now_split1 = date(int(split1[0]), int(split1[1]), int(split1[2]))
	print(now_split2)
	print(now_split1)
	#Вычитаем отформатированные даты
	date_time = now_split2 - now_split1
	date_time = str(date_time)
	print(date_time.split()[0])