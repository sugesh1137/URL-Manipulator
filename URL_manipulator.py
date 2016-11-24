from gi.repository import Gtk
import re

#importing the Gtk librarry, the PyGObject module should be installed in the system
#along with the regular expression module
#Main Class begining
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="URL Manipulator")
        self.set_border_width(10)

        #Layout of the first class
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox)

        #First Option
        self.enter_URL = Gtk.Entry()
        self.enter_URL.set_text("Enter the URL")
        vbox.pack_start(self.enter_URL, True, True, 0)

        #parse Button
        self.button = Gtk.Button(label="Parse the URL")
        self.button.connect("clicked", self.parse_URL)
        vbox.pack_start(self.button, True, True, 0)

#Parsing the URL
    def parse_URL(self, box):
        url = self.enter_URL.get_text()
        match = re.search(r'(\w+)://(\w+).(\w+)/(\w+)/(\w+)/(\w+):(\S+)', url)
        print('URL is: ' + match.group())
        print('Scheme is: ' + match.group(1))
        print('Network location is: ' + match.group(2))
        print('Drive location is: ' + match.group(4))
        print('Folder location is: ' + match.group(5))
        print('File location is: ' + match.group(6))
        print('Port Number is: ' + match.group(7))
       
    
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
