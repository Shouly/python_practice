# take a break
import  time
import  webbrowser

def have_fun():
    webbrowser.open("https://github.com/Shouly/python_practice",0,True)
count = 3
i=0
for i in range(0,count):
    time.sleep(5)
    have_fun()
    i = i + 1
