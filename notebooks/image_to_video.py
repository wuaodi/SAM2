import os
import cv2

src_path = '/home/wuaodi/PycharmProjects/DXO/结果/enhance_bbox结果'
img_array = []

# by os.listdir
for filename in sorted(os.listdir(src_path)):
    print(src_path+filename)
    img = cv2.imread(os.path.join(src_path, filename))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    print(filename)

# out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 5, size)  # mp4

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
print('over')