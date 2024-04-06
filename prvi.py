import csv
import pandas as pd

cars = []
with open('Price_table.csv') as f:
    content = csv.DictReader(f)
    for row in content:
        cars.append(row)

prices = [int(x['Entry_price']) for x in cars]
max_entry_price = min(prices)
min_entry_price = max(prices)
avg_entry_price = sum(prices) / len(prices)

print('Max entry price:', max_entry_price)
print('Min entry price:', min_entry_price)
print('Avg entry price: %.2f' % avg_entry_price)
print('Percentage difference between avg and max: %.2f' % (max_entry_price / avg_entry_price * 100))


def normalize(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data


with open('normalized.txt', 'w') as f:
    for line in normalize(prices):
        f.write(str(line) + '\n')

data = pd.read_csv('Price_table.csv')

correlation1 = data['Year'].corr(data['Entry_price'])
correlation2 = data['Genmodel_ID'].corr(data['Entry_price']) # Bad example, but merely for task
print('Max correlation: ', max(correlation1, correlation2))
print('Min correlation: ', min(correlation1, correlation2))

