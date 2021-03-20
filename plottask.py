#Program that plots the following functions in the range [0, 4]:
#f(x) = x
#g(x) = x**2
#h(x) = x**3
#The plots must use the same set of axis
#Author: Caio Forte Ribeiro

import numpy as np
import matplotlib.pyplot as plt

#x goes from 0(inclusive) to 5 (not inclusive)
x = np.array([0, 1, 2, 3, 4])

#define f(x), g(x), and h(x)
f = x
g = x**2
h = x**3

#Set font family, colour and size for title and axis
#Color palette source: https://learnui.design/tools/data-color-picker.html#palette
fontTitle = {"family": "calibri", 
             "color" : "#342e2e", 
             "size": "18"
             }

fontAxis = {"family": "calibri",
            "color" : "#342e2e", 
            "size": "12"
            }

#Customise background colour and width of line
plt.rcParams["axes.facecolor"] = "#f5f5f5"
plt.rcParams["lines.linewidth"] = 3
plt.rcParams["figure.facecolor"] = "#f5f5f5"

#Set title and axis labels
plt.title("Plots", fontdict = fontTitle)
plt.xlabel("x", fontdict = fontAxis) 
plt.ylabel("Functions", fontdict = fontAxis)

#Customise colours and labels of the plotting
plt.plot(x, f, color = "#58508d", label = "$f(x) = x$")
plt.plot(x, g, color = "#ff6361", label = "$g(x) = x^{2}$")
plt.plot(x, h, color = "#ffa600", label = "$h(x) = x^{3}$")

#Adds a legend
plt.legend()

#Adds a grid
plt.grid()

#Displays the resulting figure
plt.show()