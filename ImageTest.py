from tkinter import *     
from tkinter import filedialog
import os

def walk_dir(root_dir, extension):
    file_list = []
    towalk = [root_dir]
    while towalk:
        root_dir = towalk.pop()
        for path in os.listdir(root_dir):
            path = os.path.join(root_dir, path).lower()
            for i in extension:
                if os.path.isfile(path) and path.endswith(i):
                    file_list.append(path)
                elif os.path.isdir(path):
                    towalk.append(path)
    return file_list


root_dir = str(filedialog.askdirectory(title = "Select Location" ))
extension = ['.png']
image_list = walk_dir(root_dir, extension)
image_list.sort()

print(image_list)
def change(num,image_list):
	global next_Button
	global previous_Button
	global canvas
	global img
	global my_label

	my_label = Label(root,text = "Image " + str(num) + " of " + str(len(image_list)))
	my_label.grid(row = 2 , column = 0 , columnspan = 3)
	canvas = Canvas(root,width = 1360 , height = 620) # Canvas
	
	previous_Button = Button(root,text = "< Previous", command = lambda : change(num-1,image_list))
	next_Button = Button(root,text = "Next >", command = lambda : change(num+1,image_list))


	canvas.grid_forget()
	canvas.grid(row = 1, column = 0, columnspan = 3)
	
	img = PhotoImage(file=(image_list[num-1])) 
	canvas.create_image(1,1, anchor=NW, image=img)
	if num == len(image_list):
		next_Button = Button(root, text = "Next >", state=DISABLED)
	if num == 1:
		previous_Button = Button(root, text="< Previous", state=DISABLED)

 # Next button
	next_Button.grid(row = 0, column = 1)

 # Previous button
	previous_Button.grid(row = 0, column = 0) 



	exit = Button(root,text = "Exit X" , command = lambda : quit()) # Exit Button
	exit.grid(row = 0, column = 2)



root = Toplevel()
mastet = Canvas


change(1,image_list)





root.mainloop()