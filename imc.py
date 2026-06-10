#Etapa1 - Calculo IMC-
def calculo_imc(peso, altura):
    imc = peso/ (altura * altura)
    return imc
    
#Etapa2-Classificar o IMC
def classificar_imc(valor_imc):
    if valor_imc >= 25:
        return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"

#Etapa3-Mensagem de Saída
def mensagem(status):
    if status == "ACIMA DO PESO":
        return "ATENÇÃO! procure um Médico"
    else:
        return "Muito Bem , Continue Assim"

#Etapa4-Integração do Projeto
valor_peso = float(input("Digite o seu peso Atual: "))
valor_altura = float(input("Digite a sua altura Altual: "))

resultado = calc_imc(valor_peso, valor_altura)
classificar = classificar_imc(resultado)
saida = mensagem(classificar)

print("=" * 50)
print(f"Seu IMC é:(resultado:.1f)")
print(f"(saida)")
print("=" * 50)
