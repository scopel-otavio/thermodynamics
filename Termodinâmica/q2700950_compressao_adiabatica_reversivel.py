"""
Questão 2700950 - Compressão adiabática reversível

Enunciado: 
Um gás ideal sofre uma compressão adiabática reversível, passando de um estado inicial com pressão P1 = 100 kPa e temperatura T1 = 293 K para um estado final com pressão P2 = 400 kPa. Sabendo que a razão entre os calores específicos (k) é igual a 2, determine a temperatura final T2 do gás.

Fórmula utilizada:
Gas ideal: T2 = T1 * (P2/P1)^((k-1)/k)
"""


def temperatura_final_adiabatica_reversivel(pressao_inicial, temperatura_inicial, pressao_final, k):
    return temperatura_inicial * (pressao_final / pressao_inicial) ** ((k - 1) / k)

if __name__ == "__main__":
    pressao_inicial = 100.0   # kPa
    temperatura_inicial = 293.0  # K
    pressao_final = 400.0     # kPa
    k = 2.0

    temperatura_final = temperatura_final_adiabatica_reversivel(
        pressao_inicial,
        temperatura_inicial,
        pressao_final,
        k
    )

    print(f"A temperatura final é {temperatura_final:.2f} K")