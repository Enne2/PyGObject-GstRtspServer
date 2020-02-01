import sys, os, time
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GLib, GObject, GstRtspServer
import json

Gst.init(None)

port = "8554"

server = GstRtspServer.RTSPServer.new()
server.set_service(port)
mounts = server.get_mount_points()
factory = GstRtspServer.RTSPMediaFactory.new()
factory.set_launch("videotestsrc ! videoconvert ! theoraenc ! queue ! rtptheorapay name=pay0")
mounts.add_factory("/test", factory)
server.attach()

#  /* start serving */
print ("stream ready at rtsp://127.0.0.1:%s/test\n", port);

loop = GLib.MainLoop()
loop.run()
