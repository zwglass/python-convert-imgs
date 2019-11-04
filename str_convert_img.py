import os
import math
import random
from uuid import uuid1
from PIL import Image, ImageDraw, ImageFont, ImageFilter
 
 
def char_img(zt,str1):
	""" 字符串生成图片。zt：字体.ttf文件。str1：字符串。 """
	# 实例一个图片对象240 x 60:
	width = 40*len(str1) #60 * 4
	height = 60
	# 图片颜色
	r = random.randint(0,200)
	g = random.randint(0,200)
	b = random.randint(0,200)
	clo = (r, g, b)
	image = Image.new('RGB', (width, height), clo)
	 
	# 创建Font对象:
	# 字体文件可以使用操作系统的，也可以网上下载
	zt = zt # 'a.ttf'
	font = ImageFont.truetype(zt, 36)
	 
	# 创建Draw对象:
	draw = ImageDraw.Draw(image)
	 
	# 输出文字:
	# str1 = "我爱世界"
	w = 4 #距离图片左边距离
	h = 10 #距离图片上边距离
	draw.text((w, h), str1, font=font)
	# 模糊:
	image.filter(ImageFilter.BLUR)
	code_name = f'testimg{str1}.jpg'
	save_path = './convert-imgs'
	is_exists = os.path.exists(save_path)
	if not is_exists:
		os.makedirs(save_path, exist_ok=True)
	save_dir = './convert-imgs/{}'.format(code_name)
	image.save(save_dir, 'jpeg')
	# print("已保存图片: {}".format(save_dir))
 
if __name__ == '__main__':
	zt = './fonts/lishu.TTF'
	str1 = '我爱你'
	char_img(zt,str1)
	strs_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
	for s in strs_list:
		char_img(zt, s)
