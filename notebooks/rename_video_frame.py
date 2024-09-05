import os
import cv2

# 定义视频目录
video_dir = "./videos/davinci_raofei"
target_dir =    "./videos/davinci_raofei_3jpg"

# 获取所有 JPEG 文件名并进行排序
frame_names = [
    p for p in os.listdir(video_dir)
    if os.path.splitext(p)[-1].lower() in [".jpg", ".jpeg"]
]
frame_names.sort()

# 重命名并缩放图像
for idx, old_name in enumerate(frame_names, start=1):
    # 生成新的文件名
    new_name = f"{idx:05d}.jpg"  # 格式化为 00001, 00002, ...
    old_path = os.path.join(video_dir, old_name)
    new_path = os.path.join(target_dir, new_name)

    # 打开图像并缩放
    img = cv2.imread(old_path)
    img = cv2.resize(img, (1224, 1024))
    # 打印通道数
    print(img.shape)
    cv2.imwrite(new_path, img)


print("文件重命名和缩放完成。")