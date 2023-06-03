import pandas as pd


def city(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # ordenar el DataFrame por población en orden descendente
        df_sorted = df.sort_values('Population', ascending=False)

        # seleccionar las 10 primeras ciudades con mayor población
        top10_ciudades = df_sorted.head(10)[['City', 'Population']]
        print(top10_ciudades)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def KM2(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # ordenar el DataFrame por población en orden descendente
        df_sorted = df.sort_values('Population', ascending=False)

        # seleccionar las 10 primeras ciudades con mayor población
        top10_ciudades = df_sorted.head(10)[['Density KM2', 'Population']]
        print(top10_ciudades)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def M2(csv_file):
    try:
        df = pd.read_csv(csv_file)
        # ordenar el DataFrame por población en orden descendente
        df_sorted = df.sort_values('Population', ascending=False)
        # seleccionar las 10 primeras ciudades con mayor población
        top10_ciudades = df_sorted.head(10)[['Density  M2', 'Population']]
        print(top10_ciudades)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))