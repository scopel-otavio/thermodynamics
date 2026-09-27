"""
Exemplo 1.1 - Aplicação da Primeira Lei ao Sistema Fechado

AAquecimento isobárico de oxigênio em sistema fechado
"""

# Propriedades do fluído / Constantes (PEP 8: maiúsculas)
CP_OXIGENIO = 909.4 # J / (kg * K)

# Estado inicial (A)
massa = 0.95            # kg
temp_a_celcius = 27     # °C
pressao_a = 150         # kPa (absoluta)

# Estado final (B)
pressao_b = pressao_a
temp_b_celcius = 627         # °C


# Variação e temperatura: delta(T_Celsius) == Delta(T_Kelvin)
delta_temp = temp_b_celcius - temp_a_celcius # K

# Primeira Lei para processo siobárico (P = cte)
# Delta(U) = Q - W
# W = P * Delta(V) = m * R * Delta(T)
# Delta*U = (U2 - U1) = m(u2 = u1) = m * cv * (T2 - T1) = m * cv * Delta(T)
# Q = W + Delta(U) = m * R * Delta(T) + m * cv * Delta(T)
# R = cp - cv
# Q = m * (R + cv) * Delta(T)
# Q = m * cp * Delta(T)
# Assim...

calor_joules = massa * CP_OXIGENIO * delta_temp
calor_kj = calor_joules / 1000

# Apresentação formatada
print(f"Variação de temperatura: {delta_temp:.1f} K")
print(f"Calor adicionado (Q):   {calor_joules:.2f} kJ")