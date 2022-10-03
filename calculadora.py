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
        self.boton_7 = self.boton_num_punto("7", 0, 1)
        self.boton_8 = self.boton_num_punto("8", 1, 1)
        self.boton_9 = self.boton_num_punto("9", 2, 1)
        self.boton_borrar = tk.Button(self.ventana, text="BR", width=3, command=self.borrar)
        self.boton_borrar.grid(column=3, row=1)
        self.boton_borrar.configure(background="black")
        self.boton_borrar.configure(foreground="red")
        # Fila 2
        self.boton_4 = self.boton_num_punto("4", 0, 2)
        self.boton_5 = self.boton_num_punto("5", 1, 2)
        self.boton_6 = self.boton_num_punto("6", 2, 2)
        self.boton_dividir = self.boton_operador("/", 3, 2)
        # Fila 3
        self.boton_1 = self.boton_num_punto("1", 0, 3)
        self.boton_2 = self.boton_num_punto("2", 1, 3)
        self.boton_3 = self.boton_num_punto("3", 2, 3)
        self.boton_multiplicar = self.boton_operador("*", 3, 3)
        # Fila 4
        self.boton_punto = self.boton_num_punto(".", 0, 4)
        self.boton_0 = self.boton_num_punto("0", 1, 4)
        self.boton_mas = self.boton_operador("+", 2, 4)
        self.boton_menos = self.boton_operador("-", 3, 4)
        # Fila 5
        self.boton_igual = tk.Button(self.ventana, text="=", width=3, command=self.op_igual)
        self.boton_igual.grid(column=2, row=5)
        self.boton_igual.configure(background="black")
        self.boton_igual.configure(foreground="white")
        self.boton_potencia = self.boton_operador("^", 3, 5)
        self.ventana.mainloop()

    def boton_num_punto(self, valor, columna, fila):
        self.boton = tk.Button(self.ventana, text=valor, width=3, command=lambda: self.op_numero(valor))
        self.boton.grid(column=columna, row=fila)
        self.boton.configure(foreground="blue")
        return self.boton

    def boton_operador(self, valor, columna, fila):
        self.boton_op = tk.Button(self.ventana, text=valor, width=3, command=lambda: self.op_operador(valor))
        self.boton_op.grid(column=columna, row=fila)
        self.boton_op.configure(background="black")
        self.boton_op.configure(foreground="white")
        return self.boton_op

    # Métodos para el command
    def op_numero(self, valor):
        self.nueva_operacion()
        self.datos += valor
        self.label.configure(text=self.datos)

    def op_operador(self, simbolo):
        n = len(self.datos)
        if n == 0 and simbolo == "-":
            self.datos += simbolo
            self.label.configure(text=self.datos)
        else:
            if n > 0:
                if self.datos[n - 1] in self.operadores:
                    pass
                else:
                    self.datos += simbolo
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

    def op_igual(self):
        n = len(self.datos) - 1
        if n >= 0:
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
        self.num = "0123456789."
        self.es_operador = self.cantidad_operadores * [False]
        self.__numStr = ""
        for i in range(len(self.datos)):
            if i == 0 and self.datos[i] == "-" or self.datos[i] in self.num:
                self.__numStr += self.datos[i]
                if self.datos[i] == ".":
                    self.hay_punto = True
            else:
                if self.hay_punto is True:
                    self.lista.append(float(self.__numStr))
                else:
                    self.lista.append(int(self.__numStr))
                if self.datos[i] == "+":
                    self.es_operador[0] = True
                elif self.datos[i] == "-":
                    self.es_operador[1] = True
                elif self.datos[i] == "*":
                    self.es_operador[2] = True
                elif self.datos[i] == "/":
                    self.es_operador[3] = True
                elif self.datos[i] == "^":
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
