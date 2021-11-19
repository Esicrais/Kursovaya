from PIL import Image, ImageDraw


def sh_img(text):
    rx=0
    ry=0
    img = Image.open("win.jpg")
    pix = img.load()
    draw = ImageDraw.Draw(img)#???
    for i in text:
        cod2=str(bin(ord(i))[2:].zfill(8))#получаем код юникод, потом в 2ю систему. Срезаем 2 символа и дополняем до 8 знаков.перевод в строку
        for j in cod2:

            r, g, b = pix[rx,ry][0:3]#вытаскиваем значения красного из координат
            r =str(bin(r)[2:].zfill(8))
            new_r=int(r[0:7]+j[-1])
            draw.point((rx,ry), (new_r, g, b))# Создаем новую точку с параметрами цвета
            rx=rx+1
            if rx == img.size[0]:
                ry=ry+1
    img.save("newimage.jpg", "JPG")
sh_img(str(input()))
