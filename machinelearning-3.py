import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.rand(greyhounds)
lab_height = 24 + 4 * np.random.rand(labs)




N = 500
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, grey_height, width, color='#d62728')
p2 = plt.bar(ind, lab_height, width,bottom=grey_height)
plt.ylabel('Scores')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()