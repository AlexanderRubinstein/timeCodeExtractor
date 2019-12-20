#!/bin/bash

ffmpeg -i "D:\\ProjectsJupiter\\Introduction to Computer Vision\\Timecode_Extraction\\Generalized nonparametric method. An appendix to stock market analysis.mp4" -vf "select=not(mod(n\,250))" -vsync vfr "D:\\ProjectsJupiter\\Introduction to Computer Vision\\Timecode_Extraction\\Frames\\frame_%d.jpg"