# DISCLAIMER: I could not run this laboratory at all. I have tried this on two different devices
# (notebook and a computer), with different versions of Python (3.6, 3.9 and 3.10), different versions
# of wheel/pypi/pqcrypto packages...

import ctypes, os
import inputs as inp
import pqcrypto


# Only for Linux/MacOS systems. By default, Windows does not come with make
# Even after installing CygWin with make packages, I am not able to run these functions
def tryingCCompile():
    system_output = os.system("cd src && make")

    CFUNC = ctypes.CDLL("src/libCFunctionFile.so")

    CFUNC.SUM.argtypes = [ctypes.c_int, ctypes.c_int]

    python_sum = CFUNC.SUM(inp.SUB_NUM_1_1, inp.SUB_NUM_1_2)
    print(python_sum)


if __name__ == '__main__':
    # tryingCCompile()
    pass
