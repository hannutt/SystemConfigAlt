System data collector app.
Project keywords: Python, Kivy, Cross-platform, KV-language, Matplotlib, system info

The program collects and displays system information about your device. The program also allows you 
to manage running processes.

MAIN FEATURES:

SYSTEM INFORMATION:

View free and used memory and disk space. These features are made with the Psutil and Shutil libraries.
Check your internet connection status and speed. This feature uses the Urrlib and Speedtest libraries to determine connection information.

Operating system information, miscellaneous information about the operating system, such as name, version, etc.
Battery status, see battery charge in text and graphic format.

CURRENTLY RUNNING APPLICATIONS

See currently running applications. This is done with the Pywinauto Desktop library.
Applications are displayed in a simple list

CLOSE RUNNING APPLICATION

You can close a running application with a mouse click. Every running application has a PID (Process ID),
which is needed to close the application. Process-id is obtained using the Psutil library.
In this view you can also see the start time of each program

GRAPHIC DIAGRAMS OF SYSTEM DATA
You can make graphs of free and used memory, disk space, etc. This feature is made with the Matplotlib library.
