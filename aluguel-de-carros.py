from datetime import date
atual = date.today().year
dado = dict()
print(" ALUGUEL DE CARROS ")
atual = date.today().year

dado['nome'] = str(input("Digite seu nome completo: ")).strip().title()
nasc = int(input("Ano de nascimento: "))
dado['idade'] = atual - nasc

dado['cpf'] = int(input("Digite seu CPF: "))
dado['carro'] = str(input("Digite um modelo de carro: ")).strip().upper()
dado['dias'] = int(input("Duração com o veiculo: "))
dado['carteira'] = str(input("Tem CNH? [S/N] ")).strip().upper()
while dado['carteira'] not in 'SsNn':
    dado['carteira'] = str(input("Por favor digite [S/N] se possui CNH: ")).strip().upper()

if dado["carteira"] in "Ss":
    valor = 20 * dado["dias"]
    print("\033[0;32mVocê pagará menos por ter CNH!\033[m")
else:
    valor = 70 * dado["dias"]
    print("\033[0;31mVocê pagará ao dobro por conta de não ter CNH!\033[m")
   
print("="*30)
print("{:^30}".format("RELATORIO"))
print(f"Nome: {dado['nome']}")
print(f"Ano de nascimento: {nasc}")
print(f"Idade: {dado['idade']}")
print(f"CPF: {dado['cpf']}")
print(f"Veiculo: {dado['carro']}")
print(f"CNH: {dado['carteira']}")
print(f"Duração será de {dado['dias']} dias")
print(f"Valor R${valor}")