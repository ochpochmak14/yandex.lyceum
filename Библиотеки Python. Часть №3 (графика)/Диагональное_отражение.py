from PIL import Image
    
 
def mirror():
    im1 = Image.open("image.jpg")
    im2 = im1.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_90)
    im2.save('res.jpg')