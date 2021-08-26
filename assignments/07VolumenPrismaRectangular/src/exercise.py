# Escribe aquí tus funciones...
def area_prisma(base,altura):
    return (base*altura)
def volumen_prisma(base,profundidad):
    return (base * profundidad)

def main():
    #escribe tu código abajo de esta línea
        b = float(input("Dame la base: "))
        a = float(input("Dame la altura: "))
        p = float(input("Dame la profundidad: "))

        r = volumen_prisma(area_prisma(b,a),p)

        print("El volumen del prisma es:",r)


if __name__=='__main__':
    main()
