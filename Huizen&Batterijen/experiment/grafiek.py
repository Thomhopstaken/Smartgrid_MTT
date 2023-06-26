import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()
sep = os.sep


def histogram():
    bestand = f'gecombineerd.csv'
    df = pd.read_csv(bestand)

    # gemiddelde = np.mean(data)
    # standaard_af = np.std(data)
    #
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].hist(df['kmeans'], density=True, color='r')
    axs[0, 0].set_title('KMeans')
    axs[1, 0].hist(df['greedy'], density=True, color='b')
    axs[1, 0].set_title('Greedy')
    axs[0, 1].hist(df['random'], density=True, color='g')
    axs[0, 1].set_title('Random')
    axs[1, 1].hist(df['hillclimber'], density=True, color='c')
    axs[1, 1].set_title('Hill Climber')

    # plt.hist(df['kmeans'], density=True, color='r', label='KMeans', alpha=0.5, bins=50)
    # plt.hist(df['greedy'], density=True, color='b', label='Greedy', alpha=0.5, bins=50)
    # plt.hist(df['random'], density=True, color='g', label='Random', alpha=0.5, bins=50)
    # plt.hist(df['hillclimber'], density=True, color='c', label='Hill Climber', alpha=0.5, bins=50)
    # sns.kdeplot(df['kmeans'], linewidth=2)
    # sns.kdeplot(df['greedy'], linewidth=2)
    # sns.kdeplot(df['random'], linewidth=2)
    # sns.kdeplot(df['hillclimber'], linewidth=2)

    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    histogram()
