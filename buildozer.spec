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

# PERMISOS Y LICENCIAS FORZADOS
android.accept_sdk_license = True
android.skip_android_update = False

# REGLAS DE COMPILACIÓN ESTABLES (EVITA EL ERROR DE C++)
android.api = 33
android.minapi = 21
android.ndk = 25.2.9519653
android.ndk_api = 21
p4a.branch = master
