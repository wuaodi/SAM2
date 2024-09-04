import os
import cv2
import numpy as np
import glob
src_path = '/home/wuaodi/PycharmProjects/SAM2/notebooks/results'
img_array = []

# by os.listdir
for filename in sorted(os.listdir(src_path)):
    print(src_path+filename)
    img = cv2.imread(os.path.join(src_path, filename))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    print(filename)

out = cv2.VideoWriter('单目标结果_双翼上海吊飞第六组.avi', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
print('over')