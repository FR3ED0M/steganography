from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
parent = Tk()


# choose original image
class openImage1:
    def openPlains(self):
        image = Image.open("images/plains.jpg")             # opens an image from database
        image = image.resize((250, 250), Image.ANTIALIAS)   # resizes the image to 250x250
        image.save('images/new_image.png')                  # saves the image under a new name and datatype
        photo = ImageTk.PhotoImage(image)       # creates image as a "photo" so .jpg can be opened
        label4 = Label(image=photo)             # creates label where image will be placed
        label4.image = photo                    # put image into the label placeholder
        label4.place(x=10, y=75)                # geometry as to where image will go when opened
        return

    def openBoxy(self):
        image = Image.open("images/boxy.jpg")
        image = image.resize((250, 250), Image.ANTIALIAS)
        image.save('images/new_image.png')
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openColors(self):
        image = Image.open("images/colors.jpg")
        image = image.resize((250, 250), Image.ANTIALIAS)
        image.save('images/new_image.png')
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openSpace(self):
        image = Image.open("images/space.jpg")
        image = image.resize((250, 250), Image.ANTIALIAS)
        image.save('images/new_image.png')
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openPlasma(self):
        im = Image.open("images/plasma.jpg")
        im = im.resize((250, 250), Image.ANTIALIAS)
        im.save('images/new_image.png')
        ph = ImageTk.PhotoImage(im)
        label4 = Label(image=ph)
        label4.image = ph
        label4.place(x=10, y=75)
        return


# choose watermark
class openImage2:
    def openPlains(self):
        wm = Image.open("images/plains.jpg")
        # wm = wm.resize((250, 250), Image.ANTIALIAS)
        wm = wm.resize((160, 120), Image.ANTIALIAS)
        wm.save('images/watermark.png')
        watermark = ImageTk.PhotoImage(wm)
        label2 = Label(image=watermark)
        label2.image = watermark
        label2.place(x=300, y=75)
        return

    def openBoxy(self):
        wm = Image.open("images/boxy.jpg")
        # wm = wm.resize((250, 250), Image.ANTIALIAS)
        wm = wm.resize((160, 120), Image.ANTIALIAS)
        wm.save('images/watermark.png')
        watermark = ImageTk.PhotoImage(wm)
        label2 = Label(image=watermark)
        label2.image = watermark
        label2.place(x=300, y=75)
        return

    def openColors(self):
        wm = Image.open("images/colors.jpg")
        # wm = wm.resize((250, 250), Image.ANTIALIAS)
        wm = wm.resize((160, 120), Image.ANTIALIAS)
        wm.save('images/watermark.png')
        watermark = ImageTk.PhotoImage(wm)
        label2 = Label(image=watermark)
        label2.image = watermark
        label2.place(x=300, y=75)
        return

    def openSpace(self):
        wm = Image.open("images/space.jpg")
        # wm = wm.resize((250, 250), Image.ANTIALIAS)
        wm = wm.resize((160, 120), Image.ANTIALIAS)
        wm.save('images/watermark.png')
        watermark = ImageTk.PhotoImage(wm)
        label2 = Label(image=watermark)
        label2.image = watermark
        label2.place(x=300, y=75)
        return

    def openPlasma(self):
        wm = Image.open("images/plasma.jpg")
        # wm = wm.resize((250, 250), Image.ANTIALIAS)
        wm = wm.resize((160, 120), Image.ANTIALIAS)
        wm.save('images/watermark.png')
        watermark = ImageTk.PhotoImage(wm)
        label2 = Label(image=watermark)
        label2.image = watermark
        label2.place(x=300, y=75)
        return


# creates a popup for the user to select
# pictures from the those that come with the program
def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()


def do_popup2(event):
    try:
        popup2.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup2.grab_release()


# embed a watermark into the original selected image
def embedImage(z=5):
    data = Image.open("images/new_image.png")
    data = data.resize((250, 250), Image.ANTIALIAS)
    key = Image.open("images/watermark.png").resize(data.size)
    data.getpixel((0, 0))
    key.getpixel((0, 0))
    for i in range(data.size[0]):
        for j in range(data.size[1]):
            p = data.getpixel((i, j))
            q = key.getpixel((i, j))
            red = (int(p[0])) - (int(p[0] % z)) + (int(z * q[0] / 255))
            green = (int(p[1])) - (int(p[1] % z)) + (int(z * q[1] / 255))
            blue = (int(p[2])) - (int(p[2] % z)) + (int(z * q[2] / 255))
            data.putpixel((i, j), (red, green, blue))
    ph2 = ImageTk.PhotoImage(data)
    label3 = Label(image=ph2)
    label3.image = ph2
    label3.place(x=600, y=75)
    data.save("images/inside.png")
    return


# extract the watermark from the original selected image
# ERROR: ONLY SMALL SECTION OF WATERMARK IS GETTING EXTRACTED
def xtractImage(z=5):
    data = Image.open("images/inside.png")
    for i in range(data.size[0]):
        for j in range(data.size[1]):
            p = data.getpixel((i, j))
            red = (int(p[0] % z) * (int(255 / z)))
            green = (int(p[1] % z) * (int(255 / z)))
            blue = (int(p[2] % z) * (int(255 / z)))
            data.putpixel((i, j), (red, green, blue))
    data = data.resize((160, 120), Image.ANTIALIAS)
    ph3 = ImageTk.PhotoImage(data)
    label4 = Label(image=ph3)
    label4.image = ph3
    label4.place(x=890, y=75)
    data.save("images/xtract.png")
    return


# creates the popup menu to choose images from database
x = openImage1()
y = openImage2()

# tear off the menu from the button
popup = Menu(parent, tearoff=0)
popup2 = Menu(parent, tearoff=0)

# choice of 640 x 480 images
popup.add_command(label="Boxy", command=x.openBoxy)
popup.add_command(label="Colors", command=x.openColors)
popup.add_command(label="Space", command=x.openSpace)
popup.add_command(label="Plains", command=x.openPlains)
popup.add_command(label="Plasma", command=x.openPlasma)

# choice of 160 x 120 watermark images
popup2.add_command(label="Boxy", command=y.openBoxy)
popup2.add_command(label="Colors", command=y.openColors)
popup2.add_command(label="Space", command=y.openSpace)
popup2.add_command(label="Plains", command=y.openPlains)
popup2.add_command(label="Plasma", command=y.openPlasma)

# title of window
parent.title('Image Process')

# frame of the window
frame = ttk.Frame(parent, borderwidth=5)

# buttons, as well as the bind for clicking to get the popup menu
select = ttk.Button(parent, text="Select Image")
select.bind("<Button-1>", do_popup)
wmImage = ttk.Button(parent, text="Select Watermark")
wmImage.bind("<Button-1>", do_popup2)
wmEmbed = ttk.Button(parent, text="Embed Watermark", command=embedImage)
wmXtract = ttk.Button(parent, text="Extract Watermark", command=xtractImage)


# placement geometry of frame and buttons
select.place(x=10, y=15)
wmImage.place(x=300, y=15)
wmEmbed.place(x=600, y=15)
wmXtract.place(x=890, y=15)

# geometry of the main "parent" frame and window
parent.geometry("1075x375")

parent.mainloop()