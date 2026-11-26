[app]
title = RUBI AI
package.name = rubiai
package.domain = com.rubiai.assistant
source.dir = .
source.include_exts = py,png,jpg,kv,json,atlas
version = 0.1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
