import numpy as np
import matplotlib.pyplot as plt


# Plotting in matplotlib can be done in either of two ways, which ones? Whoch way is the recommended approach?
    # Objektorienterade = metod som används för att skapa figur- och axelobjekt med fig, ax = plt.subplots()
    # Pyplot = metod som använder plt för att direkt skapa funktioner som plt.show() och plt.plot()
    # Vilken rekommenderas?
      # Objektorienterade då den ger mer kontroll, strukturerad kod och flexibilitet speciellt när man arbetar med mer avancerade grafer och vid behov av att skapa flera diagram i samma figur
    

# Explain shortly what a figure, axes, axis and an artist is in matplotlib
    # Figure - hela rutan eller fönstret för garferna
    # Axes - där graferna ritas
    # Axis - x och y axlarna
    # Artist - exempelvis linjer och text som ritas på axis


# When plotting in matplotlib, what is the expected input data type?
    # Numerisk data, alltså listor, pandas strukturer och numpy arrayer


# Create a plot of the function y = x^2 [from -4 to 4, hint use the np.linspace function] both in the object-oriented approach and the pyplot approach. Your plot should have a title and axis-labels.
# Object oriented
# för att skapa x värden från -4 till 4
x = np.linspace(-4, 4, 100)
y = x**2
# för att skapa figur och axlar
fig, ax = plt.subplots()
# för att rita grafen
ax.plot(x, y)
# för titlar och labels
ax.set_title('Grafen för y = x^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
# för att visa grafen
plt.show()

# Pyplot
# för att skapa x värden från -4 till 4
x = np.linspace(-4, 4, 100)
y = x**2
# för att rita grafen
plt.plot(x, y)
# för titlar och labels
plt.title('Grafen för y = x^2')
plt.xlabel('x')
plt.ylabel('y')
# ör att visa grafen
plt.show()


# Create a figure containing 2  subplots where the first is a scatter plot and the second is a bar plot. You have the data below. 
# Data for scatter plot
np.random.seed(15)
random_data_x = np.random.randn(1000)
random_data_y = np.random.randn(1000)
x = np.linspace(-2, 2, 100)
y = x**2
# för att skapa en figur och lägga till två subplots
fig, axs = plt.subplots(1, 2, figsize=(12,6))
# Scatter plot
axs[0].scatter(random_data_x, random_data_y, color='green', alpha=0.5)
axs[0].set_title('Scatter Plot')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
# Data for bar plot
fruit_data = {'grapes': 22, 'apple': 8, 'orange': 15, 'lemon': 20, 'lime': 25}
names = list(fruit_data.keys())
values = list(fruit_data.values())
# Bar Plot
axs[1].bar(names, values, color=('brown'))
axs[1].set_title('Bar Plot')
axs[1].set_xlabel('Fruit')
axs[1].set_ylabel('Count')