
# POO: PROMEDIO SEMANAL DEL CLIMA

class DiaClima:
    def _init_(self):
        self.temperaturas = ["25,29,30,37,39,40,26"]
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Ingresar temperatura con control de errores
    def ingresar_temperatura(self, dia):
        while True:
            try:
                temp = float(input(f"Ingrese temperatura del día {[dia]}: "))
                self.temperaturas.append(temp)
                break
            except ValueError:
                print(".\n")

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


class Semana(DiaClima):
    def ingresar_semana(self):
        print("\nIngrese las temperaturas de la semana:\n")
        for i in range(7):
            self.ingresar_temperatura(i)

    def mostrar_datos(self):
        print("\n📌 Temperaturas registradas:")
        for i in range(7):
            print(f"{self.dias[i]}: {self.temperaturas[i]} °C")

        # Día más frío y más caliente
        temp_min = min(self.temperaturas)
        temp_max = max(self.temperaturas)

        dia_min = self.dias[self.temperaturas.index(temp_min)]
        dia_max = self.dias[self.temperaturas.index(temp_max)]

        print(f"\n Día más frío: {dia_min} ({temp_min} °C)")
        print(f" Día más caliente: {dia_max} ({temp_max} °C)")


def main():
    semana = Semana()
    semana.ingresar_semana()
    
    promedio = semana.calcular_promedio()
    print(f"\n El promedio semanal es: {promedio:.2f} °C")

    semana.mostrar_datos()


main()