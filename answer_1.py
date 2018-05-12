answers = {'привет':'привет', 'как дела': 'Лучше всех', 'пока': 'увидимся'}

def get_answer (question):
	#question = input('Что вы хотите спросить: ')
	return answers.get(question, 'wtf?')

#question = input('Что вы хотите спросить: ')
#answers = {'привет':'привет', 'как дела': 'Лучше всех', 'пока': 'увидимся'}
print(get_answer(input('Введите слово: ')))