from Ui import Ui
from Api import Api

def main():


    # Obtiene los datos de entrada del usuario
    N_departamento, registros = Ui.ingresar_datos()

    # Obtiene los datos de COVID-19 del API
    data = Api.obtener_datos(N_departamento, registros)

    # Muestra los resultados al usuario
    Ui.mostrar_resultados(data)


main()