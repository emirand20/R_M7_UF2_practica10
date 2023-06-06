import pandas as pd
import matplotlib.pyplot as plt


def city(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # ordenamos el df por población en orden descendente
        df['Population'] = df['Population'].str.replace(',', '').astype(float)
        df_sorted = df.sort_values('Population', ascending=False)

        # seleccionamos las 10 primeras ciudades con mayor población
        top10_ciudades = df_sorted.head(10)[['City', 'Population']]
        print(top10_ciudades)

        ciudades = top10_ciudades['City']
        poblaciones = top10_ciudades['Population']

        fig, ax = plt.subplots()

        # gráfico de tipo "queso"
        ax.pie(poblaciones, labels=ciudades, autopct='%1.1f%%', startangle=90)

        ax.set_title("Top 10 ciudades por población")
        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def KM2(csv_file):
    try:
        df = pd.read_csv(csv_file)

        df['Density KM2'] = df['Density KM2'].str.replace(',', '').astype(float)
        df_sorted = df.sort_values('Population', ascending=False)

        top10_ciudades = df_sorted.head(10)[['Density KM2', 'Population']]
        print(top10_ciudades)

        # extraemos los datos de densidad y población
        densidad = top10_ciudades['Density KM2']
        poblacion = top10_ciudades['Population']

        fig, ax = plt.subplots()

        # gráfico de tipo "queso"
        ax.pie(densidad, labels=poblacion, autopct='%1.1f%%', startangle=90)
        ax.set_title("Top 10 ciudades por densidad y población")
        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def M2(csv_file):
    try:
        df = pd.read_csv(csv_file)

        df['Density  M2'] = df['Density  M2'].str.replace(',', '').astype(float)
        df_sorted = df.sort_values('Population', ascending=False)

        # seleccionamos las 10 primeras ciudades con mayor población
        top10_ciudades = df_sorted.head(10)[['Density  M2', 'Population']]
        print(top10_ciudades)

        # sacamos los datos de densidad y población
        densidad = top10_ciudades['Density  M2']
        poblacion = top10_ciudades['Population']

        fig, ax = plt.subplots()

        # gráfico de tipo "queso"
        ax.pie(densidad, labels=poblacion, autopct='%1.1f%%', startangle=90)
        ax.set_title("Top 10 ciudades por densidad y población")
        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))