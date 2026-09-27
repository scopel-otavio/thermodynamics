"""
Ao iniciar uma viagem, o carro tinha 0,2 kg de ar (suposto gás perfeito) em cada pneu, à temperatura de 27ºC e pressão manométrica de 450 kPa. Ao final da viagem, a temperatura atingiu 57ºC. Despreze as variações de volume do pneu. Admita o seguinte:

 
• as propriedades termodinâmicas da substância não foram alteradas durante a viagem;
• Rar = 0,3 kN × m / Kg × K;
• Patm = 100 kPa.

 
Ao final da viagem, a pressão manométrica do ar no pneu, em KPa, e o volume do pneu, em m3, serão, respectivamente, iguais a
"""

# Hipoteses
# Gás ideal
# volume inicial = volume final

# Propriedades
massa_ar = 0.2      # kg
temperatura_inicial = 27        # ºC  
pressao_inicial = 450           # kPa (manométrica)

temperatura_final = 47          # ºC

# Equação do gás ideal PV = mRT

# P1 * V1 / T1 = P2 * V2 / T2
# P2 = (P1 / T1)  * T2

def pressao_final(T1, P1, T2):
    return ((P1 / T1) * T2)

print(pre)
