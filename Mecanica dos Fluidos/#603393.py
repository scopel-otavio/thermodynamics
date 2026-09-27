fluidos = {
    "água": {"volume":14, "peso_especifico":10000},
    "mercúrio": {"volume":1, "peso_especifico":136000},
    "gasolina": {"volume":15, "peso_especifico":7200}
}

# Calcula o peso de cada fluido: P = V * v
pesos = {
    nome: dados["volume"] * dados["peso_especifico"]
    for nome, dados in fluidos.items()
}

# Ordena os nomes com base no valor do peso (ordem crescente)
ordem_crescente = sorted(pesos, key=pesos.get)

print("Pesos calculados (N):")
for fluido, peso in pesos.items():
    print(f" - {fluido.capitalize()}: {peso:,.0f} N")
    
print(f"\nOrdem crescente: {', '.join(ordem_crescente)}")