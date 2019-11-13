# -*- coding: utf-8 -*-
"""
Created  2019  11 11

@author  zhaoshuo

"""

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

import numpy as np
import os


def plot_slip(path, num, name):

    a = np.loadtxt(path,str,skiprows=1)  # 获取txt str可以读字符串 跳过前24行

    GPS_PRN = locals()
    for i in range(32):
        GPS_PRN['G' + str(i)] = a[:,i]  # 动态生成变量名

    for i in range(1,32):
        # print(GPS_PRN.get('G'+str(i)))  # 调用-test
        GPS_PRN['G' + str(i)] = np.array(GPS_PRN.get('G'+str(i)), dtype='float_')

        slip = GPS_PRN['G' + str(i)]

        if  slip.mean() == -99.0:
            print(GPS_PRN['G' + str(i)].mean)
            continue

        scale_y = 5

        epoch = GPS_PRN['G' + str(i)].size


        lim1 = [1] * epoch


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份

        fig = plt.figure(num)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GPS_PRN['G' + str(i)], "r.")

        plt.plot(lim1, "m--")


        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("周跳估值/周", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('G' + str(i)), font2)
        plt.ylim(0, scale_y)
        plt.grid("on")
        plt.savefig('G' + str(i)+"-slip" , dpi=300)

def plot_resc(path, num, name):

    a = np.loadtxt(path,str,skiprows=1)  # 获取txt str可以读字符串 跳过前24行

    GPS_PRN = locals()
    for i in range(32):
        GPS_PRN['G' + str(i)] = a[:,i]  # 动态生成变量名

    for i in range(1,32):
        # print(GPS_PRN.get('G'+str(i)))  # 调用-test
        GPS_PRN['G' + str(i)] = np.array(GPS_PRN.get('G'+str(i)), dtype='float_')

        resc = GPS_PRN['G' + str(i)]

        if  resc.mean() == -99.0:
            print(GPS_PRN['G' + str(i)].mean)
            continue

        scale_y = 2

        epoch = GPS_PRN['G' + str(i)].size


     #   lim1 = [1] * epoch


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份

        fig = plt.figure(num)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GPS_PRN['G' + str(i)], "r.")

    #    plt.plot(lim1, "m--")


        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("Residual/m", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('G' + str(i)), font2)
        plt.ylim(-scale_y, scale_y)
        plt.grid("on")
        plt.savefig('G' + str(i)+"-resc" , dpi=300)


if __name__ == '__main__':
    i = 0

    pathlist = os.listdir()
    for file in pathlist:
        if file.endswith(".slip"):
            print("开始绘制周跳文件",file)
            name = file[0:9]  # 传进去文件名字
            plot_slip(file,i,name)
            i = i + 1
        elif file.endswith(".resc"):
            print("开始绘制相位残差文件", file)
            name = file[0:9]  # 传进去文件名字
            plot_resc(file, i, name)
            i = i + 1
