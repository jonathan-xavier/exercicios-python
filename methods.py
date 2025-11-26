nome = "jonathan"
nome.count("a")
nome.find("a") #posicao

nome.encode() #está em byte. deixa um b na frente.
nome.encode().decode() #decodifica
anotherName = nome.replace("a", "u")

#tipo o includes do javascript
hasLetterInName = "x" in nome
#print(hasLetterInName)

phone = "(81)9991294-17"
phoneReplaced = phone.replace("(", "").replace(")", "")

#split e join

fullName = "jonathan xavier rodrigues"
nameToJoin = "maria"
aaa = fullName.split(" ")
bbb = [
    *aaa,
    nameToJoin
]

nameSepareted = "-".join(fullName)
nameSeparetedSpace = " ".join(bbb)

#substituir os caracteres das pontas strip, rstrip, lstrip
bName = "xJonathan xavierx"
bothSides = bName.strip("x")
right = bName.rstrip("x")
left = bName.lstrip("x")

#comparadores in not in startsWith
bName.startswith("xj")
startsWithVar = bName.lower().startswith("xj")
includes = not ("han" in bName)
print(includes)


