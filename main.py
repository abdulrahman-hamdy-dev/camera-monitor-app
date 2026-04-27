from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.camera import Camera # 1. استيراد الكاميرا

class CameraMonitorApp(App):
    def build(self):
        # 2. إعداد الواجهة
        self.layout = BoxLayout(orientation='vertical')
        self.image = Image()
        
        # 3. تعريف الكاميرا وتشغيلها (ده اللي كان ناقص)
        from kivy.uix.camera import Camera
        self.camera = Camera(play=True, resolution=(640, 480))
        
        # 4. إضافة العناصر للواجهة
        self.layout.add_widget(self.image)
        # ملاحظة: مش لازم add_widget(self.camera) لو عايز تعرض في الـ Image بس
        
        # 5. جدولة التحديث كل 1/30 ثانية
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        
        return self.layout

    def update(self, dt):
        # 6. المعالجة الأساسية عشان السيرفر ما يكرشش (Null-Safety)
        if self.camera and self.camera.texture:
            self.image.texture = self.camera.texture
        else:
            # لو مفيش كاميرا (زي حالة السيرفر) اخرج وما توقفش البناء
            return

if __name__ == '__main__':
    CameraMonitorApp().run()
    
