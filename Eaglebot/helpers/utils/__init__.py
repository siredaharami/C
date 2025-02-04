from .extdl import *
from .paste import *

type = True
check = 0

while type:
    try:
        from . import format as _format
        from . import tools as _eagletools
        from . import utils as _eagleutils
        from .events import *
        from .format import *
        from .tools import *
        from .utils import *

        break
    except ModuleNotFoundError as e:
        def install_pip(package_name):
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

        install_pip(e.name)
        check += 1
        if check > 5:
            print("Module installation failed after multiple attempts.")
            break
