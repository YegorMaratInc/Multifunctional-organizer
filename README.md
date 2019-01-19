МИНИСТЕРСТВО ОБРАЗОВАНИЯ ПЕНЗЕНСКОЙ ОБЛАСТИ
ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ НЕТИПОВОЕ
ОБЩЕОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ
ПЕНЗЕНСКОЙ ОБЛАСТИ «ГУБЕРНСКИЙ ЛИЦЕЙ»



Многофункциональный 
органайзер





        
    
Выполнили: учащиеся 
9 информационно-математического класса                                              
Родионов Егор и Медведев Марат 




Пенза 2018


 
Введение
Цели:
	Создать программу на языке python для помощи студентам и школьникам в их сортировки информации.
Основные Задачи:
	Изучить уже имеющиеся органайзеры
	Дополнить их своими идеями
	Создать дизайн для каждой части нашей программы
	Написать код к каждой части
	Связать код частей между собой 
Актуальность:
	Актуальность проекта состоит в том, что удобных записок и прилагающимся к ним инструментам нет на рынке органайзеров. Наша программа должна помочь в учебе школьникам и студентам.	 

 
Описание классов:
	MyWidget - основной класс, который связывает все классы
1.	__init__(self) – В нём содержатся связь с основным дизайном и меню
2.	openc (self) - Открытие калькулятора
3.	opencalendar (self)- Открытие календаря
4.	delall (self) - Удаление всех заметок
5.	closeEvent(self, event)- Закрытие приложения, сохранение данных
6.	run(self)- Функция открытия окна отвечающего за создания заметки
7.	m(self)- Функция добавления заметки
8.	list(self, button)- Функция открытия содержания заметки
	Example - класс отвечающий за создание названия и содержания заметки
1.	__init__(self)- Конструктор класса основа дизайна окна
2.	save(self) - Функция сохранения заметки
	Calculator – калькулятор
	Zam_text – класс отвечающий за изменение содержания заметки
1.	__init__(self) – конструктор класса основа дизайна окна
2.	closeEvent(self, event) - Закрытие
	Calendar – календарь
	Help – помощь 
Этапы работы над проектом:
1.	Проработка основной структуры программы
2.	Написание основы дизайна
3.	Написание кода к дизайну
4.	Написание вспомогательных функций
5.	Связка всех компонентов программы
6.	Первый основной коммит на гитхаб
7.	Конечная доработка дизайна
8.	Конченая доработка программы
9.	Второй основной коммит на гитхаб
10.	Создание записки к проекту
11.	Создание презентации к проекту
12.	Последняя проверка проекта на работоспособность
13.	Третий основной коммит на гитхаб

 
Заключение
Были выполнены следующие задачи:
	Изучить уже имеющиеся органайзеры
	Дополнить их своими идеями
	Создать дизайн для каждой части нашей программы
	Написать код к каждой части
	Связать код частей между собой 
Разработаны:
Все, что вы можете заметить в методах.
