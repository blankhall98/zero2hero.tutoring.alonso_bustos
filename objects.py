# objects.py

#object 1: CAT

class CAT:
    
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def miau(self):
        print('Miau Miau Miau')
        
    def greet(self):
        print(f'miau, my name is {self.name}')
        
cat1 = CAT('garfield',5,'Persa')
cat2 = CAT('aslan',9,'siames')

#object 2: Client

inputs = {
    'name': 'Jonatan',
    'last name': 'Blank',
    'age': 26,
    'mail': 'xblankhallx@gmail.com'
    }

class Client:
    
    def __init__(self,inputs):
        self.inputs = inputs
        
    def client_name(self):
        print(f"The name of the client is {self.inputs['name']} {self.inputs['last name']}")
    
    def client_mail(self):
        print(self.inputs["mail"])
        
client1 = Client(inputs)

#object 3: Finance Calculator
import matplotlib.pyplot as plt
import numpy as np

class FinCal:
    
    def __init__(self):
        pass
    
    def compound_interest(self,initial,rate,time):
        return initial*(1+rate/100)**time
    
    def simulate_compound(self,initial,rate,time):
        T = np.array(range(time+1))
        values = self.compound_interest(initial,rate,T)
        plt.figure()
        plt.plot(T,values)
        plt.xlabel("Years")
        plt.ylabel("Debt")
        plt.title("Debt Evolution Simulation")
        plt.show()
        
app = FinCal()
        