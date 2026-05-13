#Criando um Teste com pontuação--
print("Teste os seus Conhecimentos sobre Ciências🧪")
ponto = 0
#--Qestão 1--
print("Qual é a formula da Água?🚰")
print("a-H20 \n b-C02 \n c-AL")
resposta1 = input("Digite a respposta:").lower()
if resposta1 == "a":
    print("Resposta Correta🟢")
    ponto = ponto =1
else:
    print("Você Errou🔴")
#Questão 2
print("O sol é:☀️")
print("a-satélite \n b-estrela \n c-astéroide")
resposta2 = input ("Digite a Resposta: ").lower()
if resposta2 == "b":
    print("Resposta Correta🟢")
    ponto = ponto +1
else:
    print("Você Errou🔴")
print("Fim do Questionário")
print(f"Sua pontuação foi: {ponto}")