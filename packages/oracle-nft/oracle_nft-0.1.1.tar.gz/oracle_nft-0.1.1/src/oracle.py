from helpers import fetchData, average_list, random_range
import numpy as np


def oracle_calculator(contract, marketplaces, start, end):
    end_hours, start_hours = random_range(end, start)
    price_entries = fetchData(contract, marketplaces, start_hours, end_hours)

    print('Received query list:')
    print(price_entries)
    print('\nData filtering...\n')

    average = average_list(price_entries)

    # Data filtering
    for price in price_entries:
        if price < 0.1 * average or price > 9 * average:
            print('Removing price {} as it is a extremely low or high value'.format(price))
            price_entries.remove(price)
    
    price_entries.sort()

    # Truncated average with 10%
    number_to_remove = round(len(price_entries) * 0.1)
    price_entries = price_entries[number_to_remove:-number_to_remove]

    truncated_average = average_list(price_entries)
    truncated_std = np.std(price_entries)

    print("Truncated standard deviation of list: % s "% (truncated_std))
    print("Truncated average of list: {}\n".format(truncated_average))

    prices = []
    sensitivity = 1

    for price in price_entries:
        if truncated_average - (sensitivity * truncated_std) <= price <= truncated_average + (sensitivity * truncated_std):
            prices.append(price)


    print('Final price list: ')
    print(prices)
    print('\n----------------------')
    print('Oracle price: {}'.format(np.format_float_positional(average_list(prices), trim='-')))
    print('----------------------')
