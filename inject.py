#!/usr/bin/env python3

def inject(**inject_dict):
    def call(func):
        def wrapper(*args, **kwargs):
            not_existing_keys = \
                [k for k in inject_dict.keys() if k not in func.__globals__]
            func.__globals__.update(inject_dict)
        
            ret = func(*args, **kwargs)
            
            for k in not_existing_keys:
                del func.__globals__[k]
            return ret
        return wrapper
    return call
