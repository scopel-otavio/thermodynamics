"""
Resolução de questão #3806820 (CESGRANRIO - CEF/Engenheiro Mecânico)
Primeira Lei da Termodinâmica

Um engenheiro projeta um atuador pneumático (sistema pistão-cilindro) para uma linha de montagem. O sistema deve realizar trabalho ao expandir o ar (gás ideal) para empurrar uma peça. Durante a expansão, o sistema é aquecido para manter a pressão constante. Para essa solução, adotou-se o modelo de um gás ideal contido em um cilindro com pistão que sofre uma expansão isobárica reversível a uma pressão constante de P = 200 kPa. O volume inicial do gás é 0,5 m3, e o final, 1,5 m3. Durante esse processo, o gás recebe Q = 350 kJ de calor.

 
Qual é a variação da energia interna do gás durante essa expansão, em kJ?

"""


# Propriedaes
# estado A
pressao_A = 200     # kPa
volume_A = 0.5      # m³

volume_B = 1.5      # m³

calor_entra = 350   # kJ

# Primeira Lei da termodinamica
# dU = Q - W
# W = P(V2 - V1)
trabalho_sai = pressao_A * (volume_B - volume_A)

energia_intera = calor_entra - trabalho_sai

print(f"A variação da energia intera é {energia_intera:.2f} kJ")


# ...para um gás idela
# P1 * V1 / T1 = P2 * V2 / T2
