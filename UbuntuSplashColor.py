#!/usr/bin/python3

'''
Author: UnclassedPenguin

'''
from subprocess import call
import os.path
import sys

path1 = '/usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.grub'
path2 = '/usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.script'
path3 = '/usr/share/gnome-shell/theme/ubuntu.css'

def main():
    colour = get_Colour()
    print("Colour = {}".format(colour[0]))
    print("Colour(RGB) = {}".format(colour[1]))
    print("Colour(RGBP) = {}".format(colour[2]))
    create_Backups()
    parse_Login(colour[0])
    parse_Grub(colour[1])
    parse_Script(colour[2])
    print('\n')
    print('Please reboot to take affect')
    print('\n')

def get_Colour():
    while True:
        colour = input("What colour would you like to change to(in hex #000000)?\n")
        if colour[0] == '#' and len(colour) == 7:
            colourrgb = '{},{},{},0'.format(int(colour[1:3], 16), int(colour[3:5], 16), int(colour[5:], 16))
            colourrgbp = '{}, {}, {}'.format(round(int(colour[1:3], 16)/256, 2), round(int(colour[3:5], 16)/256, 2), round(int(colour[5:], 16)/256, 2))

            return colour, colourrgb, colourrgbp
            break
        else:
            print("invalid colour")

def create_Backups():
    if os.path.isfile(path1+'.old'):
        print('ubuntu-logo.grub.old file exists')
        print('\n')
    else:
        print('ubuntu-logo.grub.old file does not exist...Creating...')
        print('\n')
        call('cp {} {}'.format(path1, path1+'.old'), shell=True)
    if os.path.isfile(path2+'.old'):
        print('ubuntu-logo.script.old file exists')
        print('\n')
    else:
        print('ubuntu-logo.script.old file does not exist...Creating...')
        print('\n')
        call('cp {} {}'.format(path2, path2+'.old'), shell=True)
    if os.path.isfile(path3+'.old'):
        print('ubuntu.css.old file exists')
        print('\n')
    else:
        print('ubntu.css.old file does not exist...Creating...')
        print('\n')
        call('cp {} {}'.format(path3, path3+'.old'), shell=True)

def parse_Login(colour):
    print('Parsing Login File...')
    print('\n')
    file1 = open(path3, 'r')
    filelist = []
    tmplist = []
    tmpvar = ''

    for line in file1:
        filelist.append(line)
        if line[0:16] == '#lockDialogGroup':
            tmpvar = line

    for item in filelist[int(filelist.index(tmpvar)):int(filelist.index(tmpvar))+6]:
        tmplist.append(item)

    for item in tmplist:
        if item[-3:].strip() == '}':
            tmpvar2 = item
            break
    position1 = int(filelist.index(tmpvar))
    position2 = int(filelist.index(tmpvar2))
    for item in range(position2 - position1 + 1):
        del filelist[position1]
    filelist.insert(position1, '  background-repeat: repeat; }\n')
    filelist.insert(position1, '  background: {};\n'.format(colour))
    filelist.insert(position1, '#lockDialogGroup {\n')
    file1.close()
    file2 = open('/tmp/ubuntu.css.working', 'w')
    for item in filelist:
        file2.write(item)
    file2.close()
    call('cp /tmp/ubuntu.css.working {}'.format(path3), shell=True)

def parse_Grub(colourrgb):
    print('Parsing Grub File...')
    print('\n')
    file1 = open(path1, 'r')
    file2 = open('/tmp/ubuntu-logo.grub.working', 'w')
    for line in file1:
        if line[0:2] == 'if':
            file2.write('if background_color {}; then'.format(colourrgb))
            file2.write('\n')
        else:
            file2.write(line)
    file1.close()
    file2.close()
    call('cp /tmp/ubuntu-logo.grub.working {}'.format(path1), shell=True)
    call('update-grub', shell=True)

def parse_Script(colourrgbp):
    print('Parsing Script File...')
    print('\n')
    file1 = open(path2, 'r')
    file2 = open('/tmp/ubuntu-logo.script.working', 'w')
    for line in file1:
        if line[0:28] == 'Window.SetBackgroundTopColor':
            file2.write('Window.SetBackgroundTopColor ({});'.format(colourrgbp))
            file2.write('\n')
        elif line[0:31] == 'Window.SetBackgroundBottomColor':
            file2.write('Window.SetBackgroundBottomColor ({});'.format(colourrgbp))
            file2.write('\n')
        else:
            file2.write(line)
    file1.close()
    file2.close()
    call('cp /tmp/ubuntu-logo.script.working {}'.format(path2), shell=True)
    call('update-initramfs -u', shell=True)

if __name__ == '__main__':
    sys.exit(main())
