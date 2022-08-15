"""
** makeImage.py **

copyright kamosika
Released under the MIT liense
https://opensource.org/licenses/MIT

Date: 2022-08-15

----

** PIL License **
The Python Imaging Library (PIL) is

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is

    Copyright © 2010-2022 by Alex Clark and contributors

Like PIL, Pillow is licensed under the open source HPND License:

By obtaining, using, and/or copying this software and/or its associated
documentation, you agree that you have read, understood, and will comply
with the following terms and conditions:

Permission to use, copy, modify, and distribute this software and its
associated documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appears in all copies, and that
both that copyright notice and this permission notice appear in supporting
documentation, and that the name of Secret Labs AB or the author not be
used in advertising or publicity pertaining to distribution of the software
without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
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