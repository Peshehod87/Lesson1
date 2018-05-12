def get_answer (question, answers):
	#question = input('Что вы хотите спросить: ')
	if question in answers:
		return answers[question]
	else:
		return 'Диалог не удался'

question = input('Что вы хотите спросить: ')
answers = {'привет':'привет', 'как дела': 'Лучше всех', 'пока': 'увидимся'}
l = get_answer(question, answers)
print (l.lower())