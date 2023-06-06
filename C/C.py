import pandas as pd
import matplotlib.pyplot as plt


def mobil(csv_file):
    try:
        df = pd.read_csv(csv_file)

        # ordenamos por "id" en orden descendente
        df_sorted = df.sort_values('id', ascending=False)

        mobile = df_sorted.head(10)[['id', 'clock_speed']]
        print(mobile)

        ids = mobile['id']
        clock_speeds = mobile['clock_speed']

        fig, ax = plt.subplots()

        # gráfica de barras
        ax.bar(ids, clock_speeds)

        # títulos y etiquetas de los ejes
        ax.set_xlabel('ID')
        ax.set_ylabel('Clock Speed')
        ax.set_title('Top 10 Mobile Clock Speeds')

        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def megapixels(csv_file):
    try:
        df = pd.read_csv(csv_file)

        df_sorted = df.sort_values('id', ascending=False)

        mobile = df_sorted.head(10)[['id', 'mobile_wt']]
        print(mobile)

        # sacar los datos de "id" y "mobile_wt"
        ids = mobile['id']
        mobile_weights = mobile['mobile_wt']

        fig, ax = plt.subplots()

        ax.bar(ids, mobile_weights)

        ax.set_xlabel('ID')
        ax.set_ylabel('Mobile Weight')
        ax.set_title('Top 10 Mobile Weights')

        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def battery_power(csv_file):
    try:
        df = pd.read_csv(csv_file)
        df_sorted = df.sort_values('id', ascending=False)

        mobile = df_sorted.head(10)[['id', 'battery_power']]
        print(mobile)

        ids = mobile['id']
        battery_powers = mobile['battery_power']

        fig, ax = plt.subplots()

        # gráfica de barras
        ax.bar(ids, battery_powers)

        ax.set_xlabel('ID')
        ax.set_ylabel('Battery Power')
        ax.set_title('Top 10 Battery Powers')

        plt.show()

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error:", str(e))