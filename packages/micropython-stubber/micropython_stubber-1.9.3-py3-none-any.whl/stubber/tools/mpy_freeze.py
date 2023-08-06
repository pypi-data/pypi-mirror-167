from pathlib import Path

import manifestfile

"""

python3 ../../tools/makemanifest.py -o build-standard/frozen_content.c -v "MPY_DIR=../.." -v "MPY_LIB_DIR=../../lib/micropython-lib" -v "PORT_DIR=/home/jos/micropython/ports/unix" -v "BOARD_DIR=" -b "build-standard"  --mpy-tool-flags="" variants/standard/manifest.py

            "args": [
                "-o",
                "build-standard/frozen_content.c",
                "-v",
                "MPY_DIR=../..",
                "-v",
                "MPY_LIB_DIR=../../lib/micropython-lib",
                "-v",
                "PORT_DIR=/home/jos/micropython/ports/unix",
                "-v",
                "BOARD_DIR=",
                "-b",
                "build-standard",
                "--mpy-tool-flags=",
                "variants/standard/manifest.py"
            ]

"""


VARS = {}
VARS["MPY_DIR"] = "./repos/micropython"
VARS["MPY_LIB_DIR"] = "./repos/micropython-lib"  # ? if <= 1.19.1
VARS["PORT_DIR"] = "./repos/micropython/ports/unix"
VARS["BOARD_DIR"] = ""
manifest_file = "C:\\develop\\MyPython\\micropython-stubber\\repos\\micropython\\ports\\unix\\variants\\standard\\manifest.py"
manifest_file = "variants/standard/manifest.py"


manifest = manifestfile.ManifestFile(manifestfile.MODE_FREEZE, VARS)

for input_manifest in [Path(manifest_file)]:
    try:
        manifest.execute(input_manifest.as_posix())
    except manifestfile.ManifestFileError as er:
        print('freeze error executing "{}": {}'.format(input_manifest, er.args[0]))


print(manifest.files())
