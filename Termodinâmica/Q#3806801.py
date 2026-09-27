"""
Resolução da questão #3806801 (CESGRANRIO - CEF/Engenheiro Mecânico)
Transformação Isocórica (Volume constante) de Gás Ideal
"""


def celsius_para_kelvin(temp_celsius: float) -> float:
    return temp_celsius + 273.0

def calcular_pressao_absoluta(pressao_manometrica: float, pressao_atm: float) -> float:
    return pressao_manometrica + pressao_atm

def calcular_pressao_manometrica(pressao_absoluta: float, pressao_atm: float) -> float:
    return pressao_absoluta - pressao_atm


# Dados do problema
p_atm = 100.0                # kPa

# Estado A (Inicial)
p_man_a = 200.0              # kPa
temp_celsius_a = 27.0        # °C (corrigido de 26 para 27)

# Estado B (Final)
temp_celsius_b = 45.0        # °C

# Conversões para escala termodinâmica absoluta
t_a = celsius_para_kelvin(temp_celsius_a)
t_b = celsius_para_kelvin(temp_celsius_b)
p_abs_a = calcular_pressao_absoluta(p_man_a, p_atm)

# Lei de Charles / Gay-Lussac (V = constante): P_abs_A / T_A = P_abs_B / T_B
p_abs_b = p_abs_a * (t_b / t_a)

# Conversão final para pressão manométrica
p_man_b = calcular_pressao_manometrica(p_abs_b, p_atm)

print(f"Temperatura A: {t_a:.1f} K")
print(f"Temperatura B: {t_b:.1f} K")
print(f"Pressão absoluta final: {p_abs_b:.1f} kPa")
print(f"Nova pressão manométrica: {p_man_b:.0f} kPa")