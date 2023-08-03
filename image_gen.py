from PIL import Image, ImageDraw, ImageFont

def generate_image(names_with_headshots, output_path):
    # Constants
    image_size = 500  # Change this value to control the size of the square image
    font_size = 20
    text_color = (255, 255, 255)  # White text color
    background_color = (0, 0, 0)  # Black background color
    headshot_size = 100  # Change this value to control the size of the headshot images
    margin = 35

    # Create a new blank image with black background
    img = Image.new('RGB', (image_size, image_size), background_color)
    draw = ImageDraw.Draw(img)

    # Load a font (you can change the font or use a different one if needed)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Loop through the names and headshots and draw them on the image
    for idx, (name, headshot_path) in enumerate(names_with_headshots):
        # Load and resize the headshot image
        headshot_img = Image.open(headshot_path).resize((headshot_size, headshot_size))

        # Calculate position for the text and headshot
        text_x = headshot_size + 2 * margin
        text_y = idx * (font_size + 2 * margin) + margin
        headshot_x = margin
        headshot_y = idx * (font_size + 2 * margin) + margin

        # Draw the headshot image
        img.paste(headshot_img, (headshot_x, headshot_y))

        # Draw the name text
        draw.text((text_x, text_y), name, fill=text_color, font=font)

    # Save the final image
    img.save(output_path)

# Example usage
names_with_headshots = [
    ("Name1", "./image.jpg"),
    ("Name2", "./image.jpg"),
    ("Name3", "./image.jpg"),
    ("Name4", "./image.jpg"),
    ("Name5", "./image.jpg"),
]

output_image_path = "output_image.jpg"
generate_image(names_with_headshots, output_image_path)