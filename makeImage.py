"""
makeImage.py

copyright kamosika
Released under the MIT liense
https://opensource.org/licenses/MIT

Date: 2022-08-15
"""


from PIL import Image,ImageDraw,ImageFont
import random
import os

def print_image(working_hours = [4,5,9,0,2,3,5]):
    img = Image.new("RGB",(250,128),(255,255,255))
    draw = ImageDraw.Draw(img)
    ipaexg_font = ImageFont.truetype("ipaexg.ttf", 15) #フォントの設定
    uzura_font = ImageFont.truetype("uzura.ttf",15) #フォントの設定
    
    #画像のサイズ
    image_x = 250
    image_y = 128

    #外枠の幅
    outline_width = 5

    #外枠を描く
    draw.rectangle((outline_width,outline_width,image_x - outline_width,image_y - outline_width),fill=(255,255,255),outline=(255,0,0))

    #グラフの幅
    graph_width = 140
    #グラフの高さ（最大）
    graph_height_max = 100

    #グラフの開始位置x
    graph_start_x = 135

    #グラフの開始位置y
    graph_start_y = 20


    for num,hour in enumerate(working_hours):
        draw.rectangle((graph_start_x + 15*num,image_y - graph_start_y,graph_start_x + 15*(num+1),image_y - (graph_start_y + hour*10)),fill=(255,0,0),outline=(0,0,0))

    draw.text((10,10),"テスト直接",(255,0,0),font=ipaexg_font,stroke_width=5,stroke_fill=(255,0,0))
    draw.text((10,30),"テスト直接",(255,0,0),font=uzura_font,stroke_width=5,stroke_fill=(255,0,0))

    rotated_image = img.rotate(90, expand=True)
    rotated_image.save(os.path.dirname(os.path.abspath(__file__))+"/test.png")