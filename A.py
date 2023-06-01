import pandas as pd


def city(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # obtenemos los primeros 10 paises con mas valor
        paises_top10 = df['location'].value_counts().head(10).index.tolist()

        for pais in paises_top10:
            # filtramos df, para obtener solo las filas que corresponden al país actual
            datos_pais = df[df['location'] == pais]

            # agrupamos con groupby datos_pais y utilizamos pd.to_datetime() para convertir la columna 'date' en formato de fecha
            # con esto extraemos el mes indicado y lo agrupamos, luego con la columna 'total_cases'y se suma para obtener la cantidad
            # total de casos por mes para ese país
            casos_por_mes = datos_pais.groupby(pd.to_datetime(datos_pais['date']).dt.month)['total_cases'].sum()

            # mostraremos la cantidad total de casos por mes para ese país.
            print(f"Pais: {pais}", casos_por_mes)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def dead(csv_file):
    try:
        df = pd.read_csv(csv_file)
        paises_top10 = df['location'].value_counts().head(10).index.tolist()

        for pais in paises_top10:

            datos_pais = df[df['location'] == pais]

            # convertimos la columna 'date' en formato de fecha utilizando .loc
            datos_pais.loc[:, 'date'] = pd.to_datetime(datos_pais['date'])

            # agrupamos por mes y sumamos los valores de 'total_deaths'
            muertes_por_mes = datos_pais.groupby(datos_pais['date'].dt.month)['total_deaths'].sum()
            
            # mostramos la cantidad total de muertes por mes para ese país
            print(f"País: {pais}", muertes_por_mes)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))

