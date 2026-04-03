#7)შექმენით sum ფუნქციის იდენტური ვარიანტი (sum ფუნქციას გადაეცემა ინტეჯერების სია და გამოაქ ამ ინტეჯერების ჯამი)

def my_sum(numbers):
    total=0
    for number in numbers:
        total += number
        return total
    