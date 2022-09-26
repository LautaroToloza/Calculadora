import tkinter as tk


class Calculadora:
    def __init__(self):
        # Atributo
        self.cantidad_operadores = 5
        self.datos = ""
        self.lista = []
        self.es_otra_operacion = False
        self.flag_div = False
        self.hay_punto = False
        self.operadores = "+-/*^=."
        # Ventana
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        # (Ancho*Alto)
        self.ventana.geometry("275x155")

        # Label
        self.label = tk.Label(self.ventana, text=self.datos)
        self.label.grid(column=4, row=0)

        # Botones
        # Fila 1
        self.boton_7 = tk.Button(self.ventana, text="7", width=3, command=self.op_7)
        self.boton_7.grid(column=0, row=1)
        self.boton_7.configure(foreground="blue")
        self.boton_8 = tk.Button(self.ventana, text="8", width=3, command=self.op_8)
        self.boton_8.grid(column=1, row=1)
        self.boton_8.configure(foreground="blue")
        self.boton_9 = tk.Button(self.ventana, text="9", width=3, command=self.op_9)
        self.boton_9.grid(column=2, row=1)
        self.boton_9.configure(foreground="blue")
        self.boton_borrar = tk.Button(self.ventana, text="BR", width=3, command=self.borrar)
        self.boton_borrar.grid(column=3, row=1)
        self.boton_borrar.configure(background="black")
        self.boton_borrar.configure(foreground="red")
        # Fila 2
        self.boton_4 = tk.Button(self.ventana, text="4", width=3, command=self.op_4)
        self.boton_4.grid(column=0, row=2)
        self.boton_4.configure(foreground="blue")
        self.boton_5 = tk.Button(self.ventana, text="5", width=3, command=self.op_5)
        self.boton_5.grid(column=1, row=2)
        self.boton_5.configure(foreground="blue")
        self.boton_6 = tk.Button(self.ventana, text="6", width=3, command=self.op_6)
        self.boton_6.grid(column=2, row=2)
        self.boton_6.configure(foreground="blue")
        self.boton_dividir = tk.Button(self.ventana, text="/", width=3, command=self.op_dividir)
        self.boton_dividir.grid(column=3, row=2)
        self.boton_dividir.configure(background="black")
        self.boton_dividir.configure(foreground="white")
        # Fila 3
        self.boton_1 = tk.Button(self.ventana, text="1", width=3, command=self.op_1)
        self.boton_1.grid(column=0, row=3)
        self.boton_1.configure(foreground="blue")
        self.boton_2 = tk.Button(self.ventana, text="2", width=3, command=self.op_2)
        self.boton_2.grid(column=1, row=3)
        self.boton_2.configure(foreground="blue")
        self.boton_3 = tk.Button(self.ventana, text="3", width=3, command=self.op_3)
        self.boton_3.grid(column=2, row=3)
        self.boton_3.configure(foreground="blue")
        self.boton_multiplicar = tk.Button(self.ventana, text="*", width=3, command=self.op_multiplicar)
        self.boton_multiplicar.grid(column=3, row=3)
        self.boton_multiplicar.configure(background="black")
        self.boton_multiplicar.configure(foreground="white")
        # Fila 4
        self.boton_punto = tk.Button(self.ventana, text=".", width=3, command=self.op_punto)
        self.boton_punto.grid(column=0, row=4)
        self.boton_punto.configure(foreground="blue")
        self.boton_0 = tk.Button(self.ventana, text="0", width=3, command=self.op_0)
        self.boton_0.grid(column=1, row=4)
        self.boton_0.configure(foreground="blue")
        self.boton_mas = tk.Button(self.ventana, text="+", width=3, command=self.op_mas)
        self.boton_mas.grid(column=2, row=4)
        self.boton_mas.configure(background="black")
        self.boton_mas.configure(foreground="white")
        self.boton_menos = tk.Button(self.ventana, text="-", width=3, command=self.op_menos)
        self.boton_menos.grid(column=3, row=4)
        self.boton_menos.configure(background="black")
        self.boton_menos.configure(foreground="white")
        # Fila 5
        self.boton_igual = tk.Button(self.ventana, text="=", width=3, command=self.op_igual)
        self.boton_igual.grid(column=2, row=5)
        self.boton_igual.configure(background="black")
        self.boton_igual.configure(foreground="white")
        self.boton_potencia = tk.Button(self.ventana, text="^", width=3, command=self.op_potencia)
        self.boton_potencia.grid(column=3, row=5)
        self.boton_potencia.configure(background="black")
        self.boton_potencia.configure(foreground="white")
        self.ventana.mainloop()

    # Métodos para el command
    def op_0(self):
        self.nueva_operacion()
        self.datos += "0"
        self.label.configure(text=self.datos)

    def op_1(self):
        self.nueva_operacion()
        self.datos += "1"
        self.label.configure(text=self.datos)

    def op_2(self):
        self.nueva_operacion()
        self.datos += "2"
        self.label.configure(text=self.datos)

    def op_3(self):
        self.nueva_operacion()
        self.datos += "3"
        self.label.configure(text=self.datos)

    def op_4(self):
        self.nueva_operacion()
        self.datos += "4"
        self.label.configure(text=self.datos)

    def op_5(self):
        self.nueva_operacion()
        self.datos += "5"
        self.label.configure(text=self.datos)

    def op_6(self):
        self.nueva_operacion()
        self.datos += "6"
        self.label.configure(text=self.datos)

    def op_7(self):
        self.nueva_operacion()
        self.datos += "7"
        self.label.configure(text=self.datos)

    def op_8(self):
        self.nueva_operacion()
        self.datos += "8"
        self.label.configure(text=self.datos)

    def op_9(self):
        self.nueva_operacion()
        self.datos += "9"
        self.label.configure(text=self.datos)

    def borrar(self):
        lista_borrar = []
        str = ""
        if len(self.datos) > 0:
            for car in self.datos:
                lista_borrar.append(car)
            # Eliminar caracter
            del (lista_borrar[-1])
            for car in lista_borrar:
                str += car
            self.datos = str
            self.label.configure(text=self.datos)

        else:
            pass

    # Operadores
    def op_punto(self):
        n = len(self.datos) - 1
        if n > 0:
            if self.datos[n] in self.operadores:
                pass
            else:
                self.datos += "."
                self.label.configure(text=self.datos)

    def op_mas(self):
        n = len(self.datos) - 1
        if n > 0:
            if self.datos[n] in self.operadores:
                pass
            else:
                self.datos += "+"
                self.label.configure(text=self.datos)

    def op_menos(self):
        n = len(self.datos) - 1
        if n > 0:
            if self.datos[n] in self.operadores:
                pass
            else:
                self.datos += "-"
                self.label.configure(text=self.datos)

    def op_multiplicar(self):
        n = len(self.datos) - 1
        if n > 0:
            if self.datos[n] in self.operadores:
                pass
            else:
                self.datos += "*"
                self.label.configure(text=self.datos)

    def op_dividir(self):
        n = len(self.datos) - 1
        if n > 0:
            if self.datos[n] in self.operadores:
                pass
            else:
                self.datos += "/"
                self.label.configure(text=self.datos)

    def op_potencia(self):
        n = len(self.datos) - 1
        if n > 0:
            if self.datos[n] in self.operadores:
                pass
            else:
                self.datos += "^"
                self.label.configure(text=self.datos)

    def op_igual(self):
        n = len(self.datos) - 1
        if n > 0:
            if self.datos[n] in self.operadores:
                pass
            else:
                self.datos += "="
                self.label.configure(text=self.datos)
        self.agregar_num()
        self.resultado = self.operacion()
        # Configurar color del resultado, si es una division por 0.
        if self.flag_div is True:
            self.label.configure(foreground="red")
            self.flag_div = False
        else:
            self.label.configure(foreground="blue")
        # Mostrar resultado
        self.label.configure(text=str(self.resultado))
        # Nueva operacion
        self.es_otra_operacion = True

    # Métodos para calcular resultado
    def agregar_num(self):
        self.__num = "0123456789"
        self.__numStr = ""
        self.es_operador = self.cantidad_operadores * [False]
        for car in self.datos:
            if car in self.__num or car == ".":
                self.__numStr += car
                if car == ".":
                    self.hay_punto = True
            else:
                if self.hay_punto is True:
                    self.lista.append(float(self.__numStr))
                else:
                    self.lista.append(int(self.__numStr))
                if car == "+":
                    self.es_operador[0] = True
                elif car == "-":
                    self.es_operador[1] = True
                elif car == "*":
                    self.es_operador[2] = True
                elif car == "/":
                    self.es_operador[3] = True
                elif car == "^":
                    self.es_operador[4] = True

                self.__numStr = ""

    def operacion(self):
        resultado = 0
        if self.es_operador[0] is True:
            for num in self.lista:
                resultado += num
        elif self.es_operador[1] is True:
            resultado = self.lista[0] - self.lista[1]
        elif self.es_operador[2] is True:
            resultado = self.lista[0] * self.lista[1]
        elif self.es_operador[3] is True:
            try:
                resultado = self.lista[0] / self.lista[1]
                resultado = round(resultado, 3)
            except ZeroDivisionError:
                resultado = "El divisor no puede ser 0!!"
                self.flag_div = True

        elif self.es_operador[4] is True:
            resultado = pow(self.lista[0], self.lista[1])

        return resultado

    def nueva_operacion(self):
        if self.es_otra_operacion is True:
            # Reiniciar variables
            self.datos = ""
            self.label.configure(text=self.datos)
            self.label.configure(foreground="black")
            self.lista = []
            self.es_operador = self.cantidad_operadores * [False]
            self.es_otra_operacion = False
            self.hay_punto = False


def test():
    Calculadora()


if __name__ == '__main__':
    test()
