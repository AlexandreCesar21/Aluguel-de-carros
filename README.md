<h1>Aluguel de Carros</h1>

<p>Este projeto é um programa em Python que gerencia o processo de aluguel de carros, calculando o valor do aluguel com base em fatores como a posse ou não de uma Carteira Nacional de Habilitação (CNH) e a duração do aluguel.</p>



<h2>Funcionalidades</h2>
<p>• <b>Solicitação de informações do cliente, como:</b></p>
<p>• Nome completo</p>
<p>• Ano de nascimento</p>
<p>• CPF</p>
<p>• Modelo do carro a ser alugado</p>
<p>• Duração do aluguel em dias</p>
<p>• Confirmação sobre a posse de CNH</p>

<p>• <b>Cálculo dinâmico do valor do aluguel:
</b></p>
<p>• Clientes com CNH pagam menos (R$20/dia).</p>
<p>• Clientes sem CNH pagam o dobro (R$70/dia).</p>
<p>• Geração de um relatório final com todos os dados do cliente e o valor total do aluguel.
</p>

<h2>Fluxo do Programa</h2>
<p>1. <b>Entrada de Dados:</b> O programa solicita as informações do cliente, validando as respostas para a pergunta sobre a posse de CNH.</p>


<p>2. <b>Cálculo do Valor:</b></p>
<p>• Caso o cliente possua CNH, o valor total é calculado a R$20 por dia.</p>
<p>• Caso contrário, o valor é calculado a R$70 por dia, com uma mensagem de alerta.</p>


<p>3. <b>Exibição do Relatório:</b> O relatório exibe:</p>
<p>• Dados do cliente</p>
<p>• Modelo do carro</p>
<p>• Duração do aluguel</p>
<p>• Valor total a ser pago.</p>


<h2>Código</h2>
<h3><b>Requisitos</b></h3>
<p>Certifique-se de estar utilizando o Python 3.6 ou superior, já que o programa utiliza o módulo <code>datetime</code>.</p>

<h3><b>Trechos Principais do Código</b></h3>
<p><b>Importação e Configuração</b></p>
<code>from datetime import date
atual = date.today().year
dado = dict()</code>

<p><b>Coleta de Dados</b></p>
<code>dado['nome'] = str(input("Digite seu nome completo: ")).strip().title()
nasc = int(input("Ano de nascimento: "))
dado['idade'] = atual - nasc

dado['cpf'] = int(input("Digite seu CPF: "))
dado['carro'] = str(input("Digite um modelo de carro: ")).strip().upper()
dado['dias'] = int(input("Duração com o veiculo: "))
dado['carteira'] = str(input("Tem CNH? [S/N] ")).strip().upper()
while dado['carteira'] not in 'SsNn':
    dado['carteira'] = str(input("Por favor digite [S/N] se possui CNH: ")).strip().upper()
</code>

<p><b>Cálculo e Condicional</b></p>
<code>if dado["carteira"] in "Ss":
    valor = 20 * dado["dias"]
    print("\033[0;32mVocê pagará menos por ter CNH!\033[m")
else:
    valor = 70 * dado["dias"]
    print("\033[0;31mVocê pagará ao dobro por conta de não ter CNH!\033[m")
</code>

<p><b>Geração do Relatório</b></p>
<code>print("="*30)
print("{:^30}".format("RELATORIO"))
print(f"Nome: {dado['nome']}")
print(f"Ano de nascimento: {nasc}")
print(f"Idade: {dado['idade']}")
print(f"CPF: {dado['cpf']}")
print(f"Veiculo: {dado['carro']}")
print(f"CNH: {dado['carteira']}")
print(f"Duração será de {dado['dias']} dias")
print(f"Valor R${valor}")
</code>

<h2><b>Como Executar</b></h2>

<p>1. Salve o código em um arquivo com extensão .py, por exemplo: <code>aluguel_de_carros.py.</code> 
</p>
<p>2. Execute o arquivo em um ambiente Python, como o terminal ou IDEs como PyCharm ou VS Code.
</p>
<p>3. Siga as instruções exibidas na interface para fornecer os dados do cliente.
</p>

<h2><b>Melhorias Futuras</b></h2>
<p>• Adicionar validações mais robustas para entrada de dados (ex.: formatos de CPF e ano de nascimento).</p>
<p>• Expandir o cálculo do valor para incluir modelos de carros com preços diferentes.</p>
<p>• Criar uma interface gráfica usando bibliotecas como Tkinter ou PyQt.</p>
<p>• Salvar os dados do aluguel em um banco de dados ou arquivo JSON.</p>




