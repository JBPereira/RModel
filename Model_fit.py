import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')



with open('data_nick2CostsClicksVisitsDateStrategy.csv', 'rb') as csvfile:
     dataset = pd.read_table(csvfile, delimiter=';' )
     #dataset = pd.DataFrame(dataset)

example_line_item = dataset[dataset.strategy_id == 7487]
example_line_item = example_line_item[dataset.clicks > 0]
print example_line_item

example_clicks = pd.Series(example_line_item.clicks)
plt.figure()
print example_clicks[8043]

plt.plot(example_clicks[2:])

smoothed_example = []

for i in range(2, len(example_clicks)):
     smoothed_example.append(0)
     for j in range(0,3):
          smoothed_example[i-2] += example_clicks[i-j]
     smoothed_example[i-2] /= 3

plt.plot(smoothed_example, 'color', 'b')


plt.show()