with open("Table_de_multiplication.txt", "w+") as f:
    for i in range(1,11):
        f.write(f"La table de {i}\n")
        for j in range(1,11):
            f.write(f"{i} X {j} =  {i*j}\n")
        f.write("\n")
    f.close()