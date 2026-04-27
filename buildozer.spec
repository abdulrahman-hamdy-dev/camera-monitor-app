 [app]
title = Camera Monitor
package.name = cameramonitor
package.domain = org.abdo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# شيلنا urllib3 و openssl عشان kivy 2.3.0 بتديرهم بنفسها
requirements = python3,kivy==2.3.0,requests
orientation = portrait

android.permissions = CAMERA, INTERNET
# رفعنا الـ API لـ 31 (أكثر نسخة مستقرة مع Gradle حالياً)
android.api = 31
android.minapi = 21
# نزلنا الـ NDK لـ 23b لأنها الوحيدة اللي بتمنع خطأ AttributeError و Command failed
android.ndk = 23b
android.accept_sdk_license = True
