import logging

log = logging.getLogger()

def state(signal, num_contract):
    """A function that returns the current state. LONG or SHORT.
    """
    if signal > 0:
        return "LONG {}".format(int(signal / 100 * num_contract))
    else:
        return "SHORT {}".format(int(abs(signal) / 100 * num_contract))

def average(price, position, enter_position):
    """A function that returns the average price.
    """
    avg_prices = []
    for i in range(len(price)):
        # The average price remains the same as before if we do not buy anything.
        if enter_position[i] == 0:
            try:
                avg_price = avg_prices[i - 1]
            except:
                avg_price = 0
        else:
            enter_value = price[i] * enter_position[i]
            prev_value = 0 if i == 0 else position[i -1] * avg_prices[i - 1]
            value = prev_value + enter_value
            avg_price = value / position[i]
        avg_prices.append(avg_price)
    return avg_prices

def transaction_fee(enter, exit, transaction_cost):
    """A function that returns transaction costs. We currently assume 0.
    """
    if enter != 0 or exit != 0:
        return transaction_cost
    else:
        return 0