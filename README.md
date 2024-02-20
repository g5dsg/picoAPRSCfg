# picoAPRSCfg

Simple Python script to load the region 1 VHF FM channels (145.200-145.575) to a [picoAPRS](http://picoaprs.de/) v4 transceiver. Given the limited number of memories it uses the old 25kHz spaced S8..S23 frequencies. It would be easy to modify for some of the 12.5kHz channels. This will leave you with a 4 memories free for other channels (eg repeaters) which can be configured via its web page as normal.

Tested on firmware v18. Requires requests library installed. Simply execute:

`python ./picoAPRSCfg <ip>`

Where IP is the IP address displayed on your picoAPRS while in web config mode. Note this will overwrite memories 1-16 without warning.

The web interface on the device is great, but a little clunky for setting multiple channels - I found it quicker/less tedious to write a quick script. Perhaps someone else will find it useful.

