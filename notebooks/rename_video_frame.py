import os
import cv2

# 定义视频目录
video_dir = "./videos/ab_enhance"
target_dir = "./videos/ab_enhance_rename"

# 确保目标文件夹存在
os.makedirs(target_dir, exist_ok=True)

# 获取所有 JPEG 文件名并进行排序
frame_names = [
    p for p in os.listdir(video_dir)
    if os.path.splitext(p)[-1].lower() in [".jpg", ".jpeg", ".png"]
]
frame_names.sort()

# 重命名并缩放图像
for idx, old_name in enumerate(frame_names, start=1):
    # 生成新的文件名
    new_name = f"{idx:05d}.jpg"  # 格式化为 00001, 00002, ...
    old_path = os.path.join(video_dir, old_name)
    new_path = os.path.join(target_dir, new_name)

    # 打开图像
    img = cv2.imread(old_path)
    # img = cv2.resize(img, (1224, 1024))

    # 打印通道数
    if img is not None:
        print(img.shape)
        cv2.imwrite(new_path, img)
    else:
        print(f"无法读取图像: {old_path}")

print("文件重命名和缩放完成。")