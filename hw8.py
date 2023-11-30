import matplotlib.pyplot as plt
import random


def f(x):
    if x == 2:
        return 0.1
    elif x == 3:
        return 0.5
    elif x == 4:
        return 0.4
    else:
        return 0


def F(x):
    if x < 2:
        return 0
    elif 2 <= x:
        cdf = 0
        for i in range(2, x+1):
            cdf += f(i)
        return cdf


def plot_pdf_cdf():
    x = [i for i in range(0, 7)]
    pdf = [f(k) for k in x]
    cdf = [F(k) for k in x]
    plt.plot(x, pdf, "bo")
    plt.plot(x, cdf, "r+")
    plt.legend(["PDF", "CDF"])
    plt.show()


def inverse_cdf(u):
    sample = 0
    for x in range(2, 5):
        if F(x-1) <= u <= F(x):
            sample = x

    return sample


def take_sample():
    u = random.random()
    return inverse_cdf(u)


def take_samples(n):
    samples = {2: 0, 3: 0, 4: 0}
    for i in range(n):
        samples[take_sample()] += 1

    return samples


def plot_samples():
    n_samples = [100, 10, 20, 50, 1000]

    for n in n_samples:
        samples = take_samples(n)
        for i in range(2, 5):
            samples[i] /= n

        plt.hist(list(samples.keys()), list(samples.values()))
        plt.legend([f"Sample Distribution for {n} samples"])
        plt.show()

    x = [i for i in range(0, 7)]
    pdf = [f(k) for k in x]
    plt.hist(x, pdf)
    plt.legend(["f(x)"])
    plt.show()


plot_samples()