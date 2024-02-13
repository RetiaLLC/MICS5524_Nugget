# MICS5524_Nugget
USB Nugget gas sensor

Use CircuitPython to read a gas sensor and turn the USB Nugget's neopixel red if gas is detected.

Optional: Add a piezo buzzer.

Sensor: https://www.aliexpress.com/w/wholesale-mics5524.html

For the DIY hacker and beginner in STEM looking to dive into environmental monitoring or safety projects, the MiCS-5524 presents a cool gadget to play with. This compact MEMS sensor is your go-to for sniffing out carbon monoxide and natural gas leaks around the house. Plus, it's a neat tool for keeping an eye on air quality, checking your breath, or even getting an early heads-up on fires.

What's nifty about the MiCS-5524 is its sensitivity to a variety of gases—carbon monoxide, ammonia, ethanol, hydrogen, and even the big players in household gas like methane, propane, and iso-butane. It can detect concentrations ranging from the low (about 1 ppm for some gases) to the quite high (over 1000 ppm for gases like methane). But here's the kicker: while it can tell you something's up in the air, it won't pinpoint exactly which gas it's detecting. So, think of it as your general alert system rather than a specialized detective.

Plug sensor output into GPIO 17 for this example. Plugging sensor into 3v produces inaccurate results, use 5v.
