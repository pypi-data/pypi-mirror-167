# azcam-ds9

## Purpose

*azcam-ds9* is an *azcam extension* which supports SAO's ds9 display tool running under Windows. See https://sites.google.com/cfa.harvard.edu/saoimageds9.

See https://github.com/mplesser/azcam-ds9-winsupport for support code which may be helpful when displaying images on Windows computers

## Display Class
This class defines Azcam's image display interface to SAO's ds9 image display. 
It is usually instantiated as the *display* object for both server and clients.

Depending on system configuration, the *display* object may be available 
directly from the command line, e.g. `display.display("test.fits")`.

Usage Example:

```python
from azcam_ds9.ds9display import Ds9Display
display = Ds9Display()
display.display("test.fits")
rois = display.get_rois(0, "detector")
print(rois)
```

## Installation

`pip install azcam-ds9`

Or download from github: https://github.com/mplesser/azcam-ds9.git.

## Code Documentation

https://mplesser.github.io/azcam-ds9

## Notes

It may be helpful to remove all associations of .fits files in the registry and then only
execute the above batch files.  Do not directly associate .fits files with ds9.exe.