[app]
title = Steelmat Presupuestador
package.name = steelmatapp
package.domain = org.steelmat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

# PARCHES CRÍTICOS PARA EVITAR EL EXIT CODE 1:
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.skip_android_update = False
p4a.branch = master
