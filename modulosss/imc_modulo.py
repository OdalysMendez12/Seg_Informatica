#Fórmula para el imc = peso/estatura^2
def imc(peso, estatura):
    return (peso/estatura**2)

def nivel_de_peso(p_imc):
    if p_imc < 18.5:
        print("Tienes bajo peso.")
    elif p_imc >= 18.5 and p_imc <= 24.9:
        print("Tienes un peso normal.")
    elif p_imc >= 25 and p_imc <= 29.9:
        print("Tienes sobrepeso.")
    else:
        print("Tienes obesidad.")
        