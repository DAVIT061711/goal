#2)მომხმარებელს შემოატანინე რაიმე ცხოველები და ჩასვი ისინი სეტში, შემდეგ მთლიანად გაასუფთავე ეს სეტი
animals = set()

user_input = input("შემოიტანე რამდენიმე ცხოველი (მძიმით გამოყოფილი): ")
for animal in user_input.split(","):
    animals.add(animal.strip())
print("სეტი გასუფთავებამდე:", animals)

animals.clear()
print("სეტი გასუფთავების შემდეგ:", animals)


