import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check_command_line()
    try:
        #open image
        image1 = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    #open shirt
    shirt1 = Image.open('shirt.png')

    #get shirt size
    shirt_size = shirt1.size

    #change image size to fit shirt
    final_image = ImageOps.fit(image1, shirt_size)

    #paste shirt to final_image
    final_image.paste(shirt1, shirt1)

    #save final image to argv[2]
    final_image(sys.argv[2])

def check_command_line():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    #confirm files have.png or .jpg extensions
    input_image = splitext(sys.argv[1])
    output_image = splitext(sys.argv[2])

    if input_image[1].lower() not in ['.jpg', '.jpeg', '.png']:
        sys.exit('Invalid input')
    if output_image[1].lower() not in ['.jpg', '.jpeg', '.png']:
        sys.exit('Invalid input')

    #check if the extensions are similar
    if input_image[1].lower != output_image[1].lower:
        sys.exit('Input and output have different extensions')

if __name__ == "__main__":
    main()
