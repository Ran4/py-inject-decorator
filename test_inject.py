#!/usr/bin/env python3
from inject import inject

@inject(name="World")
def helloer():
    assert name == "World"
    print("Hello {}".format(name))
    
if __name__ == "__main__":
    helloer()
