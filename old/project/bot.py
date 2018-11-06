import win32api, win32con
import time, random, sys, os
import ImageGrab, ImageOps, ImageFilter, ImageEnhance
from PIL import Image
from pytesseract import image_to_string
from numpy import *
import pytesseract
from difflib import SequenceMatcher
import unicodedata
import ast


##COORDS
level_up_okay = (655, 345)
left_corner = (262, 34)
x_offset = left_corner[0] #movement area not considered
y_offset = left_corner[1]
right_corner = (1123, 649)
img_height = right_corner[1] - left_corner[1]
img_width = right_corner[0] - left_corner[0]
##

#Coordinates abd colors methods
def add_offset(coord):
    new_coord = (coord[0] + x_offset, coord[1] + y_offset)
    return new_coord
def take_offset(coord):
    new_coord = (coord[0] - x_offset, coord[1] - y_offset)
    return new_coord
def rgb_eq(rgb1, rgb2):
    '''resources hoovered with cursor seem to randomly change color, very small
    variation'''
    if abs(rgb1[0] - rgb2[0]) > 1:
        return False
    if abs(rgb1[1] - rgb2[1]) > 1:
        return False
    if abs(rgb1[2] - rgb2[2]) > 1:
        return False
    return True
def is_black(rgb):
    '''Cursor border is not exactly (0,0,0) when near a dialog box.
    Black shades have in common that 3 values are ==.'''
    if rgb[0] == rgb[1] == rgb[2]:
        if rgb[0] < 12:
            return True
    return False
def get_colors(img):
    '''Img --> list of colors'''
    img = img.convert('RGB')
    colors_present = []
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            colors_present.append(img.getpixel((x,y)))
    return list(set(colors_present))



class File_manager:
    '''Uses ast.literal to read dict from file and
    repr to tore it back.'''
    def __init__(self):
        self.saved_coords = "res_coords"

    def saftey_check(self, category, res_name):
        '''False if category and res_name are not in Resource'''
        if category in Resource.categ_res:
            if res_name in Resource.categ_res[category]:
                return True
        return False

    def get_cords(self, category, res_name, mapp):
        '''Checks file list of maps of a given resource '''
        if not self.saftey_check(category, res_name):
            print "File_manager, get_coords: category or res_name wrong"
            return
        with open(self.saved_coords, 'r+') as original:
            res_cords = original.read()
            #print res_cords
            res_cords = ast.literal_eval(res_cords)
            #print type(res_cords)
        try:
            coords =  res_cords[category][res_name][mapp]
            return coords
        except(KeyError):
            return False

    def add_cords(self, category, res_name, mapp, cord_list):
        '''e.g. (cereal,   wheat,   (1,1),   [(1,1), (50,100), ...])
        [category][res_name][map] = list_cord'''
        if not self.saftey_check(category, res_name):
            print "File_manager, add_cord_list: category or res_name wrong"
            return

        with open(self.saved_coords, 'r+') as original:
            res_cords = original.read()
            res_cords = ast.literal_eval(res_cords)

            if self.get_cords(category, res_name, mapp):
                return
            else:
                res_cords[category][res_name][mapp] =  cord_list#already coords present
                print repr(res_cords)
                original.seek(0)
                original.write(repr(res_cords))


class Player:
    def __init__(self):
        self.pos = (0,0)#self.get_pos()#map where you are

    @staticmethod
    def screenGrab():
        box = (left_corner[0], left_corner[1], right_corner[0], right_corner[1])
        im = ImageGrab.grab(box)
        return im

    @staticmethod
    def screenGrab_custom( left_corner, right_corner):
        box = (left_corner[0], left_corner[1], right_corner[0], right_corner[1])
        im = ImageGrab.grab(box)
        return im

    @staticmethod
    def click_here(coord):
        '''Single click on point or on every point of a list'''
        if type(coord) == list:
            for c in coord:
                Player.click_here(c)
        else:
            win32api.SetCursorPos(coord)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            time.sleep(random.uniform(1.05, 0.190))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

    @staticmethod
    def just_click():
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        time.sleep(random.uniform(1.0, 0.2))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

    @staticmethod
    def hoover(coords, time_to_sleep):
        '''Hoover time sec over all cords in list'''
        for c in coords:
            win32api.SetCursorPos(c)
            time.sleep(time_to_sleep)

    def get_pos(self):
        '''Read top-left of screen and save pos'''
        #TODO impkeent w/ zoom and use a statistic method
        def zoom_in():
            Player.click_here((374, 9)) #get windows on focus
            win32api.SetCursorPos((300, 300))
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,120)

        def zoom_out():
            Player.click_here((374, 9)) #get windows on focus
            win32api.SetCursorPos((300, 300))
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-120)

        img = self.screenGrab_custom((12, 53), (64, 73))
        #result = pytesseract.image_to_string(img, config='--tessdata-dir digits -psm 7')
        #print "1: " + str(result)
        #img = img.convert('L')
        img = img.filter(ImageFilter.MedianFilter())
        #result = pytesseract.image_to_string(img, config='--tessdata-dir digits -psm 7')
        #print "2:" + str(result)
        #img = img.filter(ImageFilter.MaxFilter(3))
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(4)
        result = pytesseract.image_to_string(img, config='--tessdata-dir digits -psm 7')
        print "3: " + str(result)

        pixels = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                pix = pixels[x, y]
                if pix != (255,255,255):
                    try:
                        if not(pixels[x -1, y] == (255,255,255) and pixels[x +1, y] == (255,255,255)):
                            pixels[x, y] = (0,0,0)
                    except:
                        pixels[x, y] = (0,0,0)
        img.save("teeest_poS.png", 'PNG')
        result = pytesseract.image_to_string(img, config='--tessdata-dir digits -psm 7')
        print "4: " + str(result)

        result = unicode(result, "utf-8")
        result = unicodedata.normalize('NFKD', result).encode('ascii','ignore')
        print "unicode: " + str(result)
        result = result.strip().split(" ")

        return (int(result[0]), int(result[1]))

    def go_up(self):
        lu = (266,21)
        rd = (1085, 27)
        click = (random.randint(lu[0], rd[0]), random.randint(lu[1], rd[1]))
        self.click_here(click)

    def go_down(self):
        lu = (294, 634)
        rd = (1013, 642)
        click = (random.randint(lu[0], rd[0]), random.randint(lu[1], rd[1]))
        self.click_here(click)

    def go_right(self):
        lu = (1107, 24)
        rd = (1363,713)
        click = (random.randint(lu[0], rd[0]), random.randint(lu[1], rd[1]))
        self.click_here(click)

    def go_left(self):
        lu = (10, 29)
        rd = (227, 707)
        click = (random.randint(lu[0], rd[0]), random.randint(lu[1], rd[1]))
        self.click_here(click)

    def go_to(self, mapp):
        start = self.get_pos()
        print "start " + str(start)
        finish = mapp
        movements = []
        while start != finish:
            if start[0] > finish[0]:
                movements.append(self.go_left)
                start = (start[0] - 1, start[1])
            elif start[0] < finish[0]:
                movements.append(self.go_right)
                start = (start[0] +1, start[1])

            if start[1] > finish[1]:
                movements.append(self.go_up)
                start = (start[0], start[1] - 1)
            elif start[1] < finish[1]:
                movements.append(self.go_down)
                start = (start[0], start[1] + 1)
        print movements

    def check_tacticmode(self):
        '''Return true if tactic mode is active.
        Detected by checking that area on left side - bottom is black'''

        check_points = [(12, 356), (13, 356), (11, 356), (12, 355),(13, 357),
        (1317, 340)]
        img = Player.screenGrab_custom((0,0), (1358, 759))
        for p in check_points:
            color = img.getpixel(p)
            print color
            if not (rgb_eq(color, (0,0,0))):
                return False
        return True

    def toggle_tacticmode(self):
        Player.click_here((942, 715))
        time.sleep(random.uniform(0.1, 0.01))

class Resource:

    categ_res = {"cereal": ["wheat", "barley", "oats"], "wood":["ash"]}

    #Abstract method
    def get_coords(self):
        raise NotImplementedError()

    def correct_cursor(self, coord):
        '''
        param coord is the assumed cursor pos
        WORKS W/ LOCAL COORDS. CURSOR IS ARROW OF RESOURCES
        ASSUSMES THE CURSOR IS IN THE POSITION WHERE COORDS INDICATES.
        Sometimes cursor position is not top-left black pixel of arrow,
        this function take an incorrect position (eg 1 on the left), and
        returns the correct one'''
        time.sleep(0.05)
        img = Player.screenGrab()
        color = img.getpixel(coord)

        #When cursor is black:
        if is_black(color):
            #Black bottom and left
            if is_black( img.getpixel((coord[0] + 1, coord[1])) ) and\
               is_black( img.getpixel((coord[0], coord[1] + 1)) ):
               return coord
            #Black on right & left
            if is_black( img.getpixel((coord[0] - 1, coord[1])) ) and\
               is_black( img.getpixel((coord[0] + 1, coord[1])) ):
               return (coord[0] - 1, coord[1])
            #Black on top & down
            if is_black( img.getpixel((coord[0], coord[1] - 1)) ) and\
               is_black( img.getpixel((coord[0], coord[1] + 1)) ):
               return (coord[0], coord[1] - 1)
        #When cursor is white, but checking for white is not robust so loook
        #for 3 black blocks on L, T, LT
        if is_black( img.getpixel((coord[0] -1, coord[1])) ) and\
           is_black( img.getpixel((coord[0], coord[1] - 1)) ) and\
           is_black( img.getpixel((coord[0] - 1, coord[1] - 1)) ):
            return (coord[0] - 1, coord[1] - 1)

        #When cursor is of a different color
        else:
            #Pix on right is black
            if is_black( img.getpixel((coord[0] + 1, coord[1])) ):
                #2 pix on right and 1 top is black
                if is_black( img.getpixel((coord[0] + 2, coord[1] - 1)) ):
                    return (coord[0] + 1, coord[1] - 1)
                #1 pix on right is black
                if is_black( img.getpixel((coord[0] + 1, coord[1])) ):
                    return (coord[0] + 1, coord[1])

            #Pix on down is black
            if is_black( img.getpixel((coord[0], coord[1] + 1)) ):
                #2 pix down is white
                if is_black( img.getpixel((coord[0] - 1, coord[1] + 2)) ):
                    return (coord[0] - 1, coord[1] + 1)
                #2 pix down is black
                if is_black( img.getpixel((coord[0], coord[1] + 2)) ):
                    return (coord[0] + 1, coord[1])
            else:
                #In theory this is never executed
                #print "assume is top-left of real pos"
                return (coord[0] + 1, coord[1] + 1)

    def is_cereal(self, coord):
        '''Check for schyte symbol by loooking 18, 19, 20 px down cursor and
        13px on the right. Those point are black for schyte.'''
        #print "From inside is_cereal original " + str(take_offset(coord))
        win32api.SetCursorPos(coord) #global coord
        time.sleep(0.05) #wait that cursor is drawn
        coord = self.correct_cursor(take_offset(coord))
        #print "From inside is_cereal corrected " + str(coord)
        img = Player.screenGrab()
        #img.save("TEssst.png", 'PNG')
        off = 18
        #print img.getpixel(take_offset(coord))
        for i in range(0, 3):
            try:
                if not is_black( img.getpixel((coord[0], coord[1] + 18 + i))):
                    #print "no b" + str(i)
                    return False
                if not is_black( img.getpixel((coord[0] + 13, coord[1])) ):
                    #print "no b"
                    return False
            except:
                #bottom and most-right pixels
                return False
        return True

    def grab_resource_dialog(self, coord):
        '''Returns raw image which contains the name of the resource'''
        win32api.SetCursorPos(coord)
        time.sleep(0.1)
        dialog_topleft = (coord[0], coord[1] - 80)
        dialog_width = 110
        dialog_height = 100
        img = Player.screenGrab_custom(dialog_topleft,
                               (dialog_topleft[0] + dialog_width, dialog_topleft[1] + dialog_height))
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("dialog.png", 'PNG')
        return img

    def extract_resource_name(self, img, name_len):
        '''Raw image --> Crop --> string of name
        Divide image in N horizontal bands of "band size" which can be either
        black or white bands depending on number of blk/wht pixels; either 1 or 0
        is appended to an array whoise index is the row.
        Then index at which a sequence of white raws starts is calculated and
        used to slice horizontally original image.
        Finally vertical slicing is applied to obtain just the resource name.

        name_len used to crop vertically.'''
        #Enhance white areas
        white_img = img.filter(ImageFilter.EDGE_ENHANCE)
        white_img = img.filter(ImageFilter.MaxFilter(3))

        img_width = img.size[0]
        img_height = img.size[1]
        band_size = 1
        white_threshold = 10 #if row has > white, it belongs to resource name
        band_array = []

        #Find horizontal index to crop
        ############################################################################
        #coords local to small snippet
        for y in range(0, (img_height - (img_height%band_size)), band_size):
            color_count = 0 #reset every row
            for x in range(0, img_width):
                color = white_img.getpixel((x, y))
                if color  == (255, 255, 255):
                    color_count += 1
            #print color_count
            if color_count > white_threshold:
                band_array.append(1)
            else:
                band_array.append(0)

        one_in_a_row = 0
        name_height = 8 #assuming font of resource name is 8px tall
        start_dex = 0
        for i in range(0, len(band_array)):
            if band_array[i] == 0:
                one_in_a_row = 0
            else:
                one_in_a_row += 1
            if one_in_a_row == name_height:
                start_dex = i - name_height
                break
        #horizontally crop immediatelly so next step faster
        #13 assumed to be name height
        cropped_hor = img.crop((0, start_dex - 1, img_width, start_dex + 13))

        #Find vertical slice points to crop
        ############################################################################
        band_array = []
        for x in range(0, cropped_hor.size[0]):
            color_count = 0 #reset every column
            for y in range(0, cropped_hor.size[1]):
                color = cropped_hor.getpixel((x, y))
                if color  == (255, 255, 255):
                    color_count += 1
            if color_count > 1: #detect even 1 white pixel
                band_array.append(1)

            else:
                band_array.append(0)
        #print band_array
        one_in_a_row = 0
        ver_start_dex = 0
        for i in range(0, len(band_array)):
            if band_array[i] == 0:
                one_in_a_row = 0
            else:
                one_in_a_row += 1
            if one_in_a_row == 2: #3 white in a raw == name
                ver_start_dex = i - 3
                break

        cropped_ver = cropped_hor.crop((ver_start_dex - 1, 0, ver_start_dex + self.name_len, cropped_hor.size[1]))

        result = cropped_ver.filter(ImageFilter.EDGE_ENHANCE_MORE)
        result = cropped_ver.filter(ImageFilter.FIND_EDGES)
        result = pytesseract.image_to_string(result)
        result = unicode(result, "utf-8")
        result = unicodedata.normalize('NFKD', result).encode('ascii','ignore')
        return result

    def are_names_similar(self, to_match, against):
        '''How to_match is similar to against'''
        #print to_match
        #print against
        perc = SequenceMatcher(None, to_match, against).ratio()
        #print perc
        if perc > 0.65:
            return True
        else:
            return False

    def resource_available(self, coord):
        '''false if resource has been gathered alreay or too high level'''
        #CURSOR IS ON TOP MOST PIZEL OF ARROW (BLACK)
        win32api.SetCursorPos(coord) #global coord
        coord = self.correct_cursor(take_offset(coord))
        time.sleep(0.15)
        top_left_red_square = (coord[0] + 19, coord[1] + 20) #global coord
        availbale = True
        red_count = 0
        img = screenGrab()
        for x in range(0, 3):
            for y in range(0, 3):
                if rgb_eq(img.getpixel(take_offset((top_left_red_square[0] + x, top_left_red_square[1] + y))), (211, 22, 29)):
                    red_count += 1
        if red_count == 9:
            availbale = False
        return availbale

    def are_same_resource(self, a, b):
        '''
        HAS TO WORK WITH GLOBAL COORDS OTHERWISE CURSOR ISNT RIGHT
        2 points a and b belongs to same resource if by moving from a to b,
        a remains of the same lighter color, otherwise if a gets darker it means
        the cursor moved to another resource.
        Not all points of a cereal change color, so many points are considered'''
        win32api.SetCursorPos(a) #global coord
        #print take_offset(a)
        time.sleep(0.2) #wait that cursor is drawn
        img = Player.screenGrab()
        a = self.correct_cursor(take_offset(a)) #returns local coords
        color_a_focus_a = []
        color_a_focus_b = []
        #print a
        #img.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
        #-1 otherwise cursor color considered, take_offset to global coord--> local
        #print (a[0]-1, a[1]-1)
        for x in range(0, 9):
            for y in range(0,1):
                color_a_focus_a.append(img.getpixel((a[0]-1-x, a[1]-1-y)))
        #print "color a focus a, img coord (" + str(take_offset((a[0]-1, a[1]-1))) + ") "+ str(color_a_focus_a)

        #move cursor to b and check color of a
        win32api.SetCursorPos(b)
        time.sleep(0.2)
        img = Player.screenGrab()
        #img.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
        for x in range(0, 9):
            for y in range(0,1):
                color_a_focus_b.append(img.getpixel((a[0]-1-x, a[1]-1-y)))
        #print color_a_focus_a
        #print color_a_focus_b
        for i in range(0, len(color_a_focus_a)):
            if  rgb_eq(color_a_focus_a[i], color_a_focus_b[i]):
                continue
            else:
                return False
        return True

    def remove_aliases(self, cord_list):
        ''' deletes from list of tuples representing COORDS
        those that are the same resource'''
        ignore = []
        for i in range(0, len(cord_list)):
            if cord_list[i] in ignore:
                #print "ignored"
                pass #coord is near an already considered
            else:
                for other in range(i+1, len(cord_list)):
                    if cord_list[i] == (713, 335) or cord_list[other] == (713, 335) or\
                        cord_list[i] == (743, 335) or cord_list[other] == (743, 335):
                        print "being considered"
                    if abs(cord_list[i][0] - cord_list[other][0]) < 50 and\
                       abs(cord_list[i][1] - cord_list[other][1]) < 50:
                       if self.are_same_resource(cord_list[i], cord_list[other]):
                           if cord_list[i] == (713, 335) or cord_list[other] == (713, 335) or\
                               cord_list[i] == (743, 335) or cord_list[other] == (743, 335):
                               print "(considered are close) (kept, ignored): " + str((cord_list[i], cord_list[other]))
                           ignore.append(cord_list[other])
                           print "---------------"
                           #adding a coord 2 times it's okay set-wise
        return list(set(cord_list) - set(ignore))

class Wheat(Resource):

    def __init__(self):
        self.name = "Wheat"
        self.name_len = len(self.name)*10

    def get_map_wheat(self, pos):
        '''Checks if wheat position in the map has been mapped and returns a
        list of coords.'''
        pass



    def is_wheat(self, coord):
        '''Takes global coord and checks if its whaet'''
        img = self.grab_resource_dialog(coord)
        name = self.extract_resource_name(img, self.name)
        return self.are_names_similar(name, self.name)

    def get_coords(self):
        '''divide screen in squares of size square_size and check wheather they
        contain > pixels of color wheat_colors than whe t_threshold, if yes add to
        wheat coords'''
        wheat_coords = []
        square_size = 30
        #img.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
        #LOCAL COORDS
        for x in range(left_corner[0] + 1, (right_corner[0] - (right_corner[0]%square_size)+1), square_size):
            for y in range(left_corner[1] + 1, (right_corner[1] - (right_corner[1]%square_size)+1), square_size):
                #print "sqr:" + str(x) + " " + str(y)
                #for every block do:
                if self.is_cereal((x, y)):
                    if self.is_wheat((x, y)):
                        wheat_coords.append((x, y))
                        print wheat_coords

        #Wheat coords are local
        wheat_coords_world = map(add_offset, wheat_coords)
        print "wheat coords raw: " + str(wheat_coords_world)
        return wheat_coords_world
        filtered = filter(self.is_cereal, wheat_coords_world)
        print "wheat coords filtered is_cereal: " + str(filtered)
        filtered2 = filter(self.is_wheat, wheat_coords_world)
        print "wheat coords filtered is_wheat: " + str(filtered2)
        return filtered2
        return self.remove_aliases(filtered)
