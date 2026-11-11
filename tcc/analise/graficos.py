"""Gráficos do Capítulo 4: média trimestral por grupo (Cenário 3), 31/12/2018 a 31/12/2025.

Gera PDFs vetoriais em tcc/latex/figuras/ com fonte Times (Liberation Serif, métrica idêntica).
Uso: python3 tcc/analise/graficos.py   (requer matplotlib, openpyxl, numpy)
"""
import datetime as dt
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import resultados_c3 as R

DATAS = []
for a in range(2018, 2026):
    for m, d in ((3, 31), (6, 30), (9, 30), (12, 31)):
        if (a, m) >= (2018, 12):
            DATAS.append(dt.date(a, m, d))
assert len(DATAS) == 29

COR = {'F': '#1f5a96', 'NF': '#d9752b'}
ROT = {'F': 'Familiares', 'NF': 'Não familiares'}
GRAFICOS = [
    ('Divida Bruta / Atv Tt %', 'div-bruta-ativo-trimestral.pdf', 'Dívida bruta / Ativo total (%)'),
    ('Exigivel Tt / Ativo Tt %', 'exigivel-ativo-trimestral.pdf', 'Exigível total / Ativo total (%)'),
    ('Divida CP / Divida Tt %', 'divida-cp-trimestral.pdf', 'Dívida CP / Dívida total (%)'),
]

plt.rcParams.update({
    'font.family': 'serif', 'font.serif': ['Liberation Serif', 'Times New Roman', 'Nimbus Roman'],
    'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': True, 'grid.color': '#dddddd', 'grid.linewidth': 0.6, 'axes.axisbelow': True,
    'pdf.fonttype': 42,
})


def main():
    dados, grupo, _ = R.carregar()
    destino = os.path.join(R.RAIZ, 'tcc', 'latex', 'figuras')
    for ind, arq, rotulo in GRAFICOS:
        fig, ax = plt.subplots(figsize=(6.3, 3.2))
        ax.axvspan(dt.date(2020, 3, 1), dt.date(2021, 12, 31), color='#eeeeee', zorder=0)
        for gg in ('F', 'NF'):
            serie = []
            for i in range(29):
                v = [dados[(t, ind)][i] for t in grupo if grupo[t] == gg and dados[(t, ind)][i] is not None]
                serie.append(np.mean(v))
            ax.plot(DATAS, serie, color=COR[gg], lw=1.8, marker='o', ms=2.5, label=ROT[gg])
        ax.set_ylabel(rotulo)
        ax.set_xlabel('Data-base (trimestral)')
        ax.set_xticks(DATAS[::4])
        ax.set_xticklabels([f'dez/{d.year}' for d in DATAS[::4]])
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, _: f'{y:.0f}'))
        ax.set_ylim(bottom=0)
        ax.text(dt.date(2020, 3, 15), ax.get_ylim()[1] * 0.97, 'pandemia', va='top', fontsize=8, color='#666666')
        ax.legend(frameon=False, loc='lower left', ncol=2)
        fig.tight_layout()
        fig.savefig(os.path.join(destino, arq))
        plt.close(fig)
        print('gerado', arq)


if __name__ == '__main__':
    main()
