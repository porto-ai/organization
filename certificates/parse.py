#!/usr/bin/python2.7
# -*- coding: iso-8859-15 -*-

import string, os

import argparse

def process(type_certificate):

    filename = type_certificate + '.csv'
    filenametex = type_certificate+'_certificate'

    insstud = open( filename, "r" )
    linesstud = insstud.readlines();
    insstud.close()


    ins = open( filenametex + '.tex', "r" )
    lines = ins.readlines()
    ins.close()

    linesOriginal = []
    linesOriginal.extend(lines) # copy list, not pointer

    counter = 1
    for std in linesstud:
        lines[25] = lines[25].replace("PUTHERE", std)
        
        # generate certificate
        ins = open( filenametex + '_changed.tex', "w" )
        ins.writelines(lines)
        ins.close()

        os.system('make clean; make ' + type_certificate + '; make clean')
        os.system('mv -v tmp_certificates/'+type_certificate+'_certificate_changed.pdf certificates/' + type_certificate +'_'+str(counter)+'.pdf')
        os.system('rm -v ' + filenametex + '_changed.tex')
        
        counter = counter + 1
        lines = []
        lines.extend(linesOriginal)

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--type', help='type of certificate (students, professor)')

    args = parser.parse_args()
    process(args.type)
