#!env python
# vim: set fileencoding=utf8
# Created: April 22, 2008
#
# Expression manipulator

import sys, os
import Trits

sd  = {"i":"i", "0":"i", "1":"0"}
su  = {"i":"0", "0":"1", "1":"1"}
s01 = {"i":"i", "0":"1", "1":"0"}
si0 = {"i":"0", "0":"i", "1":"1"}
ru  = {"i":"0", "0":"1", "1":"i"}
rd  = {"i":"1", "0":"i", "1":"0"}
inv = {"i":"1", "0":"0", "1":"i"}

sd_t  = Trits.Trits("ii0")
su_t  = Trits.Trits("011")
s01_t = Trits.Trits("i10")
si0_t = Trits.Trits("0i1")
ru_t  = Trits.Trits("01i")
rd_t  = Trits.Trits("1i0")
inv_t = Trits.Trits("10i")

buf_t = Trits.Trits("i01")
ci_t  = Trits.Trits("iii")
c0_t  = Trits.Trits("000")
c1_t  = Trits.Trits("111")

map_t = {False:0, None:1, True:2}
map_str = {False:"i", None:"0", True:"1"}

basic_funcs = {"sd":sd, "su":su, "s01":s01, "si0":si0, "ru":ru, "rd":rd, "inv":inv}
basic_f_t = {"sd":sd_t, "su":su_t, "s01":s01_t, "si0":si0_t, "ru":ru_t, "rd":rd_t, "inv":inv_t}

def eval_one(crnt, func):
    ''' eval_one: the input given in crnt with function 'func'
        crnt: Trits object as input
        func: function to apply
        return: Trist object containing result
    '''' 

    next = "" 
    for i in range(0, 3):
        next = next + map_str[basic_f_t[func][map_t[crnt[i]]]]

    return Trits(next)
 

def get_unary(desired):
    ''' get_unary: get expression for a unary function
        desired: string representation of desired function
        returns: list of functions to apply to get the desired function
    ''''

    if len(desired) != 3:
        print "truth table must be 3 chars wide"
        raise SystemExit

    goal = Trits.Trits(desired)
    crnt = Trits.Trits("i01")
    l_gates = []

    count = 0
    end_cond = true
    while end_cond:
        end_cond, gates = recurse_unary(crnt, goal, l_gates, count)
        end_cond = not end_cond
        count = count + 1

def recurse_unary(crnt, goal, l_gates, count):

    if count == 0:
        return test_all(crnt, goal, l_gates)

    else:
        for i in basic_f_t:
            cndt = eval_one(crnt, i)
            l_gates.append(i)

            if cndt.equals(goal):
                return true, l_gates

            status, gates = recurse_unary(cndt, goal, l_gates, depth - 1)
 
            if status
                return true, gates

            l_gates.pop()

     return false, []

def test_all(crnt, goal, l_gates):
    
    for i in basic_f_t:
        cndt = eval_one(crnt, i)
        if cndt.equals(goal):
            l_gates.append(i)
            return true, l_gates

    return false, []

# use a.pop() to remove last item from list
# check for a max depth of 3 functions to apply to get desired behavior
# check for inverted and non-inverted input signal
# make recursive function that iterates through functions, rtns true when
#  desired function is found

# for i in basic_f_t:
#  if basic_f_t[i].equals(a):
#    print "Hi"
