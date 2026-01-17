#5) დაწერე პროგრამა, რომელიც ამოწმებს პაროლის სიგრძეს.
#თუ პაროლი 8 სიმბოლოზე ნაკლებია → „სუსტი პაროლი“,
#წინააღმდეგ შემთხვევაში → „კარგი პაროლი“.
password =input("enter your password")
if len(password) < 8:
    print("exact password")
else:
    print("good pasword")