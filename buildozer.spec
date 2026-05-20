[app]
title = Steelmat Presupuestador
package.name = steelmatapp
package.domain = org.steelmat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3==3.11.1,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

# PERMISOS Y LICENCIAS
android.accept_sdk_license = True
android.skip_android_update = False

# DEJAMOS QUE BUILDOZER ELIJA SUS PROPIAS VERSIONES COMPATIBLES
android.api = 33
android.minapi = 21
android.ndk_api = 21
p4a.branch = master
