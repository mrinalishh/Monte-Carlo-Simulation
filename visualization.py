import matplotlib
matplotlib.use('TkAgg')  # ensures window opens

import matplotlib.pyplot as plt
import numpy as np


# ------------------ BASIC ------------------
def plot_results(results):
    plt.figure(figsize=(8, 5))
    plt.hist(results, bins=10)
    plt.title("Monte Carlo Results")
    plt.grid(True)
    plt.show(block=True)


# ------------------ STOCK CLEAN ------------------
def plot_stock_simulation(simulations):
    plt.figure(figsize=(10, 6))

    mean_path = np.mean(simulations, axis=1)
    median_path = np.median(simulations, axis=1)
    p5 = np.percentile(simulations, 5, axis=1)
    p95 = np.percentile(simulations, 95, axis=1)

    # sample paths
    for i in range(min(10, simulations.shape[1])):
        plt.plot(simulations[:, i], alpha=0.2)

    # main lines
    plt.plot(mean_path, linewidth=4, label="Mean")
    plt.plot(median_path, linestyle='--', linewidth=2, label="Median")

    # range
    plt.fill_between(range(len(mean_path)), p5, p95, alpha=0.15, label="5-95% Range")

    # starting price
    plt.axhline(simulations[0, 0], linestyle=':', label="Initial Price")

    plt.title("Monte Carlo Stock Simulation (1-Year Forecast)")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.show(block=True)


# ------------------ DISTRIBUTION ------------------
def plot_final_distribution(final_prices):
    plt.figure(figsize=(10, 6))

    plt.hist(final_prices, bins=30, alpha=0.7)

    mean_price = np.mean(final_prices)
    median_price = np.median(final_prices)
    var_95 = np.percentile(final_prices, 5)

    plt.axvline(mean_price, linestyle='--', linewidth=2, label=f"Mean: {mean_price:.2f}")
    plt.axvline(median_price, linestyle='-', linewidth=2, label=f"Median: {median_price:.2f}")
    plt.axvline(var_95, linestyle=':', linewidth=2, label=f"VaR (5%): {var_95:.2f}")

    plt.title("Final Price Distribution with Risk Metrics")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)

    plt.show(block=True)