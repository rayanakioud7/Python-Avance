with open("text1.txt", 'w+') as f:
    f.write("Bonjour Mes amis\n")
    f.close()

with open("text2.txt", "w+") as file:
    for i in range(100):
        file.write("Bonjour Mes amis\n")
    f.close()

