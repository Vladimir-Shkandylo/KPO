#�������� ������
class password:
    #������������� ����������
    password = "pa$$w0rd" 
    def __init__(self, input_string):
        self.input_string = input_string
        
    #������� ��� ��������� ������� � ����� ����������     
    def CompareAndOutput(self):
        if self.input_string == self.password:
            print("������ ������");
        else:
            print("�������� ������");        
    
    
    
#���� ������ 
input_string = input("������� ������\n")

#�������� ��������� ������
p1 = password(input_string)
#����������� ������� ������
p1.CompareAndOutput()


