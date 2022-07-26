#!/usr/bin/env python3

import sys
import math
import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt

RED=0
GREEN=1
BLUE=2

def mosaic(channel, steps):
    rows = channel.shape[0]
    cols = channel.shape[1]

    pos = np.array([])
    path = np.empty((steps, 2), dtype=np.uint8)

    for t in range(steps):
        if t == 0:
            init_row = np.random.randint(int(rows/2)-1, int(rows/2)+2)
            init_col = np.random.randint(int(cols/2)-1, int(cols/2)+2)
            pos = np.array([init_row, init_col])
        else:
            opt = []
            for row in range(pos[0]-1, pos[0]+2):
                for col in range(pos[1]-1, pos[1]+2):
                    if (row < 0) | (row >= rows) | (col < 0) | (col >= cols) | (row == pos[0]) & (col == pos[1]):
                        pass
                    else:
                        opt.append([row, col])

            opt = np.array(opt)
            np.random.shuffle(opt)
            pos = opt[0]

        path[t] = pos

    t = 0
    for step in path:
        step_val = 1.0 * math.pow(0.95, t)
        if channel[step[0]][step[1]] < step_val:
            channel[step[0]][step[1]] = step_val
            t += 1

            surround_val = step_val * 0.95
            for row in range(step[0]-1, step[0]+2):
                for col in range(step[1]-1, step[1]+2):
                    if (row >= 0) & (row < rows) & (col >= 0) & (col < cols):
                        if channel[row][col] < surround_val:
                            channel[row][col] = surround_val

    return channel

def mosaic_test():
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    steps = int(sys.argv[3])

    red = np.zeros((rows, cols))
    red = mosaic(red, steps)

    green = np.zeros((rows, cols))
    green = mosaic(green, steps)

    blue = np.zeros((rows, cols))
    blue = mosaic(blue, steps)

    img = (np.dstack((red, green, blue)) * 255.999).astype(np.uint8)
    smo = scipy.ndimage.gaussian_filter(img, sigma=0.90)

    plt.subplot(1, 5, 1)
    plt.imshow(red)
    plt.subplot(1, 5, 2)
    plt.imshow(green)
    plt.subplot(1, 5, 3)
    plt.imshow(blue)
    plt.subplot(1, 5, 4)
    plt.imshow(img)
    plt.subplot(1, 5, 5)
    plt.imshow(smo)
    plt.show()

# --- #

def spiral(num_of_revolutions, iterations, noise):
    x = []
    y = []

    angle_increment = num_of_revolutions * 2 * math.pi / iterations
    for i in range(iterations):
        angle = angle_increment * i
        n = i / iterations * np.random.randint(-noise, noise+1)
        x.append(int(angle * n * math.cos(angle) + n))
        y.append(int(angle * n * math.sin(angle) + n))

    x = np.array(x)
    y = np.array(y)

    x += np.abs(np.min(x))
    y += np.abs(np.min(y))

    frame = np.zeros([np.max(y)+1, np.max(x)+1])
    for i in range(iterations):
        frame[y[i]][x[i]] = (-1.0 / iterations) * i + 1.0

        for pos_y in range(y[i]-1, y[i] + 2):
            for pos_x in range(x[i]-1, x[i]+2):
                if (pos_y >= 0) & (pos_y < frame.shape[0]) & (pos_x >= 0) & (pos_x < frame.shape[1]):
                    surround = frame[y[i]][x[i]] * 0.50
                    if frame[pos_y][pos_x] < surround:
                        frame[pos_y][pos_x] = surround
    return frame

def spiral_test():
    red_spiral = spiral(10, 10000, 2)
    green_spiral = spiral(10, 10000, 2)
    blue_spiral = spiral(10, 10000, 2)

    spiral_y_size = red_spiral.shape[0]
    spiral_x_size = red_spiral.shape[1]

    red = np.zeros([spiral_y_size * 3, spiral_x_size * 3])
    green = np.zeros([spiral_y_size * 3, spiral_x_size * 3])
    blue = np.zeros([spiral_y_size * 3, spiral_x_size * 3])

    for i in range(3):
        init_y = np.random.randint(int(spiral_y_size * 3 / 2) - 5, int(spiral_y_size * 3 / 2) + 6)
        init_x = np.random.randint(int(spiral_x_size * 3 / 2) - 5, int(spiral_x_size * 3 / 2) + 6)

        end_y = init_y + spiral_y_size
        end_x = init_x + spiral_x_size

        if end_y >= spiral_y_size * 3:
            end_y = spiral_y_size * 3
        if end_x >= spiral_x_size * 3:
            end_x = spiral_x_size * 3

        for y in range(init_y, end_y):
            for x in range(init_x, end_x):
                if i == RED:
                    red[y][x] = red_spiral[y-init_y][x-init_x]
                elif i == GREEN:
                    green[y][x] = green_spiral[y-init_y][x-init_x]
                else:
                    blue[y][x] = blue_spiral[y-init_y][x-init_x]

    img = (np.dstack((red, green, blue)) * 255.999).astype(np.uint8)
    plt.imshow(img)
    plt.show()

# --- #

if __name__ == "__main__":
#    mosaic_test()
    spiral_test()


