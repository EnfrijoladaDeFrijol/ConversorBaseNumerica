import tkinter as tk

"""
Función "hacerConversion()"
Hacemos uso de las cadenas formateadas
"""
def hacerConversion(*args):
    try:
        numeroEntrada = entrada_numerConvertir.get()
        numeroEnDecimal = int(numeroEntrada, baseVar.get())

        etiqueta_decimal.config(text=f"Decimal: {numeroEnDecimal}")
        etiqueta_octal.config(text=f"Octal: {oct(numeroEnDecimal)[2:]}")
    except ValueError:
        limpiarEtiquetas()

def limpiarEtiquetas(): #Limpiamos en caso de error
    etiqueta_decimal.config(text="Decimal:")


raiz = tk.Tk()
raiz.title("Conversión de sistemas númericos")
raiz.config(bg="#FFFFFF")
raiz.geometry("400x300")

# Solo es el titulo
miTitulo = tk.Label(raiz, text="Conversor de bases númericas")
miTitulo.config(bg="gray",width=30,height=2)
miTitulo.pack()

# Número a convertir
etiqueta_numeroConvertir = tk.Label(raiz,text="Ingresa´valor:")
etiqueta_numeroConvertir.pack() # Muesta la etiqueta
entrada_numerConvertir = tk.Entry(raiz)
entrada_numerConvertir.pack() # Muestra el cuadro de entrada

# Seccioanmos base númerica
baseVar = tk.IntVar() # Variable tipo entero
etiqueta_baseOriginal = tk.Label(raiz, text="Base original:")
etiqueta_baseOriginal.pack()
# Base decimal
radio_baseDecimal = tk.Radiobutton(raiz, text="Decimal", variable=baseVar, value=10, command=hacerConversion)
radio_baseDecimal.pack()
# Base octal
radio_octal = tk.Radiobutton(raiz, text="Octal", variable=baseVar, value=8, command=hacerConversion)
radio_octal.pack()



miSalida = tk.Label(raiz, text="Salida de datos")
miSalida.config(bg="#A4EA7B",width=30,height=1)
miSalida.pack()
# Salida de datos
etiqueta_decimal = tk.Label(raiz, text="Decimal:")
etiqueta_decimal.pack()

etiqueta_octal = tk.Label(raiz, text="Octal:")
etiqueta_octal.pack()

raiz.mainloop()