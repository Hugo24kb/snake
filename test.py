#from sketchpy import library as lib
#from sketchpy import canvas

#obj = lib.tom_holland()

#obj.draw()

from tkinter import  *
root=Tk()
root.resizable(True,True)
cv=Canvas(root)

cv.pack()

img=PhotoImage(file='/Users/hugowong/Desktop/Code/Pygame/Snake/gif/rab.gif')
img = img.zoom(4)
img = img.subsample(50)
cv.create_image((50,50),image=img, anchor=NW)

 
root.mainloop()