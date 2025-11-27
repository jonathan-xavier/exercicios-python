#range(): intervalo numérico 
#[0,1,2,3,4,5,6,7,8,9]

# print("\n utilizando a funcao range")
# for numero in range(5):
#     print("Numero: ", numero)

#range com len()

# lista = [1,2,3,4,5]
# for i in range(0, len(lista)):
#     print("Indice: ", i)

#enumerate()

lista_enum = ["a", "b", "c"]
# for index in range(0, len(lista_enum)): 
#     print(lista_enum[index], index)
for index, value in enumerate(lista_enum):
     print(f"{index}:{value}")   