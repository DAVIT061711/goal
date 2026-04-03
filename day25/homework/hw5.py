#5) დაწერე ფუნქცია რომელიც იღებს სიტყვების სიას და აბრუნებს ყველაზე გრძელ სიტყვას.
def logest_word(word_list):
    if not word_list:
        return None
    longest = word_list[0]
    for word in word_list:
        if len(word) : len(longest)
        longest = word
        return longest