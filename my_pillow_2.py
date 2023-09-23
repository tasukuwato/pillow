from PIL import Image, ImageFilter

im = Image.open('img/flower.png')

#RGBの順に(最小,最大)で表示。
print(im.getextrema())

# 補足:im.getpixel((x座標,y座標))で、任意の座標のRGBを取得できる。