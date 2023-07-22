import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    path = open("data/irma.csv")
    lines = path.readlines()
    t.penup()   
    t.setpos(-30.3, 16)
    for line in lines[1:]:
        t.speed(9)
        values = line.split(",")
        longY = float(values[2])
        latX = float(values[3])
        wind = float(values[4])
        if int(wind) < 74:
            t.pensize(2)
            t.color("white")
        if int(wind) >= 74 and int(wind) <= 95:
            t.pensize(3)
            t.color("blue")            
            t.write(1) # category 1
        if wind > 95 and wind < 111:
            t.pensize(4)
            t.color("green")
            t.write(2) #category 2
        if wind >= 111 and wind <= 129:
            t.pensize(6)
            t.color("yellow")
            t.write(3) # category 3
        if wind >= 130 and wind <= 156:
            t.pensize(8)
            t.color("orange")
            t.write(4) # category 4
        if wind >= 157:
            t.pensize(10)
            t.color("red")
            t.write(5) # category 5
        t.setpos(latX,longY)

        t.pendown()
    turtle.done()
    # your code to animate Irma here
   
    
    
if __name__ == "__main__":
    irma()

