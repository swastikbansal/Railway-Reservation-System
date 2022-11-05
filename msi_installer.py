
from cx_Freeze import setup,Executable
import sys

base=None
if sys.platform=="win32":
    base="Win32GUI"

description="""
                            Railway Reservation Program

This Program has been created by "Python Adda(C)" using "Python Programming Language",
As in today's world, everything is online and digital but there are many people who don't know 
how to use devices properly. People have trouble booking tickets online and with secure payment. 
This project is a small initiative to help people book tickets online easier and more interactively. 
It will make booking tickets easier. To make online ticket booking more adaptable and easier to understand 
for people who are not good in operating systems, by the use of images and other more readable things. 
We have used GUI (Graphical User Interface) so it is easier to understand and the Databases can be reset 
by admins at their will. This Program uses tkinter module for GUI and mysql.connector module for Database Connection.

                                Copyright Notice

This Software and its contents are Copyright of © 2022 Python Adda. All Rights Reserved.

Any redistribution or reproduction of part or all of the contents in any form is prohibited
other than the following:-

    -> You may use the source code as a part of your project but the Name of our organization, "Python Adda(C)"
       must be mentioned.

For source code and other details of this project you must contact to Python Adda.

Instagram: python.adda
Email: python-adda@outlook.com
Website: https://python-adda.wixsite.com/python-adda
"""
executables=[Executable("Railway Reservation System.py",
                        base=base,
                        icon=r"Images\locomotive.ico",
                        shortcut_name="Book Railway Ticket",
                        shortcut_dir="DesktopFolder",
                        copyright="Copyright (C) 2022 Python Adda")]

setup(
    name="Railway Reservation Program",
    options={"build_exe":{"packages":["tkinter","tkcalendar","mysql.connector"],"include_files":["Images"]},
            "bdist_msi":{"install_icon":r"Images\Python Adda.ico"}},
    version="1.0",
    author="Python Adda",
    description=description,
    executables=executables
    )