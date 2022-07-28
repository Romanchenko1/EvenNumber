import timeit
#в моем варианте данная функция более громоздкая и занимает больше места, выполнение данной функции состовляет: 7.025999948382377e-06
def EvenNumber(Value):
     if Value % 2 == 0:
          print("Четное число")
     elif Value % 2 != 0:
          print("Нечетное число")
#здесь только плюсы, компактная и время выполнения: 2.9459991492331026e-06
def isEven(value):
     return value%2==0


codeToTest = """
def EvenNumber(Value):
     if Value % 2 == 0:
          print("Четное число")
     elif Value % 2 != 0:
          print("Нечетное число")
print(EvenNumber(5))
"""


codeToTest1 = """
def isEven(value):
     return value%2==0
print(isEven(5))
"""


#elapsedTime = timeit.timeit(codeToTest, number = 100) / 100
#print(elapsedTime)"

#elapsedTime1 = timeit.timeit(codeToTest1, number = 100) / 100
#print(elapsedTime1)

#print(EvenNumber(5))
#print(isEven(4))