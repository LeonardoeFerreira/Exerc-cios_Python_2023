##############################################################################
# Autor: Leonardo Ferreira
# @leonardoeferreira
# Calculando Média em Python
##############################################################################

nota01 = float(input("Digite a nata da unidade 1: "))
nota02 = float(input("Digite a nata da unidade 2: "))
nota03 = float(input("Digite a nata da unidade 3: "))
nota04 = float(input("Digite a nata da unidade 4: "))

media = (nota01 + nota02 + nota03 + nota04 ) / 4

print(f" A media das notas {nota01:.2f},{nota02:.2f},"
      f"{nota03:.2f} e {nota04:.2f} é {media:.2f}")