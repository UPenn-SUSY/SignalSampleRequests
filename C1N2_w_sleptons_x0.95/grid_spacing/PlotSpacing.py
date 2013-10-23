#!/usr/bin/env python

import sys
import os.path
import optparse
import time
import array

import ROOT
import rootlogon
import metaroot

# ------------------------------------------------------------------------------
def readFile(in_file_name):
    input = []
    f = file(in_file_name, 'r')
    for l in f.readlines():
        pieces = l.split()
        if len(pieces) == 0: continue
        if pieces[0] == '#': continue
        print l.split()

        # dsid = pieces[0]
        mc1 = float(pieces[0])
        mn0 = float(pieces[1])

        input.append( { 'mc1':mc1
                      , 'mn0':mn0
                      }
                    )
    return input

# ------------------------------------------------------------------------------
def makeGraph(spacing):
    x_vals = []
    y_vals = []
    for s in spacing:
        x_vals.append(s['mc1'])
        y_vals.append(s['mn0'])

    spacing = ROOT.TGraph( len(x_vals)
                         , array.array('d', x_vals)
                         , array.array('d', y_vals)
                         )
    spacing.SetMarkerStyle(20)
    spacing.Draw('A')
    spacing.GetXaxis().SetTitle('m(#chi_{2}^{0}#chi_{1}^{#pm})')
    spacing.GetYaxis().SetTitle('m(#chi_{1}^{0})')
    return spacing

if __name__ == '__main__':
    spacing = readFile('grid_spacing.txt')
    graph = makeGraph(spacing)

    c = ROOT.TCanvas()
    graph.Draw('AP')
    c.Print('grid_spacing.pdf')
