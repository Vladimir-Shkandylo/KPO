import math

#Создание класса числа 
class Num:
    #Инициализация переменных
    numbers_list = []
    def __init__ (self, string_input):
        self.string_input = string_input 

    #Функция для разбиения чисел в список
    def SplitInput(self):
        self.numbers_list = string_input.split()
        
    #Функция для перевода списка в int    
    def ConvertInput(self):
        for i in range(len(self.numbers_list)):
            self.numbers_list[i] = int(self.numbers_list[i]) 
    
    #Функция для вывода результата         
    def OutputResults(self):
        print("Сумма = ", sum(self.numbers_list))
        print("Произведение = ", math.prod(self.numbers_list))        

        
#Ввод чисел в строку
string_input = input("Введите числа для сложения через пробел \n")

#Создание инстанции класса
n1 = Num(string_input)
#Исползовния функций класса
n1.SplitInput()
n1.ConvertInput()
n1.OutputResults()