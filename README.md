# PyGObject-GstRtspServer
#### Simple implementetion of GstRtspServer using Python GObject Introspection
I found no examples of Gstreamer's RTSP server implementation using GObject Python introspection, so this is a working script deducted from the C examples available at https://gitlab.freedesktop.org/gstreamer/gst-rtsp-server.
It could be useful for Rasperry Pi camera stream projects.

Install dependencies
------------

```sh
sudo apt install python3 python3-gst-1.0 \
    gstreamer1.0-plugins-bad gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly \
    gstreamer1.0-tools gstreamer1.0-x \
    gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 gir1.2-gst-plugins-bad-1.0 gir1.2-gst-rtsp-server-1.0
```
