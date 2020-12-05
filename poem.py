from tkinter import *

root = Tk()
part1 = Label(root, text="Jack and Jill, went up the hill",fg="Red",bg="Yellow)
part2 = Label(root, text="To fetch a pail of water, Jack fell down",fg="Red",bg="Yellow)
part3 = Label(root, text="And broke his crown, And Jill came tumbling after.",fg="Red",bg="Yellow)
part4 = Label(root, text="Up Jack got, And home did trot",fg="Red",bg="Yellow)
part5 = Label(root, text="As fast as he could caper, Went to bed",fg="Red",bg="Yellow)
part6 = Label(root, text="To mend his head, With vinegar and brown paper.",fg="Red",bg="Yellow)
part7 = Label(root, text="---THE END---")

part1.config(font = ("Arial Black",16))
part2.config(font = ("Arial Black",16))
part3.config(font = ("Arial Black",16))
part4.config(font = ("Arial Black",16))
part5.config(font = ("Arial Black",16))
part6.config(font = ("Arial Black",16))
part7.config(font = ("Arial",16))

part1.pack()
part2.pack()
part3.pack()
part4.pack()
part5.pack()
part6.pack()
part7.pack()

root.mainloop()
