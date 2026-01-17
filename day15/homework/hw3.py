#3)მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის სახელი ემთხვევა თქვენს სახელს
#და ასევე მისი ასაკი ემთხვევა თქვენს სახელს, დაბეჭდეთ "Twins" სხვა შემთხვევაში "Not Twins".
name1=input("enter your name")
name2=input("enter your name")
age1=int(input("enter your age"))
age2=int(input("enter your age"))

if name1==name2 and age1==age2:
    print("Twins")
else:
    print("Not Twins")