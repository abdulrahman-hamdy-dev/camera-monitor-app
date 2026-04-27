 [app]
title = Camera Monitor
package.name = cameramonitor
package.domain = org.abdo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# التعديل هنا: شيلنا urllib3 و openssl لأن kivy بتسحبهم تلقائي وبسببهم كان بيحصل تعارض
requirements = python3,kivy==2.3.0,requests
orientation = portrait

android.permissions = CAMERA, INTERNET
# التعديل هنا: رفعنا الـ API لـ 33 عشان يوافق النسخة اللي جيتهاب شغال بيها حالياً في الصور
android.api = 33
android.minapi = 21
# التعديل هنا: سيبنا الـ NDK فاضي عشان Buildozer يختار النسخة الأنسب للـ API 33 أوتوماتيك
android.ndk = 

# السطر ده مهم جداً لقبول الشروط آلياً
android.accept_sdk_license = True

# android.services = Monitor:service.py
