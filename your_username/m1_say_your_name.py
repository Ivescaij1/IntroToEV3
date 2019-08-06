#!/usr/bin/env python3
"""
This module is meant to be your first program that you've made for EV3.
  Make the robot say your name and then beep.
  Use the samples to learn the API calls needed (not much code to write)

Authors: Dave Fisher and Junfei Cai.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


# ------------------------------------------------------------------
# DONE: 2. Make the robot say "David Fisher can write E V 3 programs"
#   But of course use YOUR NAME.
#
#   Use the samples to figure out the necessary lines of code.
#     Hint: This program can be done in as little as 2 lines of code (1 import, 1 function call)
#   Feel free to run it, change it, and run it again with any message you like.
#   This program is simple, but if you can do this, then you have the tools to do FAR more.
# ------------------------------------------------------------------

import ev3dev.ev3 as ev3
ev3.Sound.speak('I can write E V 3 programs').wait()
