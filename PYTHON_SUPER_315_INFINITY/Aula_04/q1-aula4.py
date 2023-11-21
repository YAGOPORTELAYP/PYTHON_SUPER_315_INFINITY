def indice(m,h):
    return m/h**2

imc = []

for i in range(1,5):
    m = float(input(f"Digite a massa do {i}º Usuário:"))
    h = float(input(f"Digite a altura do {i}º Usuário:"))
    imc.append(indice(m,h))

for i in imc:
    print(f"\n{i:.2f}")