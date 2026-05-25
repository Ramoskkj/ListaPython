#simulador_investimento_cdb

dinheiro = float(input("Quanto você quer investir? R$ "))
cdb = float(input("Quantos % do CDI é o CDB? "))

cdi = 14.4

# calcular rendimento
taxa = (cdb * cdi) / 100

# dividir por 12 meses
taxa_mes = taxa / 12

# 6 meses
final = dinheiro

for i in range(6):
    final = final + (final * taxa_mes / 100)

lucro = final - dinheiro

print("\nResultado:")
print("Valor inicial: R$", round(dinheiro, 2))
print("Valor final: R$", round(final, 2))
print("Lucro: R$", round(lucro, 2))
MauricioRamos