class arithmetic:
    def inpt(self):
        self.num1=int(input("enter the first number: "))
        self.num2=int(input("enter the second number: "))

    def add(self):
        print("addition is:",self.num1 + self.num2)
    
    def sub(self):
        print("subtraction is:",self.num1- self.num2)
    
    def mul(self):
        print("multiplication is:",self.num1 * self.num2) 
    
    def div(self):
        print("division is:",self.num1 / self.num2)

obt1=arithmetic()
obt1.inpt()
obt1.add()
obt1.sub()
obt1.mul()
obt1.div()
    
    
        

