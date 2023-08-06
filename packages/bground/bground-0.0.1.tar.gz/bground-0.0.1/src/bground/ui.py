'''
Module bground.ui
The module defines simple user interface for program bground.
The interface can define input, output and plot parameters in PY-scripts.
'''

import numpy as np
import matplotlib
import bground.bdata
import bground.butils

class InputData:
    
    def __init__(self, input_file, **kwargs):
        self.input_file = input_file
        self.data = self.read_input_file(input_file, **kwargs)
    
    @staticmethod
    def read_input_file(input_file, **kwargs):
        if 'unpack' in kwargs.keys(): kwargs.update({'unpack':True})
        data = np.loadtxt(input_file, **kwargs)
        return(data)

class PlotParams:
    
    def __init__(self, xlabel=None, ylabel=None, xlim=None, ylim=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.ylim = ylim

class InteractivePlot:
    
    def __init__(self, DATA, PPAR, OUT_FILE, CLI=False):
        # Basic parameters
        self.data = DATA
        self.ppar = PPAR
        self.out_file = OUT_FILE
        # Additional parameters
        self.background = bground.bdata.bkg(OUT_FILE, 
            bground.bdata.XYpoints([],[]), bground.bdata.XYcurve([],[]))
        # Initialize specific interactive backend
        # (if Python runs in CLI = command line interface, outside Spyder
        if CLI == True:
            matplotlib.use('QtAgg')
        
    def run(self):
        plt = bground.butils.create_plot(
            self.data.data,
            xlabel = self.ppar.xlabel,
            ylabel = self.ppar.ylabel,
            xlim = self.ppar.xlim,
            ylim = self.ppar.ylim)
        plt = bground.butils.define_key_bindings(
            plt, self.data.data, self.background, self.out_file)
        bground.butils.print_ultrabrief_help()
        plt.show()
        