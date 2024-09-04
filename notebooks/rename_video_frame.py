import os
from PIL import Image

# 定义视频目录
video_dir = "./videos/spacecraft"

# 获取所有 JPEG 文件名并进行排序
frame_names = [
    p for p in os.listdir(video_dir)
    if os.path.splitext(p)[-1].lower() in [".jpg", ".jpeg"]
]
frame_names.sort()

# 重命名并缩放图像
for idx, old_name in enumerate(frame_names, start=1):
    # 生成新的文件名
    new_name = f"{idx:06d}.jpg"  # 格式化为 000001, 000002, ...
    old_path = os.path.join(video_dir, old_name)
    new_path = os.path.join(video_dir, new_name)

    # 打开图像并缩放
    with Image.open(old_path) as img:
        img = img.resize((1024, 1024))  # 缩放到 1024x1024
        img.save(new_path)  # 保存为新的文件名

print("文件重命名和缩放完成。")