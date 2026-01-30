
#6)შექმენით რიცხვების სია, შემდეგ ამ სიაში დაითვალეთ მხოლოდ ლუწი რიცხვების ჯამი (გამოიყენეთ % ოპერატორი)

numbers=[2,5,8,3,10,7,4]
even_sum= 0 
for num in numbers:
    if num % 2==0:
        even_sum+=num
        print(even_sum)