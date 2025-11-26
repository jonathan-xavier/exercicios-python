myList = [1,2,3,4,5]

first, *_ = myList


# print(myList[4])

#pegar uma parte do array tipo slice do javascript
#the both has the same result

getElements = myList[1:3]
getSinceTheFirstElement = myList[:3]
# print(myList[1:3])


#metodos de lista

#metodo append(): Adiciona um elemento no final da lista. Tipo o push()
myList.append(9)
# print("Apos o append: ", myList)

#metodo index

index = myList.index(5)
print(index)

#metodo insert: insere um elemento em um index especifico

myList.insert(2, 10)
print(myList)

#metodos de delecao



