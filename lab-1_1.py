import math

#�������� ������ ����� 
class Num:
    #������������� ����������
    numbers_list = []
    def __init__ (self, string_input):
        self.string_input = string_input 

    #������� ��� ��������� ����� � ������
    def SplitInput(self):
        self.numbers_list = string_input.split()
        
    #������� ��� �������� ������ � int    
    def ConvertInput(self):
        for i in range(len(self.numbers_list)):
            self.numbers_list[i] = int(self.numbers_list[i]) 
    
    #������� ��� ������ ����������         
    def OutputResults(self):
        print("����� = ", sum(self.numbers_list))
        print("������������ = ", math.prod(self.numbers_list))        

        
#���� ����� � ������
string_input = input("������� ����� ��� �������� ����� ������ \n")

#�������� ��������� ������
n1 = Num(string_input)
#����������� ������� ������
n1.SplitInput()
n1.ConvertInput()
n1.OutputResults()