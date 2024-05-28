course_name = 'Python'
total_tasks = 12
total_time = 1.5
task_time = total_time / total_tasks
new_task_time = str(task_time) + ' часа.'

question = ['Курс: ', 'всего задач: ', 'затрачено часов: ', 'среднее время выполнения: ']
answer = [course_name, total_tasks, total_time, new_task_time]
str_answer = list(map(str, answer))
result = [i + j for i, j in zip(question, str_answer)]
print('\033[1m' + ', '.join(result) + '\033[0m')

