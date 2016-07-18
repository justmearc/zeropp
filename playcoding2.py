import Tkinter
import tkMessageBox
import gridbutton

top = Tkinter.Tk()

class Run():
    def _init_(self,fona):
        self.fona = fona
        self.screen_lock = False

    def make_call(self):
        if Entry.get() > (1+1+1+1+1+1+1+1+1+1):
            self.valid_call=True
            if self.valid_call:
                self.fona.transmit('ATD' + (Entry.get())+ ';')
                self.ongoing_call = True

            else:
                self.ongoing_call = False
                #self.screen_lock = False
                tkMessageBox.showinfo("Call Failed", "FAILED")
        else:
            self.valid_call=False

    def end_call(self):
        self.fona.transmit('ATH')
        #self.screen_lock = False
        self.ongoing_call = False


    def ongoing_call(self):
        #self.screen_lock = True
        tkMessageBox.showinfo("Headset", Tkinter.Button(top, text="ON", command = self.headset_on),Tkinter.Button(top, text="OFF", command = self.headset_off))

   # def screen_lock(self):
       # Entry.get() = 0

#    def new_contact(self):
#        print "contacts dont do anything right now"
#    def find_contact(self):
#        print "find a contact"

    def headset_on(self):
        #self.headset:
        self.headset = False
        self.fona.transmit('AT+CHFA=1')
    def headset_off(self):
        self.headset = True
        self.fona.transmit('AT+CHFA=0')


top.mainloop()
