# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:13:13 2021

@author: _penguinl
"""

links_list = open('all_link_here.txt', 'r').read().split();
names_list = list();

import os;
from pytube import YouTube;

for link in links_list:
#     YouTube(link).streams.first().download();
    yt = YouTube(link);
    tmp = yt.streams.filter(
        progressive=True,
        file_extension='mp4'
        ).order_by('resolution').desc().first().default_filename;
    names_list.append(tmp);
    if(input("'min' or 'max': ") == "max"):
        print('down init (max_q): {0:}'.format(tmp));
        yt.streams.filter(
            progressive=True,
            file_extension='mp4'
            ).order_by('resolution').desc().first().download();
    else:
        print('down init (min_q): {0:}'.format(tmp));
#         yt.streams.filter(
#             file_extension='mp4'
#             ).order_by('resolution').desc().last().download();
        yt.streams.filter(
            progressive=True,
            file_extension='mp4'
            ).order_by('resolution').desc().last().download();
print('down completed: {0:}\n'.format(names_list));
for name in names_list:
    if os.path.exists(name):
      os.remove(name) if (input('delete: {0:} ? '.format(name)) == 'y') else None;
    else:
      print('The file does not exist');