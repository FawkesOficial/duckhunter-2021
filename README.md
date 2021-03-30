# DuckHunter 2021.1
---

DuckHunter HID converter script for the NetHunter App version 2021.1 (2021010600).\
Based on the original repo [byt3bl33d3r/duckhunter](https://github.com/byt3bl33d3r/duckhunter).\
<img src="https://user-images.githubusercontent.com/45067011/112870984-b7618000-90b6-11eb-9043-e5d6837f0c91.png" width="380" height="200"/>\
\* Tested on a Redmi Note 4(mido):
* ROM: [Liquid Remix 9.0.8-20180317-Official_Nikhil-mido](https://androidfilehost.com/?fid=962187416754468620)
* Kernel: [3.18.102-Evil-Kernel](https://forum.xda-developers.com/t/kernel-nethunter-oreo-for-mido.3768887/)
* Android Version: 8.1.0
---


## Links:
* [byt3bl33d3r/duckhunter](https://github.com/byt3bl33d3r/duckhunter)
* [aagallag/hid_gadget_test](https://github.com/aagallag/hid_gadget_test)
* My Nethunter full build guide [Coming soon...]
___

## Why?
I remade the original DuckHunter script because the current NetHunter App (as of 29/03/2021) doesn't convert STRINGs into Nethunter friendly shell scripts.
___

## How?
Following the documentation of [hid_gadget_test](https://github.com/aagallag/hid_gadget_test) I was able to add support to, for example, uppercase characters, by using:\
`echo "{any letter from [a-z]} --left-shift" | /system/xbin/hid-keyboard /dev/hidg0 keyboard`
___

## Keyboard Layouts:

```diff
- NOTE: This script currently only supports characters included in [a-z], [a-Z], [0-9] and some other special Shift and right-Alt keys for 'us', 'uk' and 'pt' keyboard layouts.
```
It is possible to add support to other characters such as '!', but you will need to use something like:\
`echo "1 --left-shift" | /system/xbin/hid-keyboard /dev/hidg0 keyboard`\
For any modification, I would recomend taking a look at the source code of [hid_gadget_test.c](https://github.com/aagallag/hid_gadget_test/blob/master/hid_gadget_test.c) as it shows all the options thath you have at your disposal:
```static struct options kmod[] = {
	{.opt = "--left-ctrl",		.val = 0x01},
	{.opt = "--right-ctrl",		.val = 0x10},
	{.opt = "--left-shift",		.val = 0x02},
	{.opt = "--right-shift",	.val = 0x20},
	{.opt = "--left-alt",		.val = 0x04},
	{.opt = "--right-alt",		.val = 0x40},
	{.opt = "--left-meta",		.val = 0x08},
	{.opt = "--right-meta",		.val = 0x80},
	{.opt = NULL}
};

static struct options kval[] = {
	{.opt = "--return",	.val = 0x28},
	{.opt = "--esc",	.val = 0x29},
	{.opt = "--bckspc",	.val = 0x2a},
	{.opt = "--tab",	.val = 0x2b},
	{.opt = "--spacebar",	.val = 0x2c},
	{.opt = "--caps-lock",	.val = 0x39},
	{.opt = "--f1",		.val = 0x3a},
	{.opt = "--f2",		.val = 0x3b},
	{.opt = "--f3",		.val = 0x3c},
	{.opt = "--f4",		.val = 0x3d},
	{.opt = "--f5",		.val = 0x3e},
	{.opt = "--f6",		.val = 0x3f},
	{.opt = "--f7",		.val = 0x40},
	{.opt = "--f8",		.val = 0x41},
	{.opt = "--f9",		.val = 0x42},
	{.opt = "--f10",	.val = 0x43},
	{.opt = "--f11",	.val = 0x44},
	{.opt = "--f12",	.val = 0x45},
	{.opt = "--insert",	.val = 0x49},
	{.opt = "--home",	.val = 0x4a},
	{.opt = "--pageup",	.val = 0x4b},
	{.opt = "--del",	.val = 0x4c},
	{.opt = "--end",	.val = 0x4d},
	{.opt = "--pagedown",	.val = 0x4e},
	{.opt = "--right",	.val = 0x4f},
	{.opt = "--left",	.val = 0x50},
	{.opt = "--down",	.val = 0x51},
	{.opt = "--kp-enter",	.val = 0x58},
	{.opt = "--up",		.val = 0x52},
	{.opt = "--num-lock",	.val = 0x53},
	{.opt = NULL}
};
```
___
