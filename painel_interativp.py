fila_espera=["senha 01", "senha 02," "senha 03", "senha 04"]
senha_atual = 0
while senha_atual < len(fila_espera):
    print("\n==========")
    print(f"senha atual:{fila_espera[atual -1]}")
    if senha_atual > 0:
        print(f"senha anterior :{fila_espera[senha_atual -1]}")
    else:
        print(f"senha anterior: nenhuma(primeiro atendimento)")
print("="*10)
if senha_atual -1 < len(fila_espera):
    print(f"Próximo da fila:{fila_espera[senha_atual -1]}")
 else:
    print(f"fila vazia! Não ha mais senha.")   


