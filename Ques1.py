class Complex:
    r1 = int(input("Enter real part of first no.: "))
    i1 = int(input("Enter imaginary part of first no.: "))
    first_no = complex(r1,i1)
    r2 = int(input("Enter real part of second no: "))
    i2 = int(input("Enter imaginary part of second no: "))
    second_no = complex(r2,i2)
    print("First no is:",first_no)
    print("Second no is:",second_no)

    def add(self):
        t = self.first_no+self.second_no
        print("Sum:",t)

    def diff(self):
        d = self.first_no-self.second_no
        print("Difference:",d)
        
    def prod(self):
        p =self.first_no*self.second_no
        print("Product:",p)
        

ob1 = Complex()
ob1.add()
ob1.diff()
ob1.prod()
