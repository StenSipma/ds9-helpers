# DS9 Helpers
Some python scipts / command line utilities which makes interacting with ds9
from the command line a bit easier. Both scripts depend on pyds9, which is a
Python interface for DS9's XPA protocol.

- `fits-open.py` takes 1 to N fits files as arguments, and opens them in DS9.
  Both applying zscale and zooming to fit the frame. If DS9 is not yet open, it
  will start it, but if it is open, it will add the given files as new frames.

- `retrieve-regions.py` lists the regions active in the currently selected DS9
  frame. The original use for this program was to make regions in DS9 and use
  them as slices in a Python program which analyzed the images.
