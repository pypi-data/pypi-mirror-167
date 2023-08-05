from PIL import Image, ImageDraw

def upScale(img:Image, scale:int)->Image:
    '''Upscaling of an image. Borders between pixels will not become soft.'''
    x,y = img.size  #get the size of the given image
    newImg = Image.new(mode="RGB", size=(x*scale, y*scale))     #create a new image with the correct size
    draw = ImageDraw.Draw(newImg)

    #iterate over all pixels in the old image
    for px in range(0, x*scale, scale):
        for py in range(0, y*scale, scale):
            #get color-value of the pixel
            color = img.getpixel((px/scale,py/scale))
            #multiply the pixel
            for sx in range(scale):
                for sy in range(scale):
                    draw.point((px+sx,py+sy), fill=color)    #put pixel into image

    #return the result
    return(newImg)
