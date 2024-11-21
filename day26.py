import matplotlib.pyplot as pyplot
labels=('python','java','scala','c#','c++')
sizes=[25,30,20,10,15]
pyplot.pie(sizes,
labels=labels,
autopct='%1.f%%',
counterclock=False,
startangle=105)

pyplot.show()