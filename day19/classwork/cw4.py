#4)შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს თავის გვარს,
#თუ პირველი 5 ასო შენი გვარის პირველი 5 ასოს მსგავსია, დაპრინტე 'almost same' სხვა შემთხვევაში დაპრინტე 'bye'

my_surname= "tsiklauri"
surname=input("Enter your surname")

if surname[:5]== my_surname[:5]:
    print("almost same")
else:
    print("bye")
