#4) მომხმარებელს შემოატანინეთ მისი ასაკი და სახელი, შემოუშვით საიტზე თუ ის იქნება 18 წელზე მეტის ან მისი სახელი იქნება "Andrew"
name = input("enter your name")
age = int(input("enter your age"))
print(age > 18 or name == "andrew")