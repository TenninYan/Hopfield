 # -*- coding: utf-8 -*-
import numpy as np
import random
import copy

# parameter to chage
use_num = 6
noise_percent = 0.1

# fixed number
data_num = 6
data_size = 25

answer = np.array(["A","C","E","H","I","X"])
raw_data = np.array(
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
         -1,1,1,1,-1],
        # X
        [1,-1,-1,-1,1,
         -1,1,-1,1,-1,
         -1,-1,1,-1,-1,
         -1,1,-1,1,-1,
         1,-1,-1,-1,1]])
data = raw_data.reshape((data_num,data_size,1))


def print_dot(data):
    for i in range(data_size):
        if data[i] == 1:
            print "*",
        else:
            print " ",
        if i%5 == 4:
            print ""

def calculate_w():
    global W
    W = np.zeros((data_size,data_size))
    for i in range(use_num):
        W = W + data[i].dot(data[i].transpose())
        # W = (train_data[i].transpose()).dot(train_data[i])
    for i in range(data_size):
        W[i][i] = 0
    # print W

def make_noise():
    noise_data = copy.deepcopy(data[:use_num])
    for num in range(use_num):
        for i in range(data_size):
            if random.random() < noise_percent:
                noise_data[num][i] *= -1
                # if random.randint(1,2) == 1:
                #     noise_data[i] = -1
                # else:
                #     noise_data[i] = 1
    return noise_data

def erase_noise(noise_data):
    for num in range(use_num):
        for num_trial in range(1000):
            place2change = random.randint(0,24)
            ans = W[place2change].dot(noise_data[num])
            # print ans
            if ans > 0:
                noise_data[num][place2change] = 1
            elif ans < 0:
                noise_data[num][place2change] = -1
            # if num_trial%15 == 0:
        # print_dot(noise_data[num])
        check_same(noise_data[num],num)

def check_same(check_data,num):
    # print check_data,data[num]
    if np.array_equal(check_data,data[num]):
        good_num[num] +=1
        # print "o"*10
        # return 1
    else:
        print_dot(noise_data[num])
        print "it should be " + answer[num]
        # print "x"*10
        # return 0


if __name__ == "__main__":
    # for i in range(data_num):
    #     print_dot(data[i])
    calculate_w()

    global good_num
    good_num = np.zeros(use_num)

    for i in range(100):
        noise_data = make_noise()
        erase_noise(noise_data)
    print good_num
    print np.average(good_num)

