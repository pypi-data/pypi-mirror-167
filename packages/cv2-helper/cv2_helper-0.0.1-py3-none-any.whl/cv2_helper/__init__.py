import cv2
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import platform

def cv2_draw_rect(image, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    cv2.rectangle(image, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=2)

    return image

def cv2_draw_label(image, text, point, font_color=(255, 255, 255), font_size=28):
    x, y = point
    x, y = int(x), int(y)
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    if platform.system() == 'Darwin': #맥
        font = 'AppleGothic.ttf'
    elif platform.system() == 'Windows': #윈도우
        font = 'malgun.ttf'
    elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        '''
        !wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        !mv malgun.ttf /usr/share/fonts/truetype/
        import matplotlib.font_manager as fm 
        fm._rebuild() 
        '''
        font = 'malgun.ttf'
    try:
        imageFont = ImageFont.truetype(font, font_size)
    except:
        imageFont = ImageFont.load_default()
    draw.text((x, y), text, font=imageFont, fill=font_color)
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    return image

def cv2_draw_rect_with_label(image, point1, point2, text, font_color=(255, 255, 255), font_size=28):
    x1, y1 = point1
    x2, y2 = point2
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    cv2.rectangle(image, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=2)

    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    if platform.system() == 'Darwin': #맥
        font = 'AppleGothic.ttf'
    elif platform.system() == 'Windows': #윈도우
        font = 'malgun.ttf'
    elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        '''
        !wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        !mv malgun.ttf /usr/share/fonts/truetype/
        import matplotlib.font_manager as fm 
        fm._rebuild() 
        '''
        font = 'malgun.ttf'
    try:
        imageFont = ImageFont.truetype(font, font_size)
    except:
        imageFont = ImageFont.load_default()
    text_width, text_height = imageFont.getsize(text)
    draw.rectangle(((x1, y1 - text_height), (x1 + text_width, y1)), fill=(0, 0, 255)) 
    draw.text((x1, y1 - text_height), text, font=imageFont, fill=font_color) #채워진 사각형
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    return image

def cv2_draw_point(image, point):
    x, y = point
    x, y = int(x), int(y)
    cv2.circle(image, center=(x, y), radius=2, color=(255, 0, 0), thickness=-1)

    return image

def cv2_draw_image(image, image_to_draw, point):
    x, y = point
    x, y = int(x), int(y)
    image_height, image_width, image_channel = image.shape 
    image_to_draw_height, image_to_draw_width, image_to_draw_channel = image_to_draw.shape 
    if image_to_draw_channel == 3:
        x1, y1 = x, y
        x2, y2 = x + image_to_draw_height, y + image_to_draw_width
        image[y1:y2, x1:x2] = image_to_draw
    elif image_to_draw_channel == 4:
        temp = x
        x = y
        y = temp
        for i in range(image_to_draw_height):
            for j in range(image_to_draw_width):
                if x + i >= image_height or y + j >= image_width:
                    continue
                alpha = float(image_to_draw[i][j][3] / 255.0) #알파 채널
                image[x + i][y + j] = alpha * image_to_draw[i][j][:3] + (1 - alpha) * image[x + i][y + j]

    return image
