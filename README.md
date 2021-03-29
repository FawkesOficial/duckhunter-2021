# DuckHunter 2021.1
---

DuckHunter HID converter for the NetHunter App version 2021.1 (2021010600).\
Based on the original repo [byt3bl33d3r/duckhunter](https://github.com/byt3bl33d3r/duckhunter).\
<img src="https://user-images.githubusercontent.com/45067011/112870984-b7618000-90b6-11eb-9043-e5d6837f0c91.png" width="380" height="200"/>\
\* Tested on a Redmi Note 4(mido):
* ROM: Liquid Remix 9.0.8-20180317-Official_Nikhil-mido
* Kernel: 3.18.102-Evil-Kernel
* Android Version: 8.1.0
```diff
- NOTE: This script currently only supports characters included in [a-z], [a-Z] and [0-9].
```
It is possible to add support to other characters such as '!', but you will need to use something like:\
`echo "1 --left-shift" | /system/xbin/hid-keyboard /dev/hidg0 keyboard`
