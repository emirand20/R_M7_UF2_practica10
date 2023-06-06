import pandas as pd
import matplotlib.pyplot as plt


def city(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # convertiremos la columna 'date' en un formato de fecha utilizando la función 'to.datetime', con el atributo 'dt.month' devolvemos el número de cada mes
        casos_por_mes = df.groupby(['location', pd.to_datetime(df['date']).dt.month])['total_cases'].sum()

        paises_top10 = casos_por_mes.groupby('location').sum().nlargest(10).index

        for pais in paises_top10:
            print(f"País: {pais}")
            print(casos_por_mes[pais])
            print()

        # crearemos una nueva figura
        plt.figure()

        for pais in paises_top10:
            casos = casos_por_mes[pais]
            plt.plot(casos.index, casos.values, label=pais)

        # agregamos una leyenda
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def dead(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # devolveremos una lista que contiene los nombres de los dies paises más frecuentes de df
        paises_top10 = df['location'].value_counts().head(10).index.tolist()

        plt.figure()
        for pais in paises_top10:
            muertes_por_mes = df[df['location'] == pais].groupby(pd.to_datetime(df['date']).dt.month)[
                'total_deaths'].sum()
            print(f"País: {pais}", muertes_por_mes)
            plt.plot(muertes_por_mes.index, muertes_por_mes.values, label=pais)

        # configuramos el título y las etiquetas de los ejes
        plt.title("Muertes totales por mes - 10 ciudades principales")
        plt.xlabel("Mes")
        plt.ylabel("Muertes totales")

        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def reproduction_rate(csv_file):
    try:
        df = pd.read_csv(csv_file)
        paises_top10 = df['location'].value_counts().head(10).index.tolist()

        plt.figure()

        for pais in paises_top10:
            datos_pais = df[df['location'] == pais]

            reproduction_rate = datos_pais.groupby(pd.to_datetime(datos_pais['date']).dt.month)[
                'reproduction_rate'].sum()

            print(f"País: {pais}")
            print(reproduction_rate)

            plt.plot(reproduction_rate.index, reproduction_rate.values, label=pais)

        plt.title("Tasa de reproducción por mes - 10 ciudades principales")
        plt.xlabel("Mes")
        plt.ylabel("Tasa de reproducción")

        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
