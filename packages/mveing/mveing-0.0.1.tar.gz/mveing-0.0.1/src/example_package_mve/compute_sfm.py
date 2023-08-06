import os
import computesfm
import math
from compute_camspairCC import *

# def create_new_testlist(testlist, defaut_scan):
#     with open(testlist) as f:
#         scans = f.readlines()
#         scans = [line.rstrip() for line in scans]
#
#     for i in range(len(defaut_scan)):
#         scans.remove(defaut_scan[i])
#
#     new_testlist = testlist[:10]+"test_new.txt"
#     with open(new_testlist, 'w') as f:
#         for i in range(len(scans)):
#             f.write(str(scans[i]) + '\n')


def cams_deal(output_file):
    cams_save_path=output_file + "/cams_1/"
    if(os.path.exists(cams_save_path)==False):
        os.mkdir(cams_save_path)
    views_dir = output_file + '/sfm/views/'
    views = os.listdir(views_dir)
    for i in range(0, len(views)):
        cam_file = views_dir + "/view_"+"{:0>4d}".format(i)+".mve/meta.ini"
        cam_save_file = cams_save_path +"/{:0>8d}".format(i)+"_cam.txt"
        with open(cam_file) as f:
            lines = f.readlines()
            if (len(lines)<9):
                pass
            else:
                R = [float(x) for x in lines[7].rstrip().split()[2:11]]
                T = [float(x) for x in lines[8].rstrip().split()[2:5]]
                with open(cam_save_file, 'w') as f:
                    f.write('extrinsic\n')
                    f.write(str(R[0]) + ' ' + str(R[1]) + ' ' + str(R[2]) + ' ' + str(T[0]*122) + '\n')  # 122 can be changed???
                    f.write(str(R[3]) + ' ' + str(R[4]) + ' ' + str(R[5]) + ' ' + str(T[1]*122) + '\n')
                    f.write(str(R[6]) + ' ' + str(R[7]) + ' ' + str(R[8]) + ' ' + str(T[2]*122) + '\n')
                    f.write('0.0 0.0 0.0 1.1\n')
                    f.write('\n')
                    f.write('intrinsic\n')
                    f.write('2500 0 800\n')
                    f.write('0 2500 600\n')
                    # f.write('2892.33 0 823.205\n')
                    # f.write('0 2883.18 619.071\n')
                    f.write('0 0 1\n')
                    f.write('\n')
                    f.write('425 935')

def compute_numofcam(img_dir_path, cams_path):
    images_dir = os.listdir(img_dir_path)
    num_images = len(images_dir)
    out_file = cams_path + "/synth_0.out"
    count_1 = 0
    with open(out_file) as f:
        f.readline()
        f.readline()
        for i in range(num_images * 5):
            line = f.readline()
            line0 = float(line.split()[0])
            if (line0 != 0):
                count_1 = count_1 + 1
    num_of_cam = math.ceil(count_1/5)
    return num_of_cam

# compute cameras
def computecams(output_file, n_views):

    img_dir_path = output_file + "/images/"
    cams_path = output_file + "/sfm/"
    if (not os.path.exists(cams_path)):
        os.makedirs(cams_path)

    #step1
    re = computesfm.computesfm(img_dir_path, cams_path)

    # try 3 times
    num = 0
    while (compute_numofcam(img_dir_path, cams_path) < n_views and num < 3):
        re = computesfm.computesfm(img_dir_path, cams_path)
        num = num+1
    if(compute_numofcam(img_dir_path, cams_path) < n_views):
        return -1

    #step2
    cams_deal(output_file)

    ## #step3
    ## compute_pair(scan_path)  # laofangfa

    # step3. another type C++kuhanshu
    compute_campair(output_file, n_views-1)

    return 0