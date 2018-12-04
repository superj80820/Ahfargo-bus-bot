from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

for item in range(1,9+1):
    img = Image.open("bus_egg_sample.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("swissk.ttf", 23)
    draw.text((17, 14),str(item),(0,0,0),font=font)
    img.save('bus_egg_%s.png' %str(item))

for item in range(10,98+1):
    img = Image.open("bus_egg_sample.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("swissk.ttf", 20)
    draw.text((12, 16),str(item),(0,0,0),font=font)
    img.save('bus_egg_%s.png' %str(item))