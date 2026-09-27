"""
Resolução da questão #3806817 (CESGRANRIO - CEF/Engenheiro Mecânico)
Turbina Isentrópica
"""

# Propriedades de entrada na turbina
entalpia_entrada = 3200         # kj/kg
entalpia_saida = 2200           # kj/kg
eficiencia_isentropica = 0.80   # 80%


# n = (h1 - h2) / (h1 - h2s)
# n * (h1 - h2s) = h1 - h2
# h1 - h2s = (h1 - h2) / n
# h2s = h1 - (h1 - h2) / n

# Entalpia isentrópica

entalpia_saida_isentropica = entalpia_entrada - (entalpia_entrada - entalpia_saida) / eficiencia_isentropica

print(f"Entalpia na saída da turbina isentrópica: {entalpia_saida_isentropica:.1f} kj/kg")