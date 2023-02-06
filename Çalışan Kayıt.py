import time
number:int
file_names=[]

def Number_Of_Actions():
    number = int(input("Enter Number of Actions to Take: "))


def menu_and_selection():
    print("\tMenu\n1.Adding Employees\n2.Employee Record Update\n3.Delete Employee Record\n4.See All Employees List")

def number_of_transactions(): 
    number_of_transactions= int(input("How Many Transactions Will Be Made: "))
    for i in range(number_of_transactions):
        menu_and_selection()
        selection = str(input("Which Operation Do You Want To Do: "))
        if selection == "1":
            file_name = str(input("Enter File Name: "))
            print("\nCreating File\n")
            time.sleep(3,"Loading...")
            f = open(file_name,mode="x")
            file_names.append(file_names)
            print("File Created")
            employee_code = input("Employee Code: ")
            employee_name = input("Employee Name: ")
            konum = input("Dosya Konumunu Girin: ")# Belge konumunu kullanıcıdan alalım
            dosya = open(konum,mode="r") # belgeyi okuma moduna alalım
            aranan_var_mi = dosya.read().find(employee_name)
            if aranan_var_mi!=-1:
                print("Eklenecek Çalışan Dosyası Mevcut.Tekrar Deneyin.")
                menu_and_selection()
            else:        
                employee_surname = input("Employee Surname: ")
                employee_age = input("Employee Age: ")
                employee_mail = input("Employee E-Mail: ")
                employee_number = input("Employee Phone Number: ")
            print("Transferring Information to File.")
            f.close()
            f = open(file_name,mode = "w")
            f.write("Employee Code: ",employee_code)
            f.write("Employee Name: ",employee_name)
            f.write("Employee Surname: ",employee_surname)
            f.write("Employee Age: ",employee_age)
            f.write("Employee E-Mail: ",employee_mail)
            f.write("Employee Phone Number: ",employee_number)
            time.sleep(3,"Information İs Transferred.")
            f.close()
        else:
            menu_and_selection()

        if selection == "2":
            print(" \n"*50)
            print("Update Operations\n ")
            file_name = str(input("Enter name for update process: "))
            time.sleep(3)
            f = open(file_name,mode = "r")
            name = input("Enter the name of the employee whose information is to be changed: ")
            if (name in file_names) == True:
                f = open(file_name,mode ="w")
                name = file_name
                print(name)
            else:
                print("Hatali İşlem")
            



number_of_transactions()
