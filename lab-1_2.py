#Создание класса
class password:
    #Инициализация переменных
    password = "pa$$w0rd" 
    def __init__(self, input_string):
        self.input_string = input_string
        
    #Функция для сравнения паролей и вывод результата     
    def CompareAndOutput(self):
        if self.input_string == self.password:
            print("Верный пароль");
        else:
            print("Неверный пароль");        
    
    
    
#Ввод пароля 
input_string = input("Введите пароль\n")

#Создание инстанции класса
p1 = password(input_string)
#Исползовние функции класса
p1.CompareAndOutput()


