import numpy as np
import matplotlib.pyplot as plt


def get_union():
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    intersection_array = np.intersect1d(a, b)
    print(intersection_array)

def make_matrix():
    b = np.arange(1,16)
    print(b.reshape(5,3, order='F'))

def flatten_matrix():
    b = np.arange(1,16).reshape(5,3, order='F')
    print(b)

    transposed_b = np.transpose(b)
    print(transposed_b)

    flattened = transposed_b.flatten()
    print(flattened)

def three_d_array():
    # problem 4
    b = np.arange(1,16).reshape(5,3, order='F')
    flattened = np.transpose(b).flatten()
    c = flattened.reshape(3,1,5)
    print(c)
    # problem 5
    d = c.flatten()
    d = d.reshape(5,3, order='F')
    print(d)
def np_difference():
    a = np.array([12, 5, 7, 15, 3, 1, 8])
    b = np.array([14, 6, 3, 11, 19, 12, 5])
    a = np.setdiff1d(a,b)
    print(a)



def plot_example():
    t = np.r_[0:10:.1]
    frequency = .5
    x = np.sin(2*np.pi*frequency*t)
    plt.plot(t, x)
    plt.xlabel('time')
    plt.ylabel('values')
    plt.show()

np_difference()