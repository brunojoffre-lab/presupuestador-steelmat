[app]
title = Steelmat Presupuestador
package.name = steelmatapp
package.domain = org.steelmat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

# Versiones fijas para evitar el error 404 de Google
android.api = 31
android.minapi = 21
p4a.branch = master
