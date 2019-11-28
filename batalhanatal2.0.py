import random
def cria_tab(n):
    tab = []
    for _ in range(n):
        line = []
        for __ in range(n):
            line.append('\u2585')
        tab.append(line)
    return tab

def print_tab(tab):
    print(' '.join([str(i).center(2) for i in range(len(tab))]))
    for line in tab:
        print('  '.join(line))

print_tab(cria_tab(20))

def p_barco(tab, linha, coluna, barco, posição='h'):
    if posição == "h": 
        for i in range(int(barco)):  
            if tab[coluna][linha+ i] != '\u2585':

                for i in range(int(barco)):
                    if tab[coluna][linha+i] == barco:
                    	tab[coluna][linha+i] = '\u2585'

                print('Você não pode colocar seu barco aqui')
                break

            else:
            	tab[coluna][linha+i] = barco    

    elif posição== "v":
        for i in range(int(barco)):
            if tab[coluna + i][linha] != '\u2585':

                for i in range(int(barco)):
                    if tab[coluna+i][linha] == barco:
                    	tab[coluna+i][linha] = '\u2585'

                print('Parceiro ai não dá pra colocar barco')

                break
            else: tab[coluna+i][linha] = barco   

    return tab
	
def verifica_p_barco(barco):
	while True:
		linha= int(input("Digite a fileira:"))
		coluna= int(input("Digite a coluna:"))
		posição= str(input("Digite a direção h/ v:"))
		
		if posição== 'h' or  posição == 'v':
			if not coluna in range(0,19) or  linha not in range(0,19):
				print('Não é um valor válido') 
			else:
				
				if coluna + int(barco) < 20 or  linha + int(barco) < 20 :
					return (int(linha-1),int(coluna-1),posição)
				else:
					print('Não pode colocar seu barco ai amigão')

		else:
			print(posição, 'Não e válido como posição') 
			
def missil(tab, linha, coluna):
	if tab[int(linha)][int(coluna)] == '\u2585':
		print("Você errou tente novamente")
		return tab
	else:
		print("Acertou")
 

def comp(barco = 0):
	while True:	
		linha = random.randint(0,19)
		coluna = random.randint(0,19)
		posição = random.choice(['h', 'v'])
		if coluna + int(barco) < 20 or  linha + int(barco) < 20 : 
			return (int(linha),int(coluna),posição)
			
tab1= cria_tab(20)
tab2 = cria_tab(20)
tab3 = cria_tab(20)

embarcações = {"barco de patrulha":'2',"submarino":'3',"destroyer":'3',"encouraçado":'4',"porta-avião":'5'}
embarcações1 = ["barco de patrulha","submarino","destroyer","encouraçado","porta-avião"]

for i in range(1):
    print("Jogador 1:")
    print_tab(tab1)
    print(embarcações1[i])
    barco =  embarcações[embarcações1[i]]

    verific= verifica_p_barco(barco)
    p_barco(tab1,verific[0],verific[1], barco,verific[2])
    print_tab(tab1)

for i in range(5):
	barco =  embarcações[embarcações1[i]]
	computador = comp(barco)
	p_barco(tab2,computador[0],computador[1],barco,computador[2])
		
while tab1 != tab3 or tab2 != tab3:

    print("Jogador 1:")
    print_tab(tab1)
    tab2 = missil(tab2,linha = str(input(" Digite a coluna")), coluna = str(input("Digite a Fileira:")))
    print('\n')
    print("Jogador 2:")
    computador= comp()
    tab1 =missil(tab1,linha= str(computador[0]), coluna= str(computador[1]))
    print('\n')

if tab1 == tab3:
    print("Parabéns computador vc é um gênio")
else:
    print("Ganhou na sorte amigão")

		
	
		
	
	
