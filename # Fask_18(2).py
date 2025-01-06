# Fask_18(2)
import random
# Список учеников
students=['Надя','Наташа','Виталя','Ваня','Вова','Нина']
students.sort()
#Список предметов
classes=['Математика','Русский язык','Английский язык','Физическая культура']
#Пустой словарь с оценками по каждому предмету
students_marks={}
for student in students:
   students_marks[student]={}
   for classe in classes:
      mark=[random.randint(1,5) for i in range(3)]
      students_marks[student][classe]=mark
   #Выводим получиывшийся словарь с оценками
   for student in students:
      print(f'''{student}{students_marks['Ваня']}''')
      print('''Список команд:
            1. Добавить оценки ученика по предмету
            2.Вывести средний балл по всем предметам
            3.Вывести все оценки по всем ученикам
            4.Удалить оценку
            5.Редактировать оценку
            6.Полная информация по  ученику
            7.Средний балл ученика по предмету
            4.Выход из программы''')
      

students_marks={'Надя':
                     {'Математика':[mark],
                      'Русский язык':[mark],
                      'Английский язык':[mark],
                      'Физическая культура':[mark]},          
            'Наташа':
                      {'Математика':[mark],
                      'Русский язык':[mark],
                      'Английский язык':[mark],
                      'Физическая культура':[mark]},
            'Виталя':
                      {'Математика':[mark],
                      'Русский язык':[mark],
                      'Английский язык':[mark],
                      'Физическая культура':[mark]},
              'Ваня':
                     { 'Математика':[mark],
                      'Русский язык':[mark],
                      'Английский язык':[mark],
                      'Физическая культура':[mark]},
              'Вова':
                      {'Математика':[mark],
                      'Русский язык':[mark],
                       'Английский язык':[mark],
                      'Физическая культура':[mark]},
              'Нина':
                      {'Математика':[mark],
                      'Русский язык':[mark],
                      'Английский язык':[mark],
                      'Физическая культура':[mark],}
                      }

while True:
                command=int(input('Введите команду:')) 
#Если данные  введены верно
                if command == 1:
                 print('1.Добавить оценку ученика по предмету')
                 student=(input('Введите имя ученика:'))
                 classes=(input('Введите предмет:'))
                 mark=int(input('Введите оценку:'))
                
                 if student in students_marks.keys() and classe in students_marks(student).keys():
#Добавляем новую оценку
                  students_marks[student][classe].append(mark)
                  print(f'Для {student} по предмету {classe} добавлена оценка{mark}')
#Неверные данные
                 else:
                  print('Ошибка:неверное имя ученика или название предмета')  
                elif command ==2:
                 print('2.Вввести средний балл по всем предметам по каждому ученику')
                 for student in students:
                  print(student)
                 for classe in classes:
# Находим сумму оценок по предмету 
                  marks_sum=sum(students_marks[student][classe])
# находим количество оценок по предмету
                  marks_count=len(students_marks[student][classe]) 
# выводим средний балл
                  print(f'{classe}-{marks_sum//marks_count}')
                  print()
                elif command == 3:
                 print('3.Вывести все оценки по всем ученикам')
                
#Словарь с оценками 
# цикл по ученикам

                 for student in students:
                  print(student)
                 for classe in classes:
                  print(f'\t{classe}-{students_marks[student][classe]}')
                  print()
                elif command == 4:
              #Удаление оценки
                 if mark [classe]:
                  def remove_grade(student, subject, index):
                   mark[student][subject].pop(index)   
                 print(input('4.Удалите оценку:'))
                 print(input('Оценка {''} удалена'))
                elif command ==5:
              #Редактирование оценки
                 def edit_grade(student, subject, index, new_grade):
                  mark[student][subject][index] = new_grade
                 print(input('5.Исправьте  оценку:'))
                 print(input('на:'))
                elif command == 6:
              #Информация о ученике
                 def print_student_info(student):
                  print(f'{'Ученик'}: {student}')
                  for subject, marks in mark[student].items():
                   print('6.'(f"{subject}: {marks}, средний балл: {(student):.2f}"))
                   print()
#Средний балл определенного ученика
                elif command ==7:
                 def print_student_info(student):
                  print(f'{'Ученик'}: {student}')
                  print(f"Средний балл [,]: {calculate_average_marks(mark[''])}")
              
                elif command== 8:
                 print('8.Выход из программы')
                 break 