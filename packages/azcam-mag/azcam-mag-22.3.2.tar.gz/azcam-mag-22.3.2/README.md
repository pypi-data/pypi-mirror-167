# azcam-mag

*azcam-mag* is an *azcam* extension for OCIW Magellan CCD controllers (ITL version). See http://instrumentation.obs.carnegiescience.edu/ccd/gcam.html.

## Installation

`pip install azcam-mag`

Or download from github: https://github.com/mplesser/azcam-mag.git.

## Example Code

The code below is for example only.

### Controller

```python
import azcam.server
from azcam_mag.controller_mag import ControllerMag
controller = ControllerMag()
controller.camserver.set_server("some_machine", 2402)
controller.timing_file = os.path.join(azcam.db.datafolder, "dspcode/gcam_ccd57.s")
```
### Exposure

```python
import azcam.server
from azcam_mag.exposure_mag import ExposureMag
exposure = ExposureMag()
filetype = "BIN"
exposure.filetype = exposure.filetypes[filetype]
exposure.image.filetype = exposure.filetypes[filetype]
exposure.display_image = 1
exposure.image.remote_imageserver_flag = 0
exposure.set_filename("/azcam/soguider/image.bin")
exposure.test_image = 0
exposure.root = "image"
exposure.display_image = 0
exposure.image.make_lockfile = 1
```

## Camera Servers

*Camera servers* are separate executable programs which manage direct interaction with controller hardware on some systems. Communication with a camera server takes place over a socket via communication protocols defined between *azcam* and a specific camera server program. These camera servers are necessary when specialized drivers for the camera hardware are required.  They are usually written in C/C++. 

## DSP Code

The DSP code which runs in Magellan controllers is assembled and linked with
Motorola software tools. These tools should be installed in the folder `/azcam/motoroladsptools/` on Windows machines, as required by the batch files which assemble and link the code.

For Magellan systems, there is only one DSP file which is downloaded during initialization. 

Note that *xxx.s* files are loaded for the Magellan systems.
