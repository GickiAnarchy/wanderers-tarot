[app]

# (str) Application versioning (method 1)
version = 0.1

# (str) Title of your application
title = The Digital Oracle

# (str) Package name
package.name = tarotoracle

# (str) Package domain (needed for android packaging)
package.domain = com.gickistudios

# (str) Source code where the main.py live
source.dir = .

# App icon
#icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/splash.png

# (list) Source files to include (let's include .kv files!)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Added certifi, requests, and charset-normalizer for Google API stability
requirements = python3, kivy, google-generativeai, requests, certifi, urllib3, charset-normalizer, idna

# (str) Application versioning (method 2)
version.filename = %(source.dir)s/main.py

#version.regex = __version__ = ['"](.*)['"]

# (str) Custom source folders for requirements
# android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Android API to use (Targeting Android 14)
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (list) Android architecture to build for
# Most modern phones need arm64-v8a
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) The orientation of the app
orientation = portrait

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False)
warn_on_root = 1
