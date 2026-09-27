# Exemplo 1.1 - Aplicação da Primeira Lei ao Sistema Fechado
cp = 909.4 # J / (kg * K)


massa_oxigenio_A = 0.95 # kg
temperatura_A = 27 # ºC
pressao_A = 150 # kPa (absoluta)

# Calor é adicionado

massa_oxigenio_B = massa_oxigenio_A # conservação da massa
pressao_B = 150 # kPa (absoluta)
temperatura_B = 627 # °C

# Primeira lei Q - W = dU
# Trabalhdo W = ∫PdV
# ...para um gás ideal PV = mRT > P = mRT / V
# W = P(V2 -V1) = mR/V * (T2 - T1) * V
# W = mR(T2 - T1)

#dU = (U2 - U1) = m(u2 - u1) = m*cv*(T2-T1)
# Q = du + W = m*cv*(T2-T1) + mR(T2 - T1)
# Q = (T2 - T1) * m * (cv - R)
# mas.. R = cp - cv
# Q = (m*cp(T2 - T1))


#... Assim

calor = massa_oxigenio_A * cp * (600) # J
calor_kj = calor / 1000
print("Calor é " + str(calor_kj) + " kj")