#4)დაწერე პროგრამა, რომელიც ამოწმებს რიცხვი არის თუ არა ის ერთდროულად 3-ისა და 5-ის ჯერადი.
number= int(input("enter number"))

if number % 3==0 and number % 5==0:
    print ("this is a multiple of 3 and 5")
else:
    print("this is not multiple of 3 and 5")