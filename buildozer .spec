[app]
title = Vortex AI
package.name = vortexai
package.domain = org.vortexai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json,md,txt,pdf
version = 1.0.0
requirements = python3,kivy>=2.3.0,requests>=2.31.0,plyer>=2.1.0,pyjnius>=1.6.1,sympy>=1.14.0
orientation = portrait
fullscreen = 0
android.presplash_color = #12101C
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
api = 33
minapi = 26
ndk_api = 33
permissions = INTERNET,RECORD_AUDIO,READ_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,BLUETOOTH,BLUETOOTH_CONNECT,FOREGROUND_SERVICE
android.gradle_dependencies = com.google.mlkit:text-recognition:16.0.0
android.add_aars = 
android.add_jars = 
android.arch = arm64-v8a
android.allow_backup = True
android.numeric_version = 1
