Name= input("Уважаемый студент НИУ ВШЭ, введите свое имя: ")
Surname= input("Введите свою фамилию: ")
Year= int(input("Введите свой год рождения: "))
print (Name,Surname,Year,sep="_")
Name, Surname = Surname, Name 
Year += 60
print (Name,Surname,Year,sep="_")