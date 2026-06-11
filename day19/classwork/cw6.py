#6)შექმენით სია 5 ელემენტით, შემდეგ მომხმარებელს შემოატანინეთ ორი რიცხვი (start / stop) და sliceing-ის
#მეშვეობით გამოიტანეთ მომხმარებლის რიცხვების მიხედვით სიის ნაწილი (შეამოწმეთ თუ რიცხვები არ არის ვალიდური 
#მაგ: -10000) მაშინ გამოიტანეთ "incorrect index"(ანუ რიცხვები უნდა იყოს ამ 5 ელემენტის ინდექსის დიაპაზონში

my_list=[1,2,3,4,5]
start=int(input("enter your number"))
stop=int(input("enter your number"))

if start >= 0  and stop <= 5:
    print(my_list[start:stop])
else:
    print("incorrect index")


