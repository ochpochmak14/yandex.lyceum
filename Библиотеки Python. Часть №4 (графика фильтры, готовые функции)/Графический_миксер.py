from PIL import Image


def twist_image(input_ﬁle_name, output_ﬁle_name):
    img = Image.open(input_ﬁle_name)
    img_width, img_height = img.size

    left_section = (0, 0, img_width // 2, img_height)
    right_section = (img_width // 2, 0, img_width, img_height)

    left_part = img.crop(left_section)
    right_part = img.crop(right_section)

    swapped_img = Image.new("RGB", (img_width, img_height))
    swapped_img.paste(right_part, (0, 0))
    swapped_img.paste(left_part, (img_width // 2, 0))

    swapped_img.save(output_ﬁle_name)
