import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
#读取图像
image = cv2.imread('./pic_data/image1.jpg')

#提取低频信息
low_frequencies=cv2.GaussianBlur(image,(31,31),0)

print("我正在运行！")
#提取高频信息
high_frequencies=image-low_frequencies

 
# plt.switch_backend('agg')
#显示结果
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(low_frequencies,cmap="gray")
plt.title("low frequencies")

plt.subplot(1,2,2)
plt.imshow(high_frequencies,cmap="gray")
plt.title("High frequencies")
# 远程服务器无法进行图形显示

# plt.show()

#把相应的照片保存下来
plt.savefig("./res_data/1.jpg")
