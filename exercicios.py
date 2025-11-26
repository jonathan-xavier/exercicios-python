#26- crie uma varivavel com valor inicial  0, enquanto o vlaor dessa variavel for 
# igual ou menos que 10, exiba em tela o proprio valor da variavel . 
# a cada execucao a mesma deve ter o seu valor atualizado, incrementado em 1 unidade

# initial = 0
# while initial <= 10:
#     print(initial)
#     initial += 1

#27- crie um strutura de repeticao que percorre a string nikola tesla exibindo 
# em tela letra por letra esse nome

# name = 'nikola tesla'
# for i in name:
#     print(i)

#28- crie uma lista com 8 elementos de uma lista de compras de supermercado, 
# por meio de um laco de repeticao for liste individualmente 
# cada um dos itens dessa lista

# items = ["arroz", "feijao", "macarrao", "biscoito","coca-cola",
#           "queijo", "pao","leite"]

# for i in items:
#     print(i)

#29- crie um programa que le um valor de inicio e um valor de fim, exibindo em 
# tela a contagem dos numero dentro desse intervalo.

# inicio = int(input("valor inicial: "))
# fim = int(input("valor final: "))

# for value in range(inicio, fim + 1):
#     print(value)

#30- crie um programa que faz uma contagem de 0 a 20, exibindo os 
# numeros pares.

# for value in range(0, 21):
#     if value % 2 == 0:
#         print(value)

#31- crie um programa que realiza a progressao aritimetica de 20 elementos, 
# com primeiro termo e razão definidos pelo usuário.
#nao entendi o exercicio
# initial_value = int(input("type a initial value: "))
# step_value = int(input("type a step: "))

# pa = initial_value + 19 * step_value
# for value in range(initial_value, pa + step_value, step_value):
#     print(value)

#32- crie um programa que exibe em tela a tabuada de um determinado
#  numero fornecido pelo usuario.

# numero = int(input("informe um numero: "))

# for i in range(1, 11):
#     print(f"{numero} X {i} = ", numero * i)

#33- crie um programa que realiza a contagem regressiva de 20 segundos
# from time import sleep

# for value in range(20, -1, -1):
#     print(value)
#     sleep(1)

#34- cria um programa que realiza a contagem de 1 até 100 usando impares,
# e exiba quantos numeros impares foram encontrados e a soma deles
# count = 0
# soma = 0
# for value in range(1, 100 + 1):
#     if not value % 2 != 0:
#         print(value)
#         soma += value
#         count += 1 


# print(f"foram encontrados {count} numeros impares!")
# print(f"a soma total deles é: {soma}")

#35- crie um programa que pede ao usuario que digite um numero qualquer, e retorne 
# se esse numero é primo ou nao, caso nao, retorne tambem quantas vezes esse numero
# é divisivel se é primo ele é divisivel por 1 ou por ele mesmo

# numero = int(input("digite um numero: "))
# count = 0
# for i in range(1, numero + 1):
#     if numero % i == 0:
#         count += 1

# if count == 2:
#     print(f"o numero {numero} é primo e é divisivel por ele mesmo")       
# else:
#     print(f"o numero {numero} não é primo! é divisivel {count} vezes!")  

#36- crie um programa que pede que o usuario digite um nome ou uma frase, verifique se esse 
#conteudo digitado é um palindromo ou nao, exibindo em tela o resultado.

# nome = str(input("digite um nome qualquer: ")).strip().upper()
# reversed_name = ""

# splitted = nome.split(" ")
# if len(splitted) > 1:
#     for word in splitted:
#         reversed_name += word[::-1]
#         " ".join(reversed_name)
# else:
#     reversed_name = nome[::-1]

# if reversed_name == nome:
#     print("é um palindromo")
# else:
#     print("não é um palindromo")    

#37- declare uma variavel que por sua vez recebe um nome digitado pelo usuario, em 
# seguida, exiba em tela uma mensagem de boas-vindas que incorpora o nome 
# anteriormente digitado, fazendo uso de f'string.

# name = str(input("informe o seu nome: ")).strip()

# print(f"Bem vindo(a), {name}! ")

#38-  peça para que o usuario digite um numero, 
# diretamente dentro da função print() eleve esse numero ao quadrado, 
# exibindo o resultado incorporado a uma mensagem

# numero = int(input("digite um numero: "))

# print(f"o numero {numero} ao quadrado fica: {numero * 2}")

#39- data a seguinte lista: nomes = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']
# substitua o terceiro elemento da lista por 'jamile'

# nomes = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']

# indice = nomes.index('Daiane')
# nomes[indice] = 'jamile'
# for i in nomes:
#     print(i)

#40- adicione o elemento 'paulo' na lista de nomes


#dessa forma tambem funciona.
# newArray = [
#     *nomes,
#     "Paulo"
# ]

# nomes.append("joao")

# for i in nomes:
#     print(i)


#41- adiciona o elemento 'Eliana' na lista de nomes, especificamente
# na terceira posição da lista.
# nomes = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']

# index = nomes.index('Daiane')
# nomes.insert(index, "Eliana")

# print(nomes)

#42- remova o elemento 'Carlos' da lista
# nomes = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']
# nomes.remove("Carlos")

# print(nomes)
