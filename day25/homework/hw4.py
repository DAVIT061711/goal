#4)დაწერე ფუნქცია, რომელიც დააბრუნებს მხოლოდ ლუწ რიცხვებს ახალი list-ის სახით
def _even_numbers(numbers_list):
    even_list=[]
    for number in numbers_list:
        if number % 2==0:
            even_list.appent(number)
        return even_list