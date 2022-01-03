"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?
"""
soma = 0
k = 0

while k < 13:
    k += 1
    soma += k

print(f'O valor da variavel soma é de {soma}')

print('-' * 45)

"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na
linguagem que desejar onde, informado um número, ele calcule a sequência de
Fibonacci e retorne uma mensagem avisando se o número informado pertence ou
não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência
ou pode ser previamente definido no código;
"""

numero = int(input("Que numero deseja encontrar: "))
ultimo_valor = 3
penultimo_valor = 2
i = 3

while i <= numero:
    sequencia = ultimo_valor + penultimo_valor
    penultimo_valor = ultimo_valor
    ultimo = sequencia
    i += 1
    if ultimo_valor == numero:
        print('Número encontrado na sequência')
        break
else:
    print('Número não encontrado na sequência')

print('-' * 45)

"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora
,faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à
média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
"""

valores_mensais = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

maior = max(valores_mensais)
print(f'O maior valor do mês foi de {maior}R$')

menor = min(valores_mensais)
print(f'O menor valor do mês foi de {menor}R$')

try:
    while True:
        valores_mensais.remove(0)
except ValueError:
    pass

media = sum(valores_mensais) / len(valores_mensais)
for x in range(len(valores_mensais)):
    if valores_mensais[x] > media:
        print(f"""O valor de {valores_mensais[x]}R$ do dia {x} superou a media
mensal de {media:.2f}R$""")

print('-' * 45)

"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por
estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de
representação que cada estado teve dentro do valor total mensal da
distribuidora.
"""


def calculo_porcentagem(SP, RJ, MG, ES, Outros):
    valor_total = SP + RJ + MG + ES + Outros
    SP_porcentagem = (SP / valor_total) * 100
    RJ_porcentagem = (RJ / valor_total) * 100
    MG_porcentagem = (MG / valor_total) * 100
    ES_porcentagem = (ES / valor_total) * 100
    Outros_porcentagem = (Outros / valor_total) * 100

    print(f'Porcentagem do valor de SP: {SP_porcentagem:.1f}%')
    print(f'Porcentagem do valor de RJ: {RJ_porcentagem:.1f}%')
    print(f'Porcentagem do valor de MG: {MG_porcentagem:.1f}%')
    print(f'Porcentagem do valor de ES: {ES_porcentagem:.1f}%')
    print(f'Porcentagem do valor de Outros Estados: {Outros_porcentagem:.1f}%')


calculo_porcentagem(SP=67.83643, RJ=36.67866, MG=29.22988, ES=27.16548, Outros=19.84953)

print('-' * 45)

"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua
preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

"""

palavra = input('Digite uma palavra: ')
palavra_reversa = palavra[::-1]
print(palavra_reversa)
