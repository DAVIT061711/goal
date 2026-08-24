#4)პითონის გაშვების გარეშე კომენტარის სახით დაწერე რას გამოიტანს თითოეული პრინტი

A = {1, 2, 3, 4}, B = {3, 4, 5, 6}

print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
print(A.symmetric_difference(B))


# intersection აბრუნებს საერთო ელემენტებს
print(A.intersection(B))           # გამოიტანს: {3, 4}

# union აერთიანებს ორივე სეტის ელემენტებს დუბლიკატების გარეშე
print(A.union(B))                  # გამოიტანს: {1, 2, 3, 4, 5, 6}

# difference აბრუნებს ელემენტებს, რომლებიც არის A-ში, მაგრამ არ არის B-ში
print(A.difference(B))             # გამოიტანს: {1, 2}

# symmetric_difference აბრუნებს ელემენტებს, რომლებიც მხოლოდ ერთ-ერთ სეტშია (გარდა საერთოესი)
print(A.symmetric_difference(B))   # გამოიტანს: {1, 2, 5, 6}


