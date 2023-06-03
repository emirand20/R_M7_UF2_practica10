import pandas as pd


def mobil(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # ordenar el DataFrame por población en orden descendente
        df_sorted = df.sort_values('id', ascending=False)

        # seleccionar las 10 primeras ciudades con mayor población
        mobile = df_sorted.head(10)[['id', 'clock_speed']]
        print(mobile)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def megapixels(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # ordenar el DataFrame por población en orden descendente
        df_sorted = df.sort_values('id', ascending=False)

        # seleccionar las 10 primeras ciudades con mayor población
        mobile = df_sorted.head(10)[['id', 'mobile_wt']]
        print(mobile)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def battery_power(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # ordenar el DataFrame por población en orden descendente
        df_sorted = df.sort_values('id', ascending=False)

        # seleccionar las 10 primeras ciudades con mayor población
        mobile = df_sorted.head(10)[['id', 'battery_power']]
        print(mobile)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
