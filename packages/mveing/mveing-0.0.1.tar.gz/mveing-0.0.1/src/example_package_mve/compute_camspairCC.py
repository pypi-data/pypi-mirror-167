import os
import math
import numpy as np
import computecampair

def write_pairs(output_file, camspair_list, num_src, pairfile_num):
    pair_path = output_file + "/pair.txt"
    with open(pair_path, 'w') as f:
        f.write(str(pairfile_num)+'\n')
        for i in range(len(camspair_list)):
            if(type(camspair_list[i]) != type(0)):
                f.write(str(i)+'\n')
                f.write(str(num_src) + ' ')
                for j in range(num_src):
                    f.write(str(camspair_list[i][j]) + ' ')
                    f.write(str(0.99) + ' ')
                f.write("\n")

def pairs_to_pair(output_file, campairfile, num_src):
    images_path = output_file + "/images/"
    images_dir = os.listdir(images_path)
    num_images = len(images_dir)
    camspair_list = [0] * (num_images)

    pair_dir = os.listdir(campairfile)
    pairfile_num = len(pair_dir)
    for pair_file in pair_dir:
        onecampair = []
        pair_id = int(pair_file[11:][:-4])
        pair_file_path = campairfile + pair_file

        with open(pair_file_path) as f:
            lines = f.readlines()
            if(len(lines)< num_src):
                pairfile_num = pairfile_num - 1
            else:
                for i in range(num_src):
                    onecampair.append(int(lines[i].rstrip()))
                camspair_list[pair_id] = onecampair
    # print("camspair_list", camspair_list)
    # exit()
    write_pairs(output_file, camspair_list, num_src, pairfile_num)



def compute_campair(output_file, num_src):
    campairfile = output_file + "/camspair/"
    if(not os.path.exists(campairfile)):
        os.makedirs(campairfile)
    viewsfile = output_file + '/sfm/'
    re_scan = computecampair.computecampair(viewsfile, campairfile, num_src)

    pairs_to_pair(output_file, campairfile, num_src)
