# azcam-ascom

*azcam-ascom* is an *azcam* extension for ASCOM cameras. See https://ascom-standards.org/.

This code has been used for the QHY and ZWO cameras.

## Installation

`pip install azcam-ascom`

Or download from github: https://github.com/mplesser/azcam-ascom.git.

## Example Code

The code below is for example only.

### Controller

```python
import azcam.server
from azcam_ascom.controller_ascom import ControllerASCOM
controller = ControllerASCOM()
```

### Exposure

```python
import azcam.server
from azcam_ascom.exposure_ascom import ExposureASCOM
exposure = ExposureASCOM()
filetype = "FITS"
exposure.filetype = exposure.filetypes[filetype]
exposure.image.filetype = exposure.filetypes[filetype]
exposure.display_image = 1
exposure.image.remote_imageserver_flag = 0
exposure.set_filename("/data/zwo/asi1294/image.fits")
exposure.display_image = 1
```
