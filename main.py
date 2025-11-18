from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from plyer import filechooser
from kivymd.uix.screenmanager import ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
import json
from pathlib import Path
class Restaurant(MDApp):
    def on_start(self):
        try:
            with open("user_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                all=screen_manager.get_screen("Acceuil").navig.profile_id.data.data1.data2
                all.user_name.text = data["nom"]
                all.user_number.text = data["number"]
                all.user_photo.source = data["photo"]
                screen_manager.get_screen("Acceuil").navig.home_id.home_data.home_data1.home_data2.user_name_and_salut.text = f"Salut {data['nom']}"
                screen_manager.get_screen("Acceuil").navig.home_id.home_data.home_data1.home_data2.picture.source =data["photo"]
                screen_manager.transition.direction = "down"
                screen_manager.current = "Acceuil"
        except:
            screen_manager.current = "welcome"
    def deconnect(self):
        screen_manager.transition.direction = "right"
        screen_manager.current = "welcome"
        p = Path("user_data.json")
        if p.exists():
            p.unlink()
            print(f"Fichier supprimé : {p}")
        else:
            print(f"Le fichier n'existe pas : {p}")
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("sign_up.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        return screen_manager
    def login(self, id):
        if id==2:
            screen_manager.transition.direction = "left"
            screen_manager.current ="sign_up"
        elif id==3:
            screen_manager.transition.direction = "right"
            screen_manager.current ="login"
        elif id==4:
            screen_manager.transition.direction = "left"
            screen_manager.current ="login"
    def data_login_on(self, nom_user, password):
        data={
                "nom": "Admin",
                "photo": "user_photo.png",
                "number": "+00012345678",
                "password": "Admin@Admin"
            }
        try:
            with open("user_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            pass
        if nom_user == "":
            toast(f"imformation incorrectée...", duration=1)
        elif password != data["password"]:
            toast(f"imformation incorrectée...", duration=1)
        elif nom_user ==data["nom"] and password==  data["password"]:
            all=screen_manager.get_screen("Acceuil").navig.profile_id.data.data1.data2
            all.user_name.text = data["nom"]
            all.user_number.text = data["number"]
            all.user_photo.source = data["photo"]
            screen_manager.get_screen("Acceuil").navig.home_id.home_data.home_data1.home_data2.user_name_and_salut.text = f"Salut {data['nom']}"
            screen_manager.get_screen("Acceuil").navig.home_id.home_data.home_data1.home_data2.user_photo.source = data["photo"]
            screen_manager.transition.direction = "left"
            screen_manager.current = "Acceuil"
            toast(f"Connecté...", duration=1)
        else:
            toast(f"imformation incorrectée...", duration=3)
    def sign_in(self, nom_user, user_photo, user_number, user_password, user_repassword_confirm):
        data={
                    "nom": nom_user,
                    "photo": user_photo,
                    "number": user_number,
                    "password": user_password
                }
        try:
            all=screen_manager.get_screen("Acceuil").navig.profile_id.data.data1.data2
            all.user_name.text = data["nom"]
            all.user_number.text = data["number"]
            all.user_photo.source = data["photo"]
            screen_manager.get_screen("Acceuil").navig.home_id.home_data.home_data1.home_data2.user_name_and_salut.text = f"Salut {data['nom']}"
            screen_manager.get_screen("Acceuil").navig.home_id.home_data.home_data1.home_data2.user_photo.source = data["photo"]
            screen_manager.transition.direction = "left"
            screen_manager.current = "Acceuil"
            toast(f"Connecté...", duration=1)
            with open("user_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except:
            pass
    def add_picture(self):
        filechooser.open_file(on_selection= self.add_now)
    def add_now(self, selected):
        if selected:
            image_profile= selected[0]
            screen_manager.get_screen("sign_up").picture.source =image_profile
if __name__=="__main__":
    Restaurant().run()
