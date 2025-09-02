'''#dicionario
components = {
    'marca':'nexus',
    'modelo':'prossc4@',
    'preco':'2300$'
}
def funcao(*args):
    print(args)
    for item in args:
        print("\n",item)
funcao(12,14,12312,123,1,3,123,12,1,2,1,213,123)

teste = {}

teste['nome'] = input("Digite um nome: ")
print(teste,"\n")

def criar_dict(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
criar_dict(nome="testnome",idade="testeidade",cidade="testecidade")
'''
#calculo_imposto

def calc_imposto(valor,**kwargs):
    total = 0
    print (kwargs)
    if 'iss' in kwargs:
        total += valor * kwargs['iss']
    if 'pis' in kwargs:
        total += valor * kwargs['pis']
    return total
calc_imposto(1000)