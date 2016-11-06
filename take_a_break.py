# take a break
import time
import webbrowser


def have_fun():
    webbrowser.open("https://shouly.github.io/", 0, True)


count = 3
for i in range(count):
    time.sleep(5)
    i += 1
    have_fun()
