import matplotlib.pyplot as plt

ylist = [1, 12, 32, 91, 28, 4, 20, 180, 97, 77]
xlist = ['jorge', 'Rob', 'Jerry', 'Duke', 'Clary', 'Rodger', 'Corey', 'Gary', 'Patrick', 'Sandy']

plt.xlabel('This is the X label')
plt.ylabel('This is the Y label')

plt.title('This is the title!')

plt.plot(xlist, ylist, "r--")  # colour, s = square, o = circle, ^ = triangle, -- = dotted line,

plt.show()
