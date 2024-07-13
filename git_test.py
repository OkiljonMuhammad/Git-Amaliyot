""" “raqamlar” nomli tekst fayl ichiga 1 dan 10 gacha 
sonlarni kiritib, ularning yig'indisini ekranga 
chiqaruvchi dastur yarating."""
with open("git_text.txt", "r") as file:
    # file.write("1 2 3 4 5 6 7 8 9 10")
    numbers = file.read().split(' ')
    yigindi = 0
    for number in numbers:
        yigindi = yigindi + int(number)

    print(yigindi)
