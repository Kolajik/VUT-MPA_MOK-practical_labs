CC      = gcc
CFLAGS  = -std=c99 -pedantic -Wall -Wextra -g -fPIC
NAME 	= libCFunctionFile

$(NAME).so: C_function_file.c
	$(CC) -shared $^ -o $@

.PHONY: clean
clean:
	rm -rf *.o *.so