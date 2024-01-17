#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import random
import matplotlib.pyplot as plt
import math

###########################################################
###########################################################
###########################################################
def per2physloc( x , style = "power") :
    if style == "power" :
        return - math.log(1 - x) / 7  # this support 3 9's
    else :
        return (2**(-6*(1-x)))


def per2physloc_2( x ) :
    # this will be the transform until we find a better one
    return -0.5 * math.log(1 - x + 0.01  ,   10)
    # return -1 * math.log(1 - x + 0.01  ,   10)

###########################################################
###########################################################
###########################################################

def gen_xlabels(intresting_xticks) : 
    # assume to be list of number in the range [0-1] that will be converted to labels in percents %
    return  [ "%7.2f %s" % ((x*100), "%")   for x in intresting_xticks ]

###########################################################
###########################################################
###########################################################

def scale_order( sample_data ) :

    # the x values [0..len(sample_data)] are also normalized to the range [0-1]
    # the y values, sample_data are left as is
    ordered_sample = sorted(sample_data, key = float)
    # assume to be ordered list of floats or integers
    list_len   = len(ordered_sample) + 1
    out_x_list = []
    out_y_list = ordered_sample
    for i,x in enumerate(ordered_sample) :
        out_x_list.append((i+1)/list_len)

    return (out_x_list, out_y_list)

###########################################################
###########################################################
###########################################################


def get_float_list(start, stop, size):
    result = []
    unique_set = set()
    for i in range(size):
        x = round(random.uniform(start, stop),2)
        while x in unique_set:
            x = round(random.uniform(start, stop),2)
        unique_set.add(x)
        result.append(x)

    return result




###########################################################
###########################################################
###########################################################
# input_dict = {}
def do_percentile(input_dict) :
    # print("here")
    phys_x_labels     = gen_xlabels(input_dict["x_ticks"])
    phys_x_ticks      = [per2physloc(x)  for x in input_dict["x_ticks"] ]


    plt.xlabel(input_dict["x_axis_label"])
    plt.ylabel(input_dict["y_axis_label"])
    plt.title( input_dict["fig_title"])
    plt.xticks(phys_x_ticks, phys_x_labels)
    plt.xticks(rotation=45)
        
    for temp_sample in input_dict["samples"] :
        
        (x_list, y_list)  = scale_order( temp_sample["data"] )
        trans_x_list = [per2physloc(x)  for x in x_list ]
        # print("trans_x_list " + str(trans_x_list))
        # print("y_list " + str(y_list))
        plt.scatter(trans_x_list, y_list, label = temp_sample["legend"])

        
    plt.xlim([0, 1])
    if input_dict["ylim"] != None :
        plt.ylim(input_dict["ylim"])
    else :
        plt.ylim([0, 10000])
        
    plt.legend()
    plt.grid()



###########################################################
###########################################################
###########################################################

# # should come from external json file
# input_dict = {
#     "fig_title"    : "this is figure title",
#     "x_axis_label" : "tail focused percentile",
#     "y_axis_label" : "latency in ms",
#     "ylim"         : [0,100], 
#     "x_ticks"      : [0.0, 0.5, 0.75, 0.9, 0.99, 0.999],

#     "samples" : [
#     {
#     "legend" : "sample 1 hyperspace",
#     "data"   : get_float_list(10, 40, 200)
#     },
#     {
#     "legend" : "sample 2 hyperspace",
#     "data"   : get_float_list(30, 100, 300)
#     }
#     ]
# }

# ###########################################################
# ###########################################################
# ###########################################################


# do_percentile(input_dict)

# plt.show()


# exit()

###########################################################
###########################################################
###########################################################
