from PIL import Image,ImageSequence
import cv2
import numpy as np
import os

from PIL import Image,ImageSequence

def gif_transfer(filename, width, height):
    gif = Image.open(filename)                # 讀取動畫圖檔
    #images是否存在
    if os.path.isdir('./images/')==False:
        os.mkdir('images') 
    #存成jpg
    i = 0                                     
    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert('RGBA')         
        frame.save(f'./images/frame{i}.png', quality=100, subsampling=0,)  # 儲存為 png
        i = i + 1                           
    num_of_jpg=i

    #存成gif
    i=0
    gif = []
    for i in range(num_of_jpg):
        
        #resize
        image = cv2.imread(f'./images/frame{i}.png', cv2.IMREAD_UNCHANGED)
        dim = (width, height)
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(f'./images/frame{i}.png', image)
        
        #append
        img = Image.open(f'./images/frame{i}.png')  # 開啟圖片
        gif.append(img)                    # 加入串列
        i = i + 1
    # 儲存為 gif
    gif[0].save("yueliclaudius.gif", save_all=True, append_images=gif[1:], duration=30, loop=0, disposal=0)
    # frame1：gif 動畫第一個影格
    # save_all：設定 True 表示儲存全部影格，否則只有第一個
    # append_images：要添加到 frame1 影格的其他影格，串列格式，通常會用 frame[1:] 來添加除了第一個影格之後的所有影格
    # duration：每個影格之間的毫秒數，支援串列格式
    # disposal：添加模式，預設 0，如果背景透明，則設定為 2 避免影格彼此覆蓋覆蓋
def main():
    filename='1.gif'#gif名字
    width = 95 #w像素
    height = 95 #h像素 
    gif_transfer(filename, width, height)
if __name__ == '__main__':
    main()