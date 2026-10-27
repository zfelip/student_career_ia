"""Funcoes de apoio a graficos, isoladas do treinamento."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def save_figure(fig, path, dpi=110):
    fig.tight_layout()
    fig.savefig(path, dpi=dpi)
    plt.close(fig)
