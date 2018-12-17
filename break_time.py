import webbrowser
import time
t = 0

print ("this program started on" + time.ctime())
while t < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=HAZJAzCshN4&start_radio=1&list=RDHAZJAzCshN4")
    t = t +1 
