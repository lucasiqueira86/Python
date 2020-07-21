print('Bom dia')
nome = input ('Qual seu nome?')
print(f'Ficamos felizes em poder te ajudar  {nome}')
ajuda = input ('Voçe gostaria de comprar um celular hoje?')
if ajuda == 'sim':
     celular = input('Otimo, qual celular voçe tem interesse?Temos em nosso estoque A20 E A30')
if celular == 'A20':
    print('Estamos com uma promoção! Apenas hoje ele ira sair por R$1.200,00 em até 12 x sem juros.')
if celular == 'A30':
    print('estamos com uma promoção! Apenas hoje ele ira sair por R$1.600,00 em até 12 x sem juros.')  
else:
    print('Infelizmente não temos esse modelo.')
