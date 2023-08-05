from PIL import Image, ImageDraw, ImageFont
import requests
import urllib.request

# Now make your requests without SSL verification
image_size = 800
background_color = (0, 0, 0)
background_image = Image.new("RGB", (image_size, image_size), background_color)

player_img_url = "https://content.mlb.com/images/headshots/current/60x60/673490.png"
player_id = player_img_url.split("/")[-1].split('.')[0]
static_base_url = 'https://img.mlbstatic.com/mlb-photos/image/upload/d_people:generic:headshot:67:current.png/w_426,q_auto:best/v1/people/'
player_id_url = f"/{player_id}/headshot/67/current"
static_url = static_base_url + player_id_url
urllib.request.urlretrieve(static_url, 'testimg.jpg')

images = ["testimg.jpg"] * 5
images2 = ["image2.jpg", "image2.jpg", "image2.jpg", "image2.jpg", "image2.jpg"]
texts = ["Text 1", "Text 2", "Text 3", "Text 4", "Text 5"]

num_images = len(images)
padding = 10
image_height = (image_size - (padding * 5) * 2) // 5
padding_left = 15
text_padding = 0

for i, image in enumerate(images):
    image = Image.open(image)
    image.thumbnail((image_height, image_height))
    y_offset = i * (image_height + padding* 2) + padding
    background_image.paste(image, (padding_left, y_offset))
    
    draw_image = ImageDraw.Draw(background_image)
    text_x = padding_left + image_height + text_padding
    text_y = (y_offset + (image_height // 2))
    font = ImageFont.truetype("arial.ttf", 35)
    ascent, descent = font.getmetrics()
    text_width = font.getmask(texts[i]).getbbox()[2]
    text_height = font.getmask(texts[i]).getbbox()[3] + descent
    text_y -= text_height // 2
    draw_image.text(xy=(text_x, text_y), text=texts[i], font=font)
    
background_image.show()


