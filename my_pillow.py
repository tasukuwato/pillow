from PIL import Image, ImageFilter

# im変数に任意のパスの画像を代入
im = Image.open('img/android.png')

# format>>> 画像の種類の分類
# size>>> (幅,高さ)でピクセル数を表示
# mode>>> 画像データフォーマットの表示。詳細は「https://imagingsolution.net/program/python/pillow/image_data_format/」
print(im.format, im.size, im.mode)

# 表示例：PNG (1024, 1218) P

