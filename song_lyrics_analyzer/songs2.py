# from tkinter import StringVar
from kivy.app import App
from lyrics_extractor import SongLyrics
# from tkinter import *
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.config import Config 
from kivy.uix.scatter import Scatter
from kivy.lang import Builder  

class TutorialApp(App):
      
    def build(self):
  
        b = BoxLayout(orientation ='vertical')
  
        # Adding the text input
        t = TextInput(text="Enter Song name : ",
                      font_size = 50,
                      size_hint_y = None
                      )
          
        f = FloatLayout()
        y = AnchorLayout(
            anchor_x ='center', anchor_y ='top')
        q = Label()
        # grid = GridLayout()
  
        # By this you are able to move the
        # Text on the screen to anywhere you want
        # s = Scatter()
        def get_lyrics():
            extract_lyrics = SongLyrics("AIzaSyDYxm7BSo2ScHWBjhkCeTbRkUBH8qRI5DM","baf4c9b4758d46256")
            temp = extract_lyrics.get_lyrics(str(t))
            res = temp['lyrics']
            result.s(res)
        result = str

        # g = Label(text="Enter Song name : ")
     
     

        # b.add_widget(grid)
        b.add_widget(y)
        # b.add_widget(g)
        y.add_widget(t)
        b.add_widget(f)
        b.add_widget(q)
 
  
        # Binding it with the label
        # t.bind(text = l.setter('text'))
  
          
        return b
  
# Run the App
if __name__ == "__main__":
    TutorialApp().run()