with open('vendasloja.txt', 'r') as arquivo:   #lendo arquivo
    texto = arquivo.read()
lista_texto = (texto.split('\n'))

faturamento = 0
lista_texto = lista_texto[1:]#deletando a primeira linha


for linha in lista_texto:
    posicao_pv = linha.find(';') #achando o ;
    valor =float(linha[posicao_pv+1 :])# transformando texto em numero
    faturamento += valor
print(faturamento)



#excluir primeira linha
#para cada linha do meu arquivo eu quero somar o valor depois de ponto e virgula

