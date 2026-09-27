"""
#2700950 CESGRANRIO - 2023 - Profissional Transpetro de Nível Superior (TRANSPETRO)/Engenharia/Mecânica
  
Um gás perfeito experimental é utilizado em uma compressão adiabática reversível, saindo da pressão (absoluta) P1 = 100 kPa, temperatura T1 = 293 K e atingindo a pressão (absoluta) de P2 = 400 kPa. Sabendo-se que a razão entre os calores específicos (k = cp / cv) vale 2, a temperatura final, em K, é igual a
"""

# Propriedades do estado 1
pressao_1 = 100         # kPa
temperatura_1 = 293     # K

pressao_2 = 400         # kPa


# razão entre os calores específicos (k = cp / cv)
k = 2


# T2 / T1 = (P2 / P1) ^ ( k - 1 / k)

temperatura_2 = temperatura_1 * (pressao_2 / pressao_1) ** ( (k-1)/k)

print(f"A temperatura final é {temperatura_2:.2f} K")