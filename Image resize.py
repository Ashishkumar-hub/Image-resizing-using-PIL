# Image Resizing Python Project
from PIL import Image
image = Image.open('cat.jpg')
image.show()

print("The file format of the source file:",image.format)
print("The pixel format used by the image. Typical values are 1, L, RGB, or CMYK:",image.mode)
print("Image size, in pixels. The size is given as a 2-tuple (width, height):",image.size)
print("Colour palette table: ",image.palette)

# Chaning Image Type
image = Image.open('cat.jpg')
image.save('cat.png')

# Resizing Image
image = Image.open('cat.jpg')
new_image = image.resize((500, 500))
new_image.save('cat.jpg.jpg')
print("Previous Image size:",image.size)
print("New Image size:",new_image.size)

#resizinfg image keeping the aspect ratio
image = Image.open('cat.jpg')
image.thumbnail((400, 400))
image.save('cat_thumbnail.jpg')
print(image.size)

# cropping image
image = Image.open('cat.jpg')
box = (100, 200, 300, 400)
cropped_image = image.crop(box) #   box(left, upper, right, lower).
cropped_image.save('cropped_image_cat.jpg')
print("size of cropped image",cropped_image.size)

# Pasting an Image onto Another Image

image = Image.open('cat.jpg')
logo = Image.open('ashishlogo.jpg')
logo.thumbnail((120, 120))
logo.save('ashishlogo_thumbnail.png')
print(image.size)
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('cat_image_with_ashishlogo.jpg')
# image_copy.paste(logo, position, logo) # remove logo background

# Rotating Images

image = Image.open('cat.jpg')
image_rot_90 = image.rotate(90)
image_rot_90.save('image_rot_90.png')
image_rot_180 = image.rotate(180)
image_rot_180.save('image_rot_180.png')
image.rotate(18).save('image_rot_18.png')
image.rotate(18, expand=True).save('image_rot_18.png')

# Flipping Images

image = Image.open('cat.jpg')
image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
image_flip.save('image_flip.jpg')

# Drawing on image

from PIL import Image, ImageDraw
canvas = Image.new('RGB', (400, 300), 'white')
img_draw = ImageDraw.Draw(canvas)
img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')
img_draw.text((70, 250), 'Ashish', fill='blue')
canvas.save('drawn_image.jpg')

# Color Transforms
image = Image.open('cat.jpg')
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image.jpg')
print(image.mode)
print(greyscale_image.mode)

# Splitting and Merging Bands

image = Image.open('cat.jpg')
red, green, blue = image.split()
print(image.mode)
print(red.mode)
print(green.mode)
print(blue.mode)
new_image = Image.merge("RGB", (green, red, blue))
new_image.save('new_image.jpg')
print(new_image.mode) # Output: RGB

# Image enhancements
from PIL import Image, ImageEnhance
image = Image.open('cat.jpg')
contrast = ImageEnhance.Contrast(image)
contrast.enhance(1.5).save('contrast.jpg')

# Incresing color of image
color = ImageEnhance.Color(image)
color.enhance(1.5).save('color.jpg')

# brightening image
brightness = ImageEnhance.Brightness(image)
brightness.enhance(1.5).save('brightness.jpg')

# sharpeness
sharpness = ImageEnhance.Sharpness(image)
sharpness.enhance(1.5).save('sharpness.jpg')

