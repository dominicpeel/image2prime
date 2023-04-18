from PIL import Image, ImageDraw, ImageFont

def create_digit_image(digit, font_path, font_size):
    font = ImageFont.truetype(font_path, font_size)
    size = font.getsize(str(digit))
    image = Image.new('L', size, color=255)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), str(digit), font=font, fill=0)
    return image

def count_black_pixels(image, threshold=0):
    width, height = image.size
    black_pixels = 0
    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            if pixel_value <= threshold:
                black_pixels += 1
    return black_pixels


font_path = "/home/dominic/.fonts/Fira Code Regular Nerd Font Complete Mono.ttf"
font_size = 50

digits = sorted(list(range(10)), key=lambda x: -count_black_pixels(create_digit_image(x, font_path, font_size)))
print(digits)
# [0, 8, 9, 6, 5, 1, 2, 4, 3, 7]