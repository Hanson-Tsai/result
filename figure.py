import matplotlib.pyplot as plt
import csv
import numpy as np

TYPE = 'total'
METHOD = 'ONVM'

y = []
count = 0

with open('/home/hstsai/onvm/result/' + TYPE + '.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in lines:
        y.extend(row)

# plt.plot(list(range(len(y))), y, color='g',
#          linestyle='dashed', marker='.', label=TYPE)
array_y = np.asarray(y)
percentile_y = np.percentile(array_y, 98)
avg = sum(y)/len(y)

plt.plot(list(range(len(y))), y, '.', label=TYPE)
plt.xticks(rotation=25)
plt.xlabel('times')
plt.ylabel('latency(ms)')
plt.ylim(0, percentile_y)
plt.axhline(avg, color='red',
            linestyle='--', linewidth=3, label='Avg: ' + str(avg))
plt.title(METHOD+' '+TYPE+' latency', fontsize=20)
plt.grid()
plt.legend()
plt.show()
plt.savefig('/home/hstsai/onvm/result/' + TYPE + '.png')
