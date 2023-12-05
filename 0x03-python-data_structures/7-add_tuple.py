#!/usr/bin/python3
def add_tuple(tuple1=(), tuple2=()):
    new_tuple = ()
    tuple_1 = tuple1 + (0, 0)
    tuple_2 = tuple2 + (0, 0)
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
