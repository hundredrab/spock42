# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:19:21 2017

@author: hundred
"""

import re
import os
from mutagen import File

# home = '/home/prophet/Music/IndieAir'  # My Music directory


def EditMeta(home, album=None):
    files = os.listdir(home)
    for filename in files:
        r = re.compile(r'(.+)\s-\s(.+)-.{11}\.m4a')
        k = r.search(filename)
        if(k is None):
            print(filename, '<-------------')
            # filename isn't standard. Won't be altered.
        else:
            art, title = k.groups()
            print(art, ':', title)
            audio = File(home+'/'+filename)
    #        print(audio)
            audio["©nam"] = [title]
            audio["©ART"] = [art]
            if(album is not None):
                audio['©alb'] = [album]
    #        audio["titl"] = [title]
    #        audio["arti"] = [art]
            audio.save()
            print(audio)

EditMeta(home)
