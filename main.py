import sys
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# como a origem so menciona que o tem 365 dias, e estou usando
# a funcao para pegar o dia do ano, foi necessario definir o ano nao bissexto
_year = 2019


def load_data():
    activities = pd.read_json("https://static.cingulo.com/bi/user_activities.json")
    return activities


def prepare_data():
    activities = load_data()
    _month = 1
    d = datetime.date(_year, 1, 1) + datetime.timedelta(0)
    m = d.strftime('%B')
    # Define os dias do mes
    df = pd.DataFrame(columns=['day'])
    for i in range(1, 32):
        df = df.append({'day': i}, ignore_index=True)

    # Trata os dados ja calculando o percentual de acessos por dia
    for i in range(365):
        temp_df = activities['activities'].str[i:i + 1].map(sum)
        d = datetime.date(_year, 1, 1) + datetime.timedelta(i)
        if d.month != _month:
            _month = d.month
            m = d.strftime('%B')
        df.at[d.day - 1, m] = temp_df.sum() / temp_df.count() * 100
    return df


def print_power_curve(months=[1, 2, 3]):
    df = prepare_data()
    legend = []
    for i in months:
        m = datetime.date(_year, int(i), 1).strftime('%B')
        plt.plot(df['day'], df[m], label=m)
    #    legend.append(m)
    plt.ylim(0, 100)
    plt.grid()
    # #
    plt.xlabel('Dia do Mês')
    plt.ylabel('Percentual de Acesso')
    plt.legend()
    plt.show()


def export_to_xlsx():
    df = prepare_data()
    df.to_excel('cingulo_activities.xlsx')


if __name__ == '__main__':
    param = sys.argv
    if len(param) > 1:
        if param[1] == '0':
            export_to_xlsx()
        else:
            print_power_curve(param[1:])
