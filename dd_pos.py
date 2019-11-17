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

        fig = plt.figure(num*31+i)   # 这个是让他每一张图都生成

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
        plt.savefig('slip/'+'G' + str(i)+"-slip" , dpi=300)
        plt.close(fig)  # 改善内存问题

def plot_resc(path, num, name):

    a = np.loadtxt(path,str,skiprows=1)  # 获取txt str可以读字符串 跳过前24行

    GPS_PRN = locals()
    BDS_PRN = locals()
    GAL_PRN = locals()

    for i in range(1,32):
        GPS_PRN['G' + str(i)] = a[:,i]  # 动态生成变量名

    for i in range(96,130):
        BDS_PRN['B' + str(i)] = a[:, i]

    for i in range(60,95):
        GAL_PRN['E' + str(i)] = a[:, i]



    for i in range(1,32):

        GPS_PRN['G' + str(i)] = np.array(GPS_PRN.get('G'+str(i)), dtype='float_')

        resc = GPS_PRN['G' + str(i)]

        if  resc.mean() == -99.0:
            print(GPS_PRN['G' + str(i)].mean)
            continue

        scale_y = 0.005

        epoch = GPS_PRN['G' + str(i)].size


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GPS_PRN['G' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("Residual/m", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('G' + str(i)), font2)
        plt.ylim(-scale_y, scale_y)
        plt.grid("on")
        plt.savefig('resc/'+'G' + str(i)+"-resc" , dpi=300)
        plt.close(fig) # 改善内存问题

    for i in range(60,95):  # GAL部分

        GAL_PRN['E' + str(i)] = np.array(GAL_PRN.get('E' + str(i)), dtype='float_')

        resc = GAL_PRN['E' + str(i)]

        if resc.mean() == -99.0:
            #   print(BDS_PRN['G' + str(i)].mean)
            continue

        scale_y = 0.005

        epoch = GAL_PRN['E' + str(i)].size

        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GAL_PRN['E' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("Residual/m", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('E' + str(i - 59)), font2)
        plt.ylim(-scale_y, scale_y)
        plt.grid("on")
        plt.savefig('resc/'+'E' + str(i - 59) + "-resc", dpi=300)
        plt.close(fig)  # 改善内存问题

    for i in range(96,130):  # BDS部分

        BDS_PRN['B' + str(i)] = np.array(BDS_PRN.get('B'+str(i)), dtype='float_')

        resc = BDS_PRN['B' + str(i)]

        if  resc.mean() == -99.0:
         #   print(BDS_PRN['G' + str(i)].mean)
            continue

        scale_y = 0.005

        epoch = BDS_PRN['B' + str(i)].size


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, BDS_PRN['B' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("Residual/m", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('B' + str(i-95)), font2)
        plt.ylim(-scale_y, scale_y)
        plt.grid("on")
        plt.savefig('resc/'+'B' + str(i-95)+"-resc" , dpi=300)
        plt.close(fig)  # 改善内存问题



def plot_resp(path, num, name):

    a = np.loadtxt(path,str,skiprows=1)  # 获取txt str可以读字符串 跳过前24行

    GPS_PRN = locals()
    BDS_PRN = locals()
    GAL_PRN = locals()

    for i in range(1, 32):
        GPS_PRN['G' + str(i)] = a[:, i]  # 动态生成变量名

    for i in range(96, 130):
        BDS_PRN['B' + str(i)] = a[:, i]

    for i in range(60, 95):
        GAL_PRN['E' + str(i)] = a[:, i]


    for i in range(1,32):

        GPS_PRN['G' + str(i)] = np.array(GPS_PRN.get('G'+str(i)), dtype='float_')

        resp = GPS_PRN['G' + str(i)]

        if  resp.mean() == -99.0:
            print(GPS_PRN['G' + str(i)].mean)
            continue

        scale_y = 2

        epoch = GPS_PRN['G' + str(i)].size


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GPS_PRN['G' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("Residual/m", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('G' + str(i)), font2)
        plt.ylim(-scale_y, scale_y)
        plt.grid("on")
        plt.savefig('resp/'+'G' + str(i)+"-resp" , dpi=300)
        plt.close(fig)  # 改善内存问题

    for i in range(60, 95):  # GAL部分

        GAL_PRN['E' + str(i)] = np.array(GAL_PRN.get('E' + str(i)), dtype='float_')

        resp = GAL_PRN['E' + str(i)]

        if resp.mean() == -99.0:
            #   print(BDS_PRN['G' + str(i)].mean)
            continue

        scale_y = 2

        epoch = GAL_PRN['E' + str(i)].size

        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GAL_PRN['E' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("Residual/m", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('E' + str(i - 59)), font2)
        plt.ylim(-scale_y, scale_y)
        plt.grid("on")
        plt.savefig('resp/'+'E' + str(i - 59) + "-resp", dpi=300)
        plt.close(fig)  # 改善内存问题

    for i in range(96,130):  # BDS部分

        BDS_PRN['B' + str(i)] = np.array(BDS_PRN.get('B'+str(i)), dtype='float_')

        resc = BDS_PRN['B' + str(i)]

        if  resc.mean() == -99.0:
         #   print(BDS_PRN['G' + str(i)].mean)
            continue

        scale_y = 2

        epoch = BDS_PRN['B' + str(i)].size


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, BDS_PRN['B' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("Residual/m", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('B' + str(i-95)), font2)
        plt.ylim(-scale_y, scale_y)
        plt.grid("on")
        plt.savefig('resp/'+'B' + str(i-95)+"-resp" , dpi=300)
        plt.close(fig)  # 改善内存问题


def plot_ele(path, num, name):

    a = np.loadtxt(path,str,skiprows=1)  # 获取txt str可以读字符串 跳过前24行

    GPS_PRN = locals()
    BDS_PRN = locals()
    GAL_PRN = locals()

    for i in range(1,32):
        GPS_PRN['G' + str(i)] = a[:, i]  # 动态生成变量名

    for i in range(96, 130):
        BDS_PRN['B' + str(i)] = a[:, i]

    for i in range(60, 95):
        GAL_PRN['E' + str(i)] = a[:, i]

    for i in range(1,32):

        GPS_PRN['G' + str(i)] = np.array(GPS_PRN.get('G'+str(i)), dtype='float_')

        ele = GPS_PRN['G' + str(i)]

        if  ele.mean() == -99.0:
            print(GPS_PRN['G' + str(i)].mean)
            continue

        scale_y = 90

        epoch = GPS_PRN['G' + str(i)].size


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GPS_PRN['G' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("ele", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('G' + str(i)), font2)
        plt.ylim(15, scale_y)
        plt.grid("on")
        plt.savefig('ele/'+ 'G' + str(i)+"-ele" , dpi=300)
        plt.close(fig)  # 改善内存问题

    for i in range(60, 95):  # GAL部分

        GAL_PRN['E' + str(i)] = np.array(GAL_PRN.get('E' + str(i)), dtype='float_')

        ele = GAL_PRN['E' + str(i)]

        if ele.mean() == -99.0:
            #   print(BDS_PRN['G' + str(i)].mean)
            continue

        scale_y = 90

        epoch = GAL_PRN['E' + str(i)].size

        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(num * 32 + 67 + i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, GAL_PRN['E' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("ele", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('E' + str(i - 59)), font2)
        plt.ylim(15, scale_y)
        plt.grid("on")
        plt.savefig('ele/'+'E' + str(i - 59) + "-ele", dpi=300)
        plt.close(fig)  # 改善内存问题

    for i in range(96, 130):  # BDS部分

        BDS_PRN['B' + str(i)] = np.array(BDS_PRN.get('B' + str(i)), dtype='float_')

        ele = BDS_PRN['B' + str(i)]

        if  ele.mean() == -99.0:
          #  print(BDS_PRN['G' + str(i)].mean)
            continue

        scale_y = 90

        epoch = BDS_PRN['B' + str(i)].size


        x = np.linspace(0, epoch, epoch)  # 0到24 分240份i

        fig = plt.figure(i)

        fig.set_size_inches(8, 4)
        fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

        plt.plot(x, BDS_PRN['B' + str(i)], "r.")

        font2 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 15,
                 }

        plt.ylabel("ele", font2)
        plt.xlabel("epoch", font2)
        plt.title(format('B' + str(i-95)), font2)
        plt.ylim(15, scale_y)
        plt.grid("on")
        plt.savefig('ele/'+'B' + str(i-95)+"-ele" , dpi=300)
        plt.close(fig)  # 改善内存问题


if __name__ == '__main__':
    i = 0

    pathlist = os.listdir()
    for file in pathlist:
        if file.endswith(".slip"):
            print("开始绘制周跳文件",file)
            name = file[0:9]  # 传进去文件名字
    #        plot_slip(file,i,name)
            i = i + 1
        elif file.endswith(".resc"):
            print("开始绘制相位残差文件", file)
            name = file[0:9]  # 传进去文件名字
            plot_resc(file, i, name)
            i = i + 1
        elif file.endswith(".resp"):
            print("开始绘制伪距残差文件", file)
            name = file[0:9]  # 传进去文件名字
            plot_resp(file, i, name)
            i = i + 1
        elif file.endswith(".ele"):
            print("开始绘制高度角文件", file)
            name = file[0:9]  # 传进去文件名字
            plot_ele(file, i, name)
            i = i + 1

