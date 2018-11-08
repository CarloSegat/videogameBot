import ImageGrab, ImageFilter
import os
import time
import Image
#left & right click-to-change-map areas excluded, bottom menu excluded
left_corner = (262, 34)
x_offset = left_corner[0] #movement area not considered
y_offset = left_corner[1]
right_corner = (1123, 649)



def screenGrab():
    box = (left_corner[0], left_corner[1], right_corner[0], right_corner[1])
    im = ImageGrab.grab(box)
    #print "im is instance of Image " + str(isinstance(im, Image.Image))
    #im = im.filter(ImageFilter.EDGE_ENHANCE)
    #im = im.filter(ImageFilter.MaxFilter())
    #im = im.filter(ImageFilter.ModeFilter(21))

    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
        
