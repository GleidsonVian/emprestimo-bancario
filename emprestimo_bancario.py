"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
 O programa deve perguntar o valor da casa a comprar,
 o salário e 
 a quantidade de meses a pagar.

 O valor da prestação mensal não pode ser superior a 30% do salário.
 Calcule o valor da prestação como sendo o valor da 
casa a comprar dividido pelo número de meses a pagar.
"""
def emprestimo_bancario():
    valor_da_casa_ao_comprar = float(input('Qual o valor da casa que o senhor deseja comprar? '))
    salario = float(input('Qual o seu salario? '))
    quantidade_de_meses = float(input('Qual a quantidade de meses que o senhor deseja? '))
    
    porcentagem_prestacao = salario * 0.30
    prestacao_mensal = valor_da_casa_ao_comprar / quantidade_de_meses

    if prestacao_mensal > porcentagem_prestacao:
        print('Empréstimo bancário recusado pois o valor da parcela ultrapassa o limite de 30% do seu salário')
        print(f'Valor da prestação: R$ {prestacao_mensal:.2f}')
        print(f'Limite máximo de prestação com base no salário: R$ {porcentagem_prestacao:.2f}')
    else:
        print('Empréstimo bancário aceito')
        print(f'Valor da prestação: R$ {prestacao_mensal:.2f}')
        print(f'Limite máximo de prestação com base no salário: R$ {porcentagem_prestacao:.2f}')
    
    

emprestimo_bancario()

