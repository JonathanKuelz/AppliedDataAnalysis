import numpy as np


def bootstrap_CI(data, nbr_draws, ci=(2.5, 97.5)):
    """
    Helper function from Tutorial02, becoming a Data Viz
    :param data: A list or np array (1D) containing data samples.
    :param nbr_draws: The number of random samples. 1000 is a good number.
    :param ci: Upper and lower confidence bounds
    :return: [lower error, upper error]
    """
    means = np.zeros(nbr_draws)
    data = np.array(data)

    for n in range(nbr_draws):
        indices = np.random.randint(0, len(data), len(data))
        data_tmp = data[indices]
        means[n] = np.nanmean(data_tmp)

    lower, upper = ci
    return [np.nanpercentile(means, lower), np.nanpercentile(means, upper)]
