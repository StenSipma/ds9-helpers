#!/usr/bin/env python3
import os
from sys import argv

from pyds9 import DS9


class DS9Viewer(DS9):
    """
    Wrapper around the DS9 interface, which is the Python interface for
    interactions with DS9 via XPA. This class mainly provides some convenience
    methods to make this interaction a lot easier.
    """

    def __init__(self, tile=True, *args, **kwargs):
        DS9.__init__(self, *args, **kwargs)
        if tile:
            self.set("tile yes")

    def frame_has_image(self, idx=None):
        """
        Test if the frame with idx has an image loaded. If idx is not specified,
        the default is the currently selected frame.
        """
        if idx is not None:
            self.select_frame(idx)
        size = self.get("fits size")
        return size != "0 0"

    def view(self, filename, overwrite=False, scale=True, zoom=True):
        """
        Load the fits file (pointed to by filename) in ds9. Will make a new
        frame by default if there is an image loaded in the currently selected
        frame. (disable this with the overwrite option)

        If scale and/or zoom are set, then zscale and zoom to fit the window
        are respectively applied.
        """
        if not overwrite and self.frame_has_image():
            self.new_frame()

        self.set(f"fits {filename}")

        if scale:
            self.zscale()
        if zoom:
            self.zoom()

    def view_fits(self, hdul, overwrite=False, scale=True, zoom=True):
        """
        Same as the view method, but instead give a HDUList from astropy's
        io.fits module.
        """
        if not overwrite and self.frame_has_image():
            self.new_frame()

        self.set_pyfits(hdul)

        if scale:
            self.zscale()
        if zoom:
            self.zoom()

    def new_frame(self):
        """
        Add a new frame to ds9 (and select it)
        """
        self.set("frame new")

    def select_frame(self, idx):
        """
        Select the frame identified by the given index. If the index does not
        exist, the default ds9 behaviour is to make a new frame with this
        index.

        The index of the initial frame is 1. (so not 0 !!)
        """
        self.set(f"frame frameno {idx}")

    def zscale(self):
        """
        Apply zscale to the current frame.
        """
        self.set("scale zscale")

    def zoom(self):
        """
        Zoom the image int he current frame to fit completely inside it.
        """
        self.set("zoom to fit")


def main():
    if len(argv) < 2:
        print("Usage:")
        print(f" $ fits-open.py [FILE1] [FILE2] ... [FILEN]")
        exit(1)

    d = DS9Viewer()
    filename = argv[1:]

    for file in filename:
        if not os.path.isfile(file):
            print(f"File '{file}' could not be found, ignoring...")
            continue
        d.view(file)


if __name__ == "__main__":
    main()
