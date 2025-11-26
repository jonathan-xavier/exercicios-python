nome_completo = "jonathan xavier"
nome_completo_aspas = """sdddd 
dv sasssssssskskkskskssk"""

nome_completo_quebra = "Jonathan \
xavier"


#formatacao

print("nome completo(1a forma): ", nome_completo_quebra)
print("nome completo(2a forma): "+ nome_completo_quebra)
print("nome completo(3a forma): " + "jonathan" + "xavier")
print("nome completo(4a forma): " + "jonathan" , "xavier")
print(f"nome completo(5a forma): {nome_completo}")
print("nome completo(6a forma): {}".format(nome_completo))
print("nome completo (7a formaa): %s" % (nome_completo))

#upper
print(nome_completo.upper())

print(nome_completo[2])
