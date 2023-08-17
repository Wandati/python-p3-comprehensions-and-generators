#!/usr/bin/env python3

def return_evens(num_list):
    # new_no = []
    # for n in num_list:
    #     if n % 2 == 0:
    #         new_no.append(n)
    # print(new_no)
    return[n for n in num_list if n % 2 == 0 ]


def make_exclamation(sentence_list):
    return [n + "!" for n in sentence_list]


