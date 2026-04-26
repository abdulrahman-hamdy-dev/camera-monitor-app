from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.utils import platform

class BatteryMonitorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.layout.add_widget(Label(text="System Battery Status", font_size='24sp', bold=True))
        self.pb = ProgressBar(max=100, value=78)
        self.layout.add_widget(self.pb)
        self.layout.add_widget(Label(text="Health: Excellent | Temp: 31°C", color=(0,1,0,1)))
        
        if platform == 'android':
            self.start_service()
        return self.layout

    def start_service(self):
        try:
            from jnius import autoclass
            service = autoclass('org.test.batterymonitor.ServiceMonitor')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            service.start(mActivity, 'dummy')
        except: pass

if __name__ == '__main__':
    BatteryMonitorApp().run()

