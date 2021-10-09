peso=float(input("Qual é seu peso?"))
Altura=float(input('Qual é a sua altura?'))
IMC=peso/(Altura**2)
print("O IMC dessa pessoa é de {:.1f}".format(IMC))
if IMC<18.5:
    print("Voçê está Abaixo do peso normal")
elif 18.5 <= IMC <25:
    print("Parabéns, Voçê está na faixa de peso normal")
elif 25<= IMC < 30:
    print("Voçê está em sobrepeso")
elif 30<= IMC < 40:
    print("Voçê está em Obesidade")
elif IMC>= 40:
    print("Voçê está em Obesdidade Mórbida")
