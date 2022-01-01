# on definit la classe (point)
class Point :
    Px=0.0
    Py=0.0
    # le constructeur 
    def __init__(self,arg1=0.0,arg2=0.0):
        self.Px=arg1
        self.Py=arg2

# la classe segment 
class Segment :
     origine=Point()
     extremite=Point()
     def __init__(self,x=0,y=0,z=0,t=0):
        self.origine.Px=x
        self.origine.Py=y
        self.extremite.Px=z
        self.extremite.Py=t
     def display(self):
         print(" Voila un segment :",end=' ')
         for i in range(1,self.extremite.Px-self.origine.Px +1):
             if(i==1 or  i==self.extremite.Px-self.origine.Px):
                 print("*",end='')
             else:
                 print("-",end='')
         print("\n")


def auto_test():
    test=Segment(1,2,3,4)
    test.display()

# le programme principale : appel a la methode auto-test pour test la classe 

print("---------- tester le programme -----------")
auto_test()


