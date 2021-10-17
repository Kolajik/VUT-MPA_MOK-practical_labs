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
