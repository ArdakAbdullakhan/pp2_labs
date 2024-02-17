import re

txt = "icmds Mkdco moemc Pxskmcmks"
pattern = re.compile('(?=[A-Z])')
print(pattern.sub(' ', txt))