 # -*- coding: utf-8 -*-
import numpy as np
# from numpy import linalg as la

data_num = 6
use_num = 2

train_data = np.array(
        # A
        [[-1,-1,1,-1,-1,
         -1,1,-1,1,-1,
         1,-1,-1,-1,1, 
         1,1,1,1,1,
         1,-1,-1,-1,1],
        # C
        [-1,1,1,1,-1,
         1,-1,-1,-1,1,
         1,-1,-1,-1,-1,
         1,-1,-1,-1,1,
         -1,1,1,1,-1],
        # E
        [1,1,1,1,1,
         1,-1,-1,-1,-1,
         1,1,1,1,-1,
         1,-1,-1,-1,-1,
         1,1,1,1,1],
        # G
        [-1,1,1,1,-1,
         1,-1,-1,-1,-1,
         1,-1,1,1,1,
         1,-1,-1,-1,1,
         -1,1,1,1,1],
        # H
        [1,-1,-1,-1,1,
         1,-1,-1,-1,1,
         1,1,1,1,1,
         1,-1,-1,-1,1,
         1,-1,-1,-1,1],
        # I
        [-1,1,1,1,-1,
         -1,-1,1,-1,-1,
         -1,-1,1,-1,-1,
         -1,-1,1,-1,-1,
         -1,1,1,1,-1]])


def print_dot(data):
    for i in range(5):
        for j in range(5):
            if data[i][j] == 1:
                print "*",
            else:
                print " ",
        print ""
    print ""


def calculate_w(main_data):
    W = np.zeros((25,25))
    w_data = train_data.reshape((data_num,25,1))
    for i in range(use_num):
        W = W + w_data[i].dot(w_data[i].transpose())
        # W = (train_data[i].transpose()).dot(train_data[i])
    for i in range(25):
        W[i][i] = 0
    print W




if __name__ == "__main__":
    main_data = train_data.reshape((data_num,5,5))
    # for i in range(data_num):
    #     print_dot(main_data[i])
    calculate_w(main_data)

