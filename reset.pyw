#! /usr/bin/env python3

'''
This program should reset or shutdown windows computer.

It's just the frontend for internal windows command line program "shutdown".
It's purpose is to enable computer shutdown/restart for remote session.

author: ondrejh.ck@email.cz
date: 3.7.2014

'''

power_ico = b'R0lGODlhYABgAIABAC4uLv///yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAABgAGAAAAL+jI+pyw0Pm5y02ougjrj7b20iAJZmOW7nyk6p2MZy8KrzbdYazn861wtWfg+h0UU8Bm2ZZIKp7KSezsM0GnpRf9sRVsJthq26r6JqIJLENXNa3W2zy1h1ca7Fy4/2O3n8ZsfXt/ZHZwi3RFgYeNgoyLPo95iHCDkjOUmDtimJmXnG2bkYk6k5umfZx2LKqOoVCnpiypAYS5oju2B7S4iiuyuqx4vhiQRYiyulDCbcSzzkG43sIH3BfOyYDd18Oa29TV3t/Z1aLh5MTsHdzR6H3m5+Dv4sPw+77P56lU+/rv7O3j0YPgDuw9dP4D99BrMoHEgwnbNrlUCskgiPYsTlX+wauqnHL2DIj/EEeiR5EMowhCiTOTvZEuDFluNEwaSp7mZMaDpR5tRHk1JFoSODgmSJyp/RmSs3Gm2qMuWOp0edSgVC9eopokipGmTq9WvPL2ChTs2adKjIojg9lm3LcKySt2bPBqVb165PvFqx7r1pjWTgkhmNYCP80DDfqmwHLWbcVcjhhY9lGEsot+BkiEpZAcOc2eFmjZc9f7bYakUrVxxXe1jtNxfs2HlDI56NO/Ks3Lwbm+4NXDLw3o6Hw45i/DjZ5KMVMwda/LluM9J9C66+NaxxtLdpcec88TvlxDcKAAA7'
reset_ico = b'R0lGODlhYABgAIABAC4uLv///yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAABgAGAAAAL+jI8ZwOoPo5y0Goat3rwrnHniSF5guJ1qU7bfWq2y7JYzAN36XXd8sgvqepqhSYj8EXPJplO1fDyn1CiQim1aj9mu0OoNI4nicrBnTitt6jaM5I5DR/I6imPP43x6O79flwKYVzRISGHYh5j45aAlwUjzNxMRCYIm6Ri5lXk1uPVy6akIKnXH5VcKyYIqpxqz1+r26pFKO9l2K2KrWxjYK+gKHBw3TJxrjFuWzObFTDb1DDomTUtZjZ2tvc3d7f0NHi5ecz3evGOuTJ1eGcY+asb+C87rXc99+H2PL6w/z8+L1TNSRwYSPCCql6FQp6Yt1DQniiUmb1xYaogAnbpbTavWwbsYsR1IZBNGqvFl0h3KlFg2skxS62WVmDIf7aoJEw7OMxZ3rjnn8wS0oAmHEuV0tFRQazh1AUL489Y/WRilpqFY0eDMklm18TxW9d3KWGLpFC17k+yEAgA7'
exit_ico = b'R0lGODlhYABgAIABAC4uLv///yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAABgAGAAAAL+jI+pywkPY2y02ouZ3HznD4ZHR5aQiKajybLqe7VyC9fOjLv2m/f0HvIJf8DY8FgqVpBMk3LRjJKeCKmVQw1ct5In93sCgseA3dVyhkVRaxXT9mYflUjRPHv/DLMrH0jIpwCIMRh400OIaAiluNS4KPiokQNJIRmJU+mY2UCpuSnTyfkJSnQYSlqqc2qaKjqD2er6Kjs6awlblXuLtqvly0u7+osajFtsayzsRCyrHKsD/Dz5Iz0NndQ8fM3qRPYNHi4+Tl5ufo6err7O3u7+Dh8vP09fb3+Pv64tdctpzd0nWjGA2Kbsy0ZQF6pkCUcx5Gbr4bWI/6Ylk6iMIUZxYxo39nvoyaLEkM9IdmOWceMlVysVVqzU0uVLQ356mYQZ86SzQIVs3uTT00hNoEGFDvWyJ0geM0v/1KkRJ0UbpVHdWPHZhGm+CWK2PkCaDw8+nvYW1dMUL9W7j+lSloMoLuHBNHIDTq3LqClerAYrFQAAOw=='

from tkinter import *
from subprocess import call

#application class
class runapp(Frame):
	''' gui with shutdown and restart button '''
	
	def __init__(self,master=None):
		self.root = Tk()
		self.root.title('Shutdown GUI')
		Frame.__init__(self,master)

		self.root.iconbitmap(default='power.ico')

		#set window fixed size (non resizable)
		self.root.resizable(width=False, height=False)

		self.createWidgets()
		
	def createWidgets(self):

		self.icons = [PhotoImage(data=power_ico),PhotoImage(data=reset_ico),PhotoImage(data=exit_ico)]

		# buttons
		self.frmButtons = Frame(master=self.root)
		self.frmButtons.pack(fill=X)
		self.btnShutdown = Button(master=self.frmButtons,text='Shutdown',image=self.icons[0],command=self.fShutdownClick)
		self.btnShutdown.pack(side=LEFT,padx=5,pady=5)
		self.btnReset = Button(master=self.frmButtons,text='Reset',image=self.icons[1],command=self.fResetClick)
		self.btnReset.pack(side=LEFT,padx=0,pady=5)
		self.btnExit = Button(master=self.frmButtons,text='Exit',image=self.icons[2],command=self.fExitClick)
		self.btnExit.pack(side=LEFT,padx=5,pady=5)

	def fShutdownClick(self):
		#should run "shutdown -s -t 0"
		call('shutdown -s -t 0')
		exit()

	def fResetClick(self):
		#should run "shutdown -r -t 0"
		call('shutdown -r -t 0')
		exit()

	def fExitClick(self):
		#just exit
		exit()

	def _quit(self):
		print('kooonec')
		self.root.quit()     # stops mainloop
		self.root.destroy()  # this is necessary on Windows to prevent
					# Fatal Python Error: PyEval_RestoreThread: NULL tstate

if __name__ == "__main__":
	app = runapp()
	app.mainloop()
	# If you put root.destroy() here, it will cause an error if
	# the window is closed with the window manager.
