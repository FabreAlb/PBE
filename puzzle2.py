import puzzle1_def as lec
import gi, threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class LabelWindow(Gtk.Window):
    def __init__(self):
        
        #inicialitzar css
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path("/home/pi/Desktop/Puzzle2/p_css.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            cssProvider,     
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        super().__init__(title="rfid_gtk.py")
        
        self.box=Gtk.Box(spacing=10)
        
        #vbox
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox.set_name("box")
        self.vbox.set_homogeneous(False)
        self.box.pack_start(self.vbox, True, True, 0)
        
        #label
        self.label = Gtk.Label(label="Please, login with your university card")
        self.label.set_use_markup(True)
        self.label.set_size_request(500,100)
        self.vbox.pack_start(self.label, True, True, 0)
        
        #button
        self.button = Gtk.Button.new_with_label("Clear")
        self.button.connect("clicked", self.clicked)
        self.vbox.pack_start(self.button, True, True, 0)
        
        #Thread read uid
        t= threading.Thread(target=self.readUid)
        t.start()
          
        self.p_inici = "yes"  #variable saber pantalla
        self.add(self.box)
    
        
    def clicked(self, button):
        #print('"Click me" button was clicked')
        t= threading.Thread(target=self.clic_boto)
        t.start()
        
    def clic_boto(self):
        if self.p_inici == "no":
            self.vbox.set_name("box")
            self.label.set_text('Please, login with your university card')
            self.p_inici = "yes"
            self.readUid()
        
    def readUid(self):
        uid=lec.Rfid().read_uid()
        self.vbox.set_name("box2")
        self.label.set_text('uid: '+uid)
        self.p_inici="no"
    
    
if __name__=="__main__":
    window = LabelWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
