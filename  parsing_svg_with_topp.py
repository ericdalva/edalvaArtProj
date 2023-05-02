## test parsing svg points with gerrys topp.py

#import pandas as pd
#import scipy.signal
import toppra as ta
import util 
import topp 

import topp

import svgpathtools
import numpy as np
import matplotlib.pyplot as plt
paths, attributes = svgpathtools.svg2paths('/home/gchen328/GIT_REPOS/ericwork/edalvaArtProj/adversarial_example_BnW_BnW.svg')
path = paths[0]

#lets see some points
num_points = 10

test = np.linspace(0,1,num_points)

points = path[0].points(test)

# print(type(points), type(points[0]), points.shape, len(path))

x = np.zeros(num_points)
y = np.zeros(num_points)

for index, point in enumerate(points) :
    x[index] = point.real
    y[index] = point.imag

for curve in path[1:] :
    points = curve.points(test)
    xtemp = np.zeros(num_points)
    ytemp = np.zeros(num_points )
    for index, point in enumerate(points) : 
        xtemp[index] = point.real
        ytemp[index] = point.imag
    x = np.append(x,xtemp)
    y = np.append(y,ytemp)


#visualize path
plt.plot(x, y)
plt.savefig("test")

# now we pass this to gerrys stroke some how, 
# looks like io. load log just returns pd dataframe, jk there is a to numpy call  
print(x.shape)
# I think the end result of his processing is something like 
#ok he gets: time, x, y for his strokes, stroke2txs just breaks off the 1st column
#so lets make that, call his code and see if we get the same thing

print(type(x))
time = np.linspace(0,7,70)
print(time.shape)
strokes = np.vstack((time,x,y))
strokes = strokes.T
print (strokes.shape)

# moment of truth 

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
t, xy = util.stroke2tx(strokes)
xydot, xyddot = util.derivatives(t, xy)
axes[0].plot(*xy.T)
axes[1].plot(t, np.linalg.norm(xydot, axis=1))
axes[2].plot(t, np.linalg.norm(xyddot, axis=1))

axes[0].axis('equal')
axes[0].set_title('xy')
axes[1].set_title('Speed vs time')
axes[2].set_title('||Acceleration|| vs time');

plt.savefig("test")

# I think i can literally just call this a stroke

stroke = topp.Stroke(strokes, clean=True)
stroke.spline_interp()
stroke.retime(vmax=1, amax=15)

ts, xs, xds, xdds = stroke.sample_retimed(N=200)

# Plot TOPP-RA results
# fig, axes = plt.subplots(3, 2, figsize=(5, 6))
fig, axes = plt.subplots(3, 2, figsize=(15, 16))
stroke.plot_xva(axes)
fig.tight_layout()

plt.savefig("retimed")
