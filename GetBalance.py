import urllib, json
import time
from Tkinter import *

root = Tk()
root.wm_title("Blockchain.info Balances")
text = Text(root)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
scrollbar.config( command = text.yview )

with open('addr.txt', 'r') as f:
    for line in f:
		addr = line
		url = "https://blockchain.info/q/addressbalance/" + addr
		response = urllib.urlopen(url);
		data = json.loads(response.read())
		sdata = format(data / 100000000.0, '.8f')
		text.insert(INSERT, '\n' + line + sdata + ' BTC\n')	

text.insert(END, '\n')
text.pack()
mainloop()