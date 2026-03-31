import random
import numpy as np
import yfinance as yf


def coin_simulation(trials, tosses=10):
    success = 0
    results = []

    for _ in range(trials):
        heads = sum(1 for _ in range(tosses) if random.random() > 0.5)
        results.append(heads)

        if heads > 6:
            success += 1

    probability = success / trials
    return probability, results


def dice_simulation(trials):
    success = 0
    results = []

    for _ in range(trials):
        roll = random.randint(1, 6)
        results.append(roll)

        if roll > 4:
            success += 1

    probability = success / trials
    return probability, results


def stock_monte_carlo(ticker="AAPL", days=252, simulations=1000):
    data = yf.download(ticker, period="1y")

    close_prices = data["Close"]

    # Fix if dataframe
    if hasattr(close_prices, "columns"):
        close_prices = close_prices.iloc[:, 0]

    close_prices = close_prices.dropna()

    if len(close_prices) == 0:
        return None

    returns = close_prices.pct_change().dropna()

    mu = float(returns.mean())
    sigma = float(returns.std())

    S0 = float(close_prices.iloc[-1])

    simulation_results = np.zeros((days, simulations))

    for sim in range(simulations):
        prices = np.zeros(days)
        prices[0] = S0

        for t in range(1, days):
            shock = np.random.normal(mu, sigma)
            prices[t] = prices[t - 1] * (1 + shock)

        simulation_results[:, sim] = prices

    return simulation_results


def risk_analysis(simulations):
    final_prices = simulations[-1]

    mean_price = np.mean(final_prices)
    min_price = np.min(final_prices)
    max_price = np.max(final_prices)

    initial_price = simulations[0, 0]
    prob_loss = np.mean(final_prices < initial_price)

    return mean_price, min_price, max_price, prob_loss, final_prices