user = {"nome": "joão", "idade": 31, "cidade": "jaboatão dos guararpes"}
user["nome"] = "jonathan"

print(user["nome"])

del user["nome"]
print(user)

#métodos: keys(), values(), items()
chaves = list(user.keys())

# print("chaves do dicionario:", chaves[0])
valores = list(user.values())
# print("valores dos dicionarios: ", valores[0])

itens = list(user.items())
print("pares chave-valor do dicionário: %s = %s " % (itens[0][0], itens[0][1]))