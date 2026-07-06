# Entrada de dados para teste
bateria_atual = 14  # Exemplo: número inteiro de 0 a 100
bola_em_jogo = False # Exemplo: True ou False

# Processamento das condições (Lógica Condicional)
if bateria_atual < 15 and bola_em_jogo == True:
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")

elif bateria_atual < 15 and bola_em_jogo == False:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    # Caso Geral: Bateria igual ou acima de 15%
    print("Sistema Trionda operando normalmente. Bateria ok.")
