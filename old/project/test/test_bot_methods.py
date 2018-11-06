import sys
sys.path.append('C:\Users\Carlo\Desktop\Dofus_bot\project')
from bot import *


test_remove_alias = False
if test_remove_alias:
    #map 4, -25
    a = Wheat()
    test_set = [(413, 245), (413, 275), (533, 155), (533, 185), (563, 155), (563, 185),
    (593, 155), (593, 185), (623, 155), (623, 185), (743, 395), (743, 425)]
    print "original: "
    print test_set

    res = a.remove_aliases(test_set)
    print "result: "
    print res

test_are_same_resource = False
if test_are_same_resource:
    #for map 5, -26, low quality full screen
    test_those = [(593, 395), (593, 425), (593, 455), (623, 365), (623, 395), (623, 425),
    (623, 455), (653, 365), (653, 395), (653, 425), (683, 365), (683, 395), (683, 425),
    (713, 305), (713, 365), (713, 395), (713, 455), (743, 305), (743, 335), (743, 365),
    (743, 395), (743, 425), (743, 455), (743, 485), (773, 305), (773, 365), (773, 395),
    (773, 425), (773, 455), (803, 305), (803, 335), (803, 365), (803, 395), (803, 425),
    (803, 455), (803, 485), (833, 305), (833, 335), (833, 365), (833, 395),
    (833, 425), (863, 335), (863, 365), (863, 395), (863, 425), (863, 455),
    (893, 335), (893, 365), (893, 395)]
    a = Wheat()
    ress = a.remove_aliases(test_those)
    print ress
    print "okay"
    time.sleep(2)
    Player.hoover(ress, 1)
    exit()
    for c in test_those:
        print "should be " + str(c[2]) + " is " + str(a.are_same_resource(c[0], c[1]))
    exit()


test_resource_available= False
if test_resource_available:
    print resource_available((670, 470))

test_image_to_string = False
if test_image_to_string:
    img = screenGrab_custom((760, 286),(836, 343))
    img.save('test.jpg')
    time.sleep(1)
    img = Image.open('test.jpg')
    img.load()
    text = image_to_string(img)
    print text

test_dialog = False
if test_dialog:
    bot_l = grab_resource_dialog((902, 180))
    time.sleep(0.2)
    top_l = grab_resource_dialog((899, 131))
    time.sleep(0.2)
    bot_r = grab_resource_dialog((936, 175))
    time.sleep(0.2)
    top_r = grab_resource_dialog((933, 137))

    bot_l.save('bot_l.png', 'PNG')
    top_l.save('top_l.png', 'PNG')
    bot_r.save('bot_r.png', 'PNG')
    top_r.save('top_r.png', 'PNG')

test_extract_resource_name = False
if test_extract_resource_name:

    w = Wheat()

    bot_l = w.grab_resource_dialog((869, 517))
    test = w.extract_resource_name(bot_l, w.name_len)
    print w.are_names_similar(test, "Wheat")
    print test
    print "Barley pos vs. Wheat --------------"
    bot_l = w.grab_resource_dialog((857,322))
    test = w.extract_resource_name(bot_l, w.name_len)
    print w.are_names_similar(test, "Barley")
    print test



test_is_cereal = False
if test_is_cereal:
    a = Wheat()
    print a.is_cereal((764, 337))

test_correct_cursor = False
if test_correct_cursor:
    img = Player.screenGrab()
    img.save('look.png', 'PNG')
    off = take_offset(win32api.GetCursorPos())
    print a.correct_cursor(off)
    print "original " + str(off)
    print img.getpixel(off)

test_get_colors = False
if test_get_colors:
    img = Image.open('wheat_colors1.png')
    colors =  get_colors(img)
    with open('colors_of_resources.py', 'w') as outfile:
        outfile.write("wheat = " + str(colors))


test_is_wheat = False
if test_is_wheat:
    a = Wheat()
    print "Should be true: " + str(a.is_wheat((459, 199)))
    print "Should be f: " + str(a.is_wheat((864, 290)))
    print "Should be f: " + str(a.is_wheat((333, 186)))
    print "Not cereal: " + str(a.is_wheat((633, 380)))

test_get_wheat_coords = False
if test_get_wheat_coords:
    w = Wheat()
    #5   -26
    #got = w.get_coords()
    #with open("saved_coords.py", 'w') as save_here:
    #    save_here.write("cereals = { 'wheat' : {(5, -26) : " + str(got) + "}}")
    from saved_coords import cereals
    got = cereals['wheat'][(5, -26)]

    got = w.remove_aliases(got)
    print "okay"
    time.sleep(1)
    Player.hoover (got, 1)

test_get_pos = False
if test_get_pos:

    zoom_on_coord()
    exit()
    p = Player()
    p.get_pos()

test_movements = False
if test_movements:
    p = Player()
    p.go_to((5, -27))
    exit()
    p.go_down()
    time.sleep(6)
    p.go_up()
    time.sleep(5)
    p.go_left()
    time.sleep(5)
    p.go_right()

test_file = False
if test_file:
    f = File_manager()
    print f.get_cords("cereal", "wheat", (1, 1))
    f.add_cords("cereal", "wheat", (1, 5), [(55,5), (98,444)])
    exit()
    f.add_cord_list("cereal", "wheat", (5, -26), [1])

test_tacticmode = True
if test_tacticmode:
    p = Player()
    if p.check_tacticmode():
        print "acrive"
    else:
        p.toggle_tacticmode()
        print "acrivated"
