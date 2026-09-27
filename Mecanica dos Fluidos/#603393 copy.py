"""
Considere as seguintes quantidades de fluidos colocadas em 3 reservatórios distintos: 14 m3 de água, 1 m3 de mercúrio e 15 m3 de gasolina.


Dados de pesos específicos (N/m3)
Água 10.000
Gasolina 7.200
Mercúrio 136.000
 
Em ordem crescente de peso nos reservatórios, tem-se
"""

# Volume dos fluidos
volume_agua = 14        # m³
volume_mercurio = 1     # m³
volume_gasolina = 15         # m³


# Pesos específicos
p_agua = 10000          # N /m³
p_gasolina = 7200       # N /m³
p_mercurio = 136000     # N /m³

peso_agua = volume_agua * p_agua                # N
peso_mercurio = volume_mercurio * p_mercurio    # N
peso_gasolina = volume_gasolina * p_gasolina    # N

lista_pesos = [peso_agua, peso_gasolina, peso_mercurio]
lista_pesos.sort()

print(f"A ordem crescente dos pesos é {lista_pesos}")

