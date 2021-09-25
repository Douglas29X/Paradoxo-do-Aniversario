
numero_de_pessoas = (int(input
	('Digite o número de pessoas que estão na sala nesse exato momento:\n')))

def calcula_aniversario(n):
	chance = (1/365) ** n
	for fatorial in range((366 - n), 366):
		chance*= fatorial
	return (1 - chance) * 100

calculo = calcula_aniversario(numero_de_pessoas)

print('\n\nA chance de duas pessoas, nessa sala, fazerem'
	f' aniversário no mesmo dia é de {calculo:.2f}%')

print(f'Lembrando que esse é o resultado aproximado.\n\nA probabilidade original é de {calculo}%\n')
