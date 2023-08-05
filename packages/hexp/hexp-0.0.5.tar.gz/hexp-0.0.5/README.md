# HexP
Dump contents of input in hexadecimal. Built with Python, Click, and CPython.

## Installation
`pip install hexp`
<br>
or
<br>
```
$ git clone https://github.com/manorajesh/hexp.git
$ pip install -r requirements.txt
$ ./hexp
```

## Usage
```
Usage: hexp [OPTIONS] [FILE]

  Print FILE, or if none given STDIN, in hexadecimal.

Options:
  -c          Display canonical Unicode inline (WIP)
  -C          Display canonical Unicode
  -G          Display hexadecimal as color (WIP)
  --version   Show the version and exit.
  -h, --help  Show this message and exit.
  ```
Run the command with a file as an argument, and it will dump the hexadecimal result to `stdout`. If no arguments are given, `stdin` is used (send `EOF` when done). Currently, only the `-C` works. It will print the `utf-8` translation in the right margin.
<hr>

#### Contents of `requirements.txt`
`click == 8.1.3`
