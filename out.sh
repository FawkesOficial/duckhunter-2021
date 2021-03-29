echo "This is a comment in ducky script"
echo "left-meta r is a windows key + r (run) or we can use left-meta"
echo -ne 'left-meta r' | /system/xbin/hid-keyboard /dev/hidg0 keyboard

echo "String will pass any text you wish"
echo -ne 'cmd' | /system/xbin/hid-keyboard /dev/hidg0 keyboard
echo -ne 'enter' | /system/xbin/hid-keyboard /dev/hidg0 keyboard

echo "We can also run "sleep" by using delay. You need to use miliseconds but we convert to seconds"
sleep 0.5
echo ""
echo -ne 'echo "Hello World!"' | /system/xbin/hid-keyboard /dev/hidg0 keyboard
echo -ne 'enter' | /system/xbin/hid-keyboard /dev/hidg0 keyboard

echo "Other keys to use are left-shift, left-alt, space, f1-f12, left-ctrl, escape, down, up, left, right"
echo -ne 'up' | /system/xbin/hid-keyboard /dev/hidg0 keyboard

echo -ne 'enter' | /system/xbin/hid-keyboard /dev/hidg0 keyboard

echo "We can combine keys and letters"
echo -ne 'left-alt f' | /system/xbin/hid-keyboard /dev/hidg0 keyboard

