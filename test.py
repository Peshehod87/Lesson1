test = {'city':'Питер', 'temperature': '15', 'wind': 'Северо-Западный'}
dic = {'Сергей': {'city':'Саратов', 'temperature': '25', 'wind': 'Северо-Западный'},
		'Маша':{'city':'Великий Устюг', 'temperature': '-25', 'wind': 'Южный'}, 'Егор': test}
key = dic.keys()
print(key)
name = input('Как Вас зовут: ')
if name in dic:
	print(dic[name])
else: 
	print('Нет такого пользователя')