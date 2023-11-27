
class Items:
    def __init__(self,name,amount,desc):
        self.name = name
        self.amount = int(amount)
        self.desc = desc



    def show(self):
        print(f"You Have {self.amount} of {self.name} and they are {self.desc}")

    

class Fridge:
    def __init__(self):
        self.products = {}


    def add_products(self,name,amount,desc): 
        self.products[name] = {"name" : name, "amount": amount, "desc" : desc}





    def show(self):
        if len(self.products) == 0:
            print("Your fridge is empty! Would like to add something?")
        for id in self.products.values():
            val = Items(name = id["name"], amount=id["amount"], desc=id["desc"])
            val.show()
           


    def delete(self):
        for key,value in self.products.items():
            if value["amount"] > 0:
                delt = value["amount"]
                delt -=1
                value["amount"] = delt
                print(f"You ate {delt} amount of {key}")
            
            





greeting = int(input('Hello, welcome to my fridge app. \nCheck what you have press "0"\n'))


def check_fridge():
    fridge = Fridge()
    ans = 0
    if greeting == 0:
         fridge.show()
         ans = int(input("1 for add, 2 for eat, 3 for exit and 0 for check what you have\n"))   
         while ans != 3:
             if ans == 1:
                name = input("add your item: ")
                amount = int(input("enter the amount: "))
                desc = input("dont forget describe it: ")
                fridge.add_products(name,amount,desc)

             ans = int(input("1 for add, 2 for eat, 3 for exit and 0 for check what you have\n")) 


             if ans == 0:
                 fridge.show()
      
             if ans == 2:
                 it = input("whats is the name of product? \n")
                 for key,value in fridge.products.items():
                     if it == key:
                         fridge.delete()

                 
             
 


            
           

             
         




check_fridge()