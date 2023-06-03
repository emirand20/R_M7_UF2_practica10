import pandas as pd


def city(csv_file):
    try:
        df = pd.read_csv(csv_file)

        casos_por_mes = df.groupby(['location', pd.to_datetime(df['date']).dt.month])['total_cases'].sum()

        paises_top10 = casos_por_mes.groupby('location').sum().nlargest(10).index

        for pais in paises_top10:
            print(f"País: {pais}")
            print(casos_por_mes[pais])
            print()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def dead(csv_file):
    try:
        df = pd.read_csv(csv_file)
        paises_top10 = df['location'].value_counts().head(10).index.tolist()

        for pais in paises_top10:
            muertes_por_mes = df[df['location'] == pais].groupby(pd.to_datetime(df['date']).dt.month)[
                'total_deaths'].sum()
            print(f"País: {pais}", muertes_por_mes)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def reproduction_rate(csv_file):
    try:
        df = pd.read_csv(csv_file)
        paises_top10 = df['location'].value_counts().head(10).index.tolist()

        for pais in paises_top10:
            datos_pais = df[df['location'] == pais]

            reproduction_rate = datos_pais.groupby(pd.to_datetime(datos_pais['date']).dt.month)[
                'reproduction_rate'].sum()

            print(f"País: {pais}")
            print(reproduction_rate)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
