from PIL import Image,ImageSequence
import cv2
import numpy as np

from PIL import Image,ImageSequence

def gif_transfer(filename,width, height):
    gif = Image.open(filename)                # 讀取動畫圖檔

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
    # 儲存為 gif
    gif[0].save("yueliclaudius.gif", save_all=True, append_images=gif[1:], duration=30, loop=0, disposal=1)
def main():
    filename='1.gif'#gif名字
    width = 500 #w像素
    height = 500 #h像素
    gif_transfer(filename,width, height)
    
if __name__ == '__main__':
    main()