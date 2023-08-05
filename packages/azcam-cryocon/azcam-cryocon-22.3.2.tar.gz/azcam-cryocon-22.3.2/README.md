# azcam-cryocon

*azcam-cryocon* is an *azcam* extension for Cryogenic Control Systems Inc. (cryo-con) temperature controllers. See http://www.cryocon.com/.

## Installation

`pip install azcam-cryocon`

Or download from github: https://github.com/mplesser/azcam-cryocon.git.

## Example Code

The code below is for example only.

### Temperature Controller

```python
import azcam.server
from azcam_cryocon.tempcon_cryocon24 import TempConCryoCon24
tempcon = TempConCryoCon24()
tempcon.description = "cryoconqb"
tempcon.host = "10.0.0.44"
tempcon.control_temperature = -100.0
tempcon.init_commands = [
"input A:units C",
"input B:units C",
"input C:units C",
"input A:isenix 2",
"input B:isenix 2",
"input C:isenix 2",
"loop 1:type pid",
"loop 1:range mid",
"loop 1:maxpwr 100",
]
```
