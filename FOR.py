lista_produtos = ['faca','garfo', 'panela','frigideira','flavorstone']


for prod in lista_produtos:
    print(prod.capitalize())


lista_precos1 = [10,10,200,50,300]

for preco in lista_precos1:
    imposto = preco * 0.1
    print(imposto)


produtos1= {
      'faca':10,
      'garfo':10,
      'panela':20,
      'frigideira':5,
      'flavorstone':15,
}

for produto in produtos1:
    print(produto)
    print(produtos1[produto])



