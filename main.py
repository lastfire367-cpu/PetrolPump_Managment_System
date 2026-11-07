import re
from abc import ABC,abstractmethod
import csv
def get_value() :
    while True :
        try :
            y=int(input("Enter a value "))
        except Exception as e :
           continue
        else :
            return y

class Fuel:
   
    def __init__(self,p_p=0,p_q=0,d_p=0,d_q=0):
        self.__petrol_price=p_p
        self.__petrol_quantity=p_q
        self.__disel_price=d_p
        self.__disel_quantity=d_q
    def  petrolPriceChange(self):
        print("New Petrol Price ")
        self.__petrol_price=get_value( )
        data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Petrol.csv","r") as file:
           reader=csv.DictReader(file,skipinitialspace=True)
           for  line  in reader :
               data.append({"Price":line['Price'],"Quantity":line['Quantity']})
        data[0]["Price"]=self.__petrol_price
        
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Petrol.csv","w") as file:
            file.write(f"Price,Quantity\n")
            for line in data:
                file.write(f"{line['Price'] },{line['Quantity']}\n")
        print("Changed :: ")
    def  diselPriceChange(self):
            print("New Disel Price ")
            self.__disel_price=get_value( )
            data=[]
            with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv","r") as file:
               reader=csv.DictReader(file,skipinitialspace=True)
               for  line  in reader :
                   data.append({"Price":line['Price'],"Quantity":line['Quantity']})
            data[0]["Price"]=self.__disel_price
            
            with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv","w") as file:
                file.write(f"Price,Quantity\n")
                for line in data:
                    file.write(f"{line['Price'] },{line['Quantity']}\n")
            print("Changed :: ")
    def diselQuantityChange(self):
        print("New Quantity of Disel ")
        self.__disel_quantity=get_value()
        data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append({"Price":line['Price'],"Quantity":line['Quantity']})
        data[0]["Quantity"]=self.__disel_quantity
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv","w") as file:
            file.write(f"Price,Quantity\n")
            for line in data:
                file.write(f"{line['Price']},{line['Quantity']}\n")
        print("Changed:: ")
    def petrolQuantityChange(self):
            print("New Quantity of Petrol ")
            self.__petrol_quantity=get_value()
            data=[]
            with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Petrol.csv") as file:
                reader=csv.DictReader(file,skipinitialspace=True)
                for line in reader:
                    data.append({"Price":line['Price'],"Quantity":line['Quantity']})
            data[0]["Quantity"]=self.__petrol_quantity
            with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Petrol.csv","w") as file:
                file.write(f"Price,Quantity\n")
                for line in data:
                    file.write(f"{line['Price']},{line['Quantity']}\n")
            print("Changed:: ")
    def display(self):
        lines_petrol=[]
        lines_disel=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Petrol.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                lines_petrol.append({"Price":line['Price'],"Quantity":line['Quantity']})
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                lines_disel.append({"Price":line['Price'],"Quantity":line['Quantity']})
        print("Petrol")
        print("Price :: Quantity")
        for line in lines_petrol:
            print(line['Price'] ,"Rs::",line["Quantity"],"liter")
        print("Disel")
        print("Price :: Quantity")
        for line in lines_disel:
            print(line['Price']," Rs::",line["Quantity"],"Liter")
            
def fuel_menu():
    obj=Fuel()
    while True:
        print("1: Display \n2: Change price of Petrol\n3: Change price of Disel\n4: Change quantity of Disel\n5: Change quantity of Petrol\n0 : exit")
        count=get_value()
        match count:
            case 0:
                return
            case 1:
                obj.display()
            case 2:
                obj.petrolPriceChange()
            case 3:
                obj.diselPriceChange()
            case 4:
                obj.diselQuantityChange()
            case 5:
                obj.petrolQuantityChange()
            case _:
                print("Invalid")
class Revenue:
  
    
    def __init__(self,s_p=0,t_r=0):
        self.__sell_profit=s_p
        self.__Total_Revenue=t_r
        self.month=0
    def sells(self):
        date=input("Enter Date : ")
        self.month=input("Enter a month : ")
        print("Disel sold ")
        disel_sell=get_value()
        print("Petrol sold ")
        petrol_sell=get_value()
        d_data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv") as file:
            reader=csv.DictReader(file)
            for line in reader:
                d_data.append({"Price":line['Price'],"Quantity":line['Quantity']})
        p_data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\petrol.csv") as file:
             reader=csv.DictReader(file)
             for line in reader:
                p_data.append({'Price':line['Price'],"Quantity":line['Quantity']})
        if(int(p_data[0]['Quantity'])>=petrol_sell and int(d_data[0]['Quantity'])>=disel_sell):
         self.__sell_profit=(int(p_data[0]['Price']))*petrol_sell+(int(d_data[0]['Price']))*disel_sell
         d_data[0]['Quantity']=int(d_data[0]['Quantity'])-disel_sell
         p_data[0]['Quantity']=int(p_data[0]['Quantity'])-petrol_sell
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Petrol.csv","w") as file:
            file.write(f"Price,Quantity\n")
            for line in p_data:
                 file.write(f"{line['Price']},{line['Quantity']}\n")
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv","w") as file:
            file.write(f"Price,Quantity\n")
            for line in d_data:
                file.write(f"{line['Price']},{line['Quantity']}\n")
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Revenue.csv","a") as file:
            file.write(f"{date},{self.__sell_profit}\n")
        else :
            print("Invaild")
            return
        print("Record updated")
    def total_revenue(self):
        self.__Total_Revenue=0
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Revenue.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                self.__Total_Revenue+=int(line['Revenue'])
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\total_Revenue.csv","a") as file:   
            file.write(f"{self.month}, {self.__Total_Revenue}\n")
    def display(self):
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Revenue.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            print("Date :: Money")
            for line in reader:
                print(line['Date'],line['Revenue'],"Rs")

        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\total_Revenue.csv") as file:   
            reader=csv.DictReader(file)     
            print("Month :: Total Revenue")
            for line in reader:
                print(line['Month'],line["Total_Revenue"])
def Revenue_menu():
     obj=Revenue()
     while True:
        print("1: Display \n2: Add total Revenue\n3: Adds daily sells\n0 : exit")
        count=get_value()
        match count:
            case 0:
                return
            case 1:
                obj.display()
            case 2:
               obj.total_revenue()
            case 3:
               obj.sells()
            case _:
                print("Invalid")

class Employee(ABC):
    @abstractmethod
    def add_employee(self):
       pass
    @abstractmethod
    def display_specific(self):
        pass
    @abstractmethod
    def display_all(self):
        pass
    @abstractmethod
    def update_record(self):
        pass
class labor(Employee):
    
    def add_employee(self):
        id=input("ID : ")
        name=input("Full name : ")
        role=input("Enter role : ")
        salary=int(input("Salary : "))
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv","a") as file:
            file.write(f"{id},{name},{role},{salary}\n")
    def display_specific(self):
        x=input("Enter id : ")
        flg=False
        data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})  #Id,Name,Role,Salary
        for line in data:
            if line['Id'] ==x:
                print("Founded",line['Name'],line['Role'],line['Salary'])
                flg=True
                break
        if not flg:
            print("Not founded : ")
    def display_all(self):
        data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})
        for line in data:
            print(line['Id'],line['Name'],line['Role'],line['Salary'])
    def update_record(self):
        print('1 : update salary\n2 : delete record\n0:exit')
        count=int(input("Enter value : "))
        data=[]
        if count==0:
          return
        elif count ==1:
         x=input('Enter Id : ')
         sal=int(input("Enter Salary : "))
         flg=True
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})
         for i,line in enumerate(data):
             if line['Id']==x:
                 data[i]["Salary"]=str(sal)
                 with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv","w") as file:
                    file.write(f"Id,Name,Role,Salary\n")
                    for line in data:
                        file.write(f"{line['Id']},{line['Name']},{line['Role']},{line['Salary']}\n")
                        print("Updated ")
                        flg=False
         if flg:
             print("Updated ")
         else :
             print('Not founded')
        elif count==2:
         x=input('Enter Id : ')
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                if line['Id'] !=x:
                 data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv","w",newline="") as file:
             writer=csv.DictWriter(file,fieldnames=["Id","Name","Role","Salary"])
             writer.writeheader()
             writer.writerows(data)
         
class Manager(Employee):
    
    def add_employee(self):
        id=input("ID : ")
        name=input("Full name : ")
        salary=int(input("Salary : "))
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv","a") as file:
            file.write(f"{id},{name},Manager,{salary}\n")
     
    def display_specific(self):
        x=input("Enter id : ")
        flg=False
        data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})  #Id,Name,Role,Salary
        for line in data:
            if line['Id'] ==x:
             print("Founded",line['Name'],line['Role'],line['Salary'])
             flg=True
             break
        if not flg:
            print("Not founded : ")
    def display_all(self):
        data=[]
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})
        for line in data:
            print(line['Id'],line['Name'],line['Role'],line['Salary'])
    def update_record(self):
        print('1 : update salary\n2 : delete record\n0:exit')
        count=int(input("Enter value : "))
        data=[]
        if count==0:
          return
        elif count ==1:
         x=input('Enter Id : ')
         sal=int(input("Enter Salary : "))
         flg=True
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})
         for i,line in enumerate(data):
             if line['Id']==x:
                 data[i]["Salary"]=str(sal)
                 with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv","w") as file:
                    file.write(f"Id,Name,Role,Salary\n")
                    for line in data:
                        file.write(f"{line['Id']},{line['Name']},{line['Role']},{line['Salary']}\n")
                       
                        flg=False
         if flg:
             print("Updated ")
         else:
             print("Not found")
        elif count==2:
         x=input('Enter Id : ')
         flg =False
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                if line['Id'] !=x:
                 data.append({"Id":line['Id'],"Name":line['Name'],"Role":line['Role'],"Salary":line['Salary']})
                else :
                    flg=True
         with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv","w",newline="") as file:
             writer=csv.DictWriter(file,fieldnames=["Id","Name","Role","Salary"])
             writer.writeheader()
             writer.writerows(data)
         if flg:
              print("Deleted")
         else:
             print("Not founded")
def manger_menu():
    obj=Manager()
  
    while True:    
        print("1 : Add record\n2: Display specific \n3: Display All\n4: Update Record\n0 : exit  ")
        count=int(input("Enter Value ")) 
        match count:
            case 1:
                obj.add_employee()
            case 2:
                obj.display_specific()
            case 3:
                obj.display_all()
            case 4:
                obj.update_record()
            case 0:
                return
            case _:
                print("Invalid")
def labor_menu():
    obj=labor()
    
    while True:   
        print("1 : Add record\n2: Display specific \n3: Display All\n4: Update Record\n0 : exit  ")
        count=int(input("Enter Value "))  
        match count:
            case 1:
                obj.add_employee()
            case 2:
                obj.display_specific()
            case 3:
                obj.display_all()
            case 4:
                obj.update_record()
            case 0:
                return
            case _:
                print("Invalid")


class Business:
    def display(self,path,path2):
           with open(path) as file:
               reader=csv.DictReader(file,skipinitialspace=True)
               print("Date","Month","Income")
               for line in reader:
                   
                   print(line['Date'],line['Month'],line['Income']+" Rs")
           with open(path2) as file:
                reader=csv.DictReader(file,skipinitialspace=True)
                print("Date","Month","Expenses")
                for line in reader:
                    print(line["Date"],line['Month'],line['Expenses']+ " Rs")
    def add_income(self,path):
        date=input("Enter Date : ")
        month=input("Enter Month : ")
        income=input("Enter Income :")
        with open(path,"a",newline="") as file:
           writer=csv.DictWriter(file,fieldnames=["Date","Month","Income"])
           writer.writerow({"Date":date,"Month":month,"Income":income})
           
    def add_expenditure(self,path):
        date=input("Enter Date : ")
        month=input("Enter Month : ")
        expenses=input("Enter Expenditure :")
        with open(path,"a",newline="") as file:
           writer=csv.DictWriter(file,fieldnames=["Date","Month","Expenses"])
           
           writer.writerow({"Date":date,"Month":month,"Expenses":expenses})
class Car_Wash(Business):
    def display(self):
        path=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Car_Wash_income.csv"
        path2=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Car_Wash_expenditure.csv"
        super().display(path,path2)
    def add_income(self):
        path=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Car_Wash_income.csv"
        super().add_income(path)
        
    def add_expenditure(self):
       path=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Car_Wash_expenditure.csv"
       super().add_expenditure(path)
class Shop(Business):
    def display(self):
        path1=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Shop_income.csv"
        path2=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Shop_expenditure.csv"
        super().display(path1,path2)
    def add_income(self):
       path=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Shop_income.csv"
       super().add_income(path)
       
    def add_expenditure(self):
       path=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Shop_expenditure.csv"
       super().add_expenditure(path)
def shop_menu():
    obj=Shop()
    while True:
        print("1: Display \n2: Add_income\n3:Add expenses\n0: exit ")
        count=int(input())
        
        match count:
            case 1:
                obj.display()
            case 2:
                obj.add_income()
            case 3:
                obj.add_expenditure()
            case 0:
                return
            case _:
                print("Invalid")    
                
def car_wash_menu():
    obj=Car_Wash()
    while True:
        print("1: Display \n2: Add_income\n3:Add expenses\n0: exit ")
        count=int(input())
       
        match count:
            case 1:
                obj.display()
            case 2:
                obj.add_income()
            case 3:
                obj.add_expenditure()
            case 0:
                return
            case _:
                print("Invalid")    


class Admin:
    def add_admin(self):
        while True :
            email=input("Enter email : ").strip()
            password=input("Enter a password : ").strip()
            if not re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email) :
                print("Invalid ")
                continue
            if not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password) :
                print("Enter stronge or alternate password ")
                continue
            
            with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\admin.csv","a",newline="") as file:
                file.write(f"{email},{password}\n")
            print("Added successfully")
            break
    def delete_admin(self):
        data=[]
        flg=True
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\admin.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append(line)
        email=input("Enter email : ")
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\admin.csv","w") as file:
            file.write(f"Email,Password\n")
            for line in data:
                if line['Email'] !=email:
                    file.write(f"{line['Email']},{line['Password']}\n")
                else :
                    print("Deleted")
                    flg=False
        if flg:
            print('Not founded')
        
                    
    def change_password(self):
        data=[]
        flg=True
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\admin.csv") as file:
            reader=csv.DictReader(file,skipinitialspace=True)
            for line in reader:
                data.append(line)
        email=input("Enter a email : ")
        new_password=input("Enter new password ")
        for i,line in enumerate(data):
            if email==line["Email"] :
                data[i]["Password"]=new_password
                flg=False
        with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\admin.csv", "w",newline="") as file:
            
            writer=csv.DictWriter(file,fieldnames=["Email","Password"])
            writer.writeheader()
            writer.writerows(data)
        if  flg:
            print("Not founded ") 
def admin_menu():
    obj=Admin()
    while True:
        print("1: Add Admin\n2: Delete Admin \n3: Change Password\n0: exit")
        count=int(input())
        match count:
            case 1:
                obj.add_admin()
            case 2:
                obj.delete_admin()
            case 3:
                obj.change_password()
            case 0:
                return
            case _:
                print("Invalid")

def display_report(path):
    with open(path) as file:
       
        for line in file:
            print(line.rstrip())
            
    print()
def report() :
   print("\t\tReport")
   path0=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\total_Revenue.csv"
   path1=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Revenue.csv"
   
   path2=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Petrol.csv"
   path3=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Disel.csv"
   
   path4=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Shop_income.csv"
   path5=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Car_Wash_income.csv"
   
   path6=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Manager.csv"
   path7=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\employee.csv"
   
   path8=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Shop_expenditure.csv"
   path9=r"C:\Users\sameer hussain\Desktop\extra\petrolpump\Car_Wash_expenditure.csv"
   print("Total Revenue :: ")
   display_report(path0)
   print("Daily Petrol,Disel Revenue")
   display_report(path1)
   print("Petrol : ")
   display_report(path2)
   print("Disel  : ")
   display_report(path3)
   print("Shop_Income : ")
   display_report(path4)
   print("Car_Wash_Income : ")
   display_report(path5)
   print("Managers record :")
   display_report(path6)
   print("Employee records : ")
   display_report(path7)
   print("Shop Expenditure : ")
   display_report(path8)
   print("Car_Wash_Expenditure :")
   display_report(path9)
   

def main():
    while True:
       email=input("Enter a email : ")
       password=input("Enter a password : ")
       flg=False
       with open(r"C:\Users\sameer hussain\Desktop\extra\petrolpump\admin.csv") as file:
           confrim=csv.reader(file,skipinitialspace=True)
           for em,pas in confrim:
               if em==email and pas==password:
                   print("\t\tWellcome\n")
                   flg=True
                   break
       if(flg) :
            break
       else :
            print("Invalid Email or Password")
               
    while True:
        print("1 : Add Admin\n2 : fuel\n3: Revenue\n4 : Manger\n5: Labor\n6: Shop\n7: Car Wash\n8: report \n0 : exit ")
        count=get_value()
        match count:
            case 1:
                admin_menu()
    
            case 2:
                 fuel_menu()
            case 3:
                 Revenue_menu()
            case 4:
                manger_menu()
            case 5:
                labor_menu()
            case 6:
                shop_menu()
            case 7:
                car_wash_menu()
            case 8:
                report()
            case 0:
                break
            case _ :
                print("Invaild")
        
       
            
    
if __name__=="__main__":
    main()
        