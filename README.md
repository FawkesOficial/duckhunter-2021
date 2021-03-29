# DuckHunter 2021.1
---

DuckHunter HID converter for the NetHunter App version 2021.1 (2021010600).\
Based on the original repo [byt3bl33d3r/duckhunter](https://github.com/byt3bl33d3r/duckhunter).\
<img src="https://user-images.githubusercontent.com/45067011/112870984-b7618000-90b6-11eb-9043-e5d6837f0c91.png" width="380" height="200"/>\
\* Tested on a Redmi Note 4(mido):
* ROM: [Liquid Remix 9.0.8-20180317-Official_Nikhil-mido](https://androidfilehost.com/?fid=962187416754468620)
* Kernel: [3.18.102-Evil-Kernel](https://forum.xda-developers.com/t/kernel-nethunter-oreo-for-mido.3768887/)
* Android Version: 8.1.0
---
## Why?
I remade the original DuckHunter script because the current NetHunter App (as of 29/03/2021) doesn't convert STRINGs into Nethunter friendly shell scripts.
---
## How?
Following the documentation of [hid_gadget_test](https://github.com/aagallag/hid_gadget_test) I was able to add support to uppercase characters by using:\
`echo "{any letter form [a-z]} --left-shift" | /system/xbin/hid-keyboard /dev/hidg0 keyboard`
---
```diff
- NOTE: This script currently only supports characters included in [a-z], [a-Z] and [0-9].
```
It is possible to add support to other characters such as '!', but you will need to use something like:\
`echo "1 --left-shift" | /system/xbin/hid-keyboard /dev/hidg0 keyboard`
