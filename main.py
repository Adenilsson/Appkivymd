
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from plyer import vibrator

KV = '''
MDScreen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "MDTopAppBar"
            left_action_items: [["menu", lambda x: None]]
            right_action_items:[["dots-vertical", lambda x: None]]
           
        TelaLogin
        
<SenhaCard>:
    size_hint: .7, .1
    pos_hint: {'center_x': 0.5,'center_y': 0.9}
    MDLabel:
        halign: "center"
        text: 'Dica: Pato voando sobre sua cabeça.'
        color: 'red'
    MDIconButton:
        icon: 'close'
        on_release: root.closeCard()
        
        


<TelaLogin>:
    MDIcon:
        icon: 'language-python'
        font_size: 90
        pos_hint: {'center_x': .5,'center_y': 0.7}
    MDTextField:
        hint_text: 'Email:'
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        size_hint_x: .6
    MDTextField:
        hint_text: 'Senha:'
        pos_hint: {'center_x': 0.5,'center_y': 0.4}
        size_hint_x: .6
    MDRaisedButton:
        text: 'Entrar:'
        pos_hint: {'center_x': 0.5,'center_y': 0.3}
        size_hint: .6, None
         
    MDLabel:
        text: "Esqueceu sua senha:"
        color:'red'
        halign: 'center'
        pos_hint: {'center_y': 0.2}
    MDTextButton:
        text: 'Click Aqui!'
        color: 'blue'
        pos_hint: {'center_x': 0.5,'center_y': 0.16}
        size_hint: .6, None
        on_release: root.abrir_card()
'''
class SenhaCard(MDCard):
    def closeCard(self):
        self.parent.remove_widget(self)
        

class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())

    

class MyApp(MDApp):
    
        
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "300"  # "500"
        #self.theme_cls.theme_style ='Light' # 'Dark' 
        return  Builder.load_string(KV)

if __name__=="__main__":
    MyApp().run()
