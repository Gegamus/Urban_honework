team1_num = 5
team1_str = "В команде Мастера кода участников: %s !" % team1_num
print(team1_str)

team1_num = 5
team2_num = 6
team_str = "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num)
print(team_str)

score2 = 42
score_srt = ("Команда Волшебники данных решила задач: {} !") .format (score2)
print(score_srt)

team1_time = 18015.2
time_str = ("Волшебники данных решили задачи за {} с !") .format(team1_time)
print(time_str)

score_1 = 40
score_2 = 42
print(f"Команды решили {score_1} и {score_2} !")

challenge_result = "победа команды Мастера кода!"
print(f"Результат битвы: {challenge_result}")

tasks_total = 82
time_avg = 350.4
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")