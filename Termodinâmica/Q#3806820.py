"""
Resolução de questão #3806820 (CESGRANRIO - CEF/Engenheiro Mecânico)
Ciclo de Carnot
"""

# ESQUEMA
# A eficiência térmica de uma máquina térmica de Carnot é dada por:
# n_carnot = 1 - temperatura_fonte_fria / temperatura_fonte_quente
# n_carnot = trabalho_sai / calor_entra
# trabalho_sai / calor_entra = 1 - temperatura_fonte_fria / temperatura_fonte_quente
# trabalho_sai = calor_entra * (1 - temperatura_fonte_fria / temperatura_fonte_quente)

# PROPRIEDADES DADAS

temperatura_fonte_fria = 300    # K (Kelvin)
temperatura_fonta_quente = 900  # K (Kelvin)
calor_entra = 1200              # kJ (kilo joules)

trabalho_sai = calor_entra * (1 - temperatura_fonte_fria/temperatura_fonta_quente)

print(f"O trabalho líquido produzido pela citada máquina vale {trabalho_sai:.2f} kJ.") 