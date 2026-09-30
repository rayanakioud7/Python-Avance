L3 =[5,8,9,6,2]
for l in L3:
    print(l)
somme = sum(L3)
print(f"La somme: {somme}")

produit = 1
for l in L3[2:5]:
    produit =produit * l 

print(f"le Produit: {produit}")

print(f"Le max={max(L3)}, Le min={min(L3)}")

count = 0
for l in L3:
    if l%3 == 0:
        count+=1
print(f"le nombre des multiples de 3 present dans la liste {count}")

for i in range(len(L3)-1,-1,-1):
    print(L3[i])