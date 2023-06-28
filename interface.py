import tkinter as tk
import logics


def button():
    root = tk.Tk()
    button1 = tk.Button(root, text="Открыть файл чтения", command='')
    button1.pack()
    button2 = tk.Button(root, text="Открыть файл записи", command='')
    button2.pack()
    button3 = tk.Button(root, text="запись", command=lambda: logics.main())
    button3.pack()
    root.mainloop()


# button()

# root = tk.Tk()
#
# def open_read_files_button():
#     file_path = logics.open_read_files()
#     return file_path
#
# def open_file_write_button():
#     file_path = logics.open_file_write()
#     return file_path
#
# button1 = tk.Button(root, text="Открыть файл чтения", command=lambda: open_read_files_button())
# button1.pack()
#
# button2 = tk.Button(root, text="Открыть файл записи", command=lambda: open_file_write_button())
# button2.pack()
#
# button3 = tk.Button(root, text="запись", command=lambda: logics.main(open_read_files_button(), open_file_write_button()))
# button3.pack()
#
# root.mainloop()
