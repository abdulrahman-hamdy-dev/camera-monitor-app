[app]
title = Camera Monitor
package.name = cameramonitor
package.domain = org.abdo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,requests,urllib3,openssl
orientation = portrait
# أهم تعديل في الصلاحيات
android.permissions = CAMERA, INTERNET
android.api = 30 
android.minapi = 21
android.ndk = 25b
# الغي السطر ده حالياً عشان ما يعملش Crash للكاميرا
# android.services = Monitor:service.py 
