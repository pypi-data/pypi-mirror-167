'''
Module bground.butils
The module defines various functions for calculation of user background:
1) Functions that create the interactive plot (basic plot, key bindings...)
2) Various auxiliary functions (sorting backround points acc.to X-coordinate)
3) Final functions calculating background (bkg curve and bkg-corrected data)
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from bground import iplot

def initialize_plot_parameters():
    '''
    Initialize parameters for plotting.
    '''
    plt.rcParams.update({
        'figure.figsize' : (6,4),
        'figure.dpi' : 100,
        'font.size' : 12})

def print_ultrabrief_help():
    '''
    Print ultra-brief help in console window before activating the plot.
    '''
    print('Activate interactive plot window and press:')
    print('0 = to print brief help in console window')
    print('1 = to draw background point at current mouse position')
    print('2 = to delete background point...')
    print('---')

def create_plot(data, xlabel, ylabel='Intensity', xlim=[0,300], ylim=[0,300]):
    '''
    Create plot from input data.
    This is the plot window, which will be made interactive.
    In the rest of the program, the plot will be the program interface.

    Parameters
    ----------
    data : 2D numpy array
        Data for plotting; columns [X,Y].
    xlim : list or tuple (containing two values)
        Lower and upper limit of X in the plot; the default is [0,300].
    xlim : list or tuple (containing two values)
        Lower and upper limit of Y in the plot; the default is [0,300].
    
    Returns
    -------
    plt : maptplotlib.pyplot object
        The line plot showing XY data.
    '''
    initialize_plot_parameters()
    X,Y = (data[0],data[1])
    plt.gcf().canvas.set_window_title('Background definition')
    plt.plot(X,Y,'b-')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    return(plt)

def define_key_bindings(plt, data, bkgr, outfile):
    '''
    Define key bindings for plot = define callback function,
    which links selected [key_press_events] with further functions.
    
    Parameters
    ----------
    plt : matplotlib.pyplot object
        Prepared interactive XY-plot,
        for which we want to define new [key_press_events].
    data : 2D numpy array
        XY-data (which are shown in plt),
        which must be sent to functions after some [key_press_events].
    bkgr : bdata.bkg object
        Empty background object,
        which must be sent to functions after some [key_press_events].
    outfile : string
        Name of the output file,
        which must be sent to functions after some [key_press_events].
    
    Returns
    -------
    plt : maptplotlib.pyplot object
        The line plot showing XY data with defined key-bindings.
    '''
    # Key function of bground package:
    # = definition of keyboard shortcuts for background definition
    # * based on standard matplotlib function canvas.mpl_connect
    # * this module (butils) just binds the matplotlib/key_press_event
    #   to our/user-defined function defined in a sister module (iplot) 
    # ! trick: we need an event with multiple arguments => lambda function
    plt.gcf().canvas.mpl_connect('key_press_event',
        lambda event: iplot.on_keypress(event, plt, data, bkgr, outfile))
    # return plt object, in which key bindings were defined
    return(plt)

def sort_bkg_points(bkg):
    '''
    Sort background points according to their X-coordinate.
    The background points are inserted as the whole bkg object.
    
    Parameters
    ----------
    bkg : bground.bdata.bkg object
        A bkg object containing unsorted list of background points.

    Returns
    -------
    None; the output is bkg object with sorted background points.
    '''
    # Sorting is based on the trick found on www
    # GoogleSearch: python sort two 1D arrays
    # https://stackoverflow.com/q/9007877
    X,Y = (bkg.points.X, bkg.points.Y)
    x,y = zip( *sorted( zip(X,Y) ) )
    bkg.points.X = list(x)
    bkg.points.Y = list(y)
    
def calculate_background(data,bkg):
    '''
    Calculate background
    = calculate interpolated background curve;
    the calculated background curve is saved within bkg object.
    
    Parameters
    ----------
    bkg : bground.bdata.bkg object
        Object containing the following items:
            * basename = string, basename of output file(s)
            * points = 3-column list: [PointType, X-coord, Y-coord]
            * itype = type of interpolation for the calculation of bkground
    
    Returns
    -------
    None; the result is the updated bkg object.
        * bkg.X = calculated X-coordinates of the WHOLE background
        * bkg.Y = calculated Y-coordinates of the WHOLE background
    '''
    # (1) Prepare background points = X,Y coordinates for interpolation
    X,Y = (bkg.points.X,bkg.points.Y)
    # (2) Interpolate background points = calculcate background curve
    try:
        # Interpolation = calculation of interpolation function F.
        # (F = interpolation object/function
        # (with which we easily calculate the interpolated data - see below
        F = interpolate.interp1d(X,Y, kind=bkg.itype)
        Xmin = bkg.points.X[0]
        Xmax = bkg.points.X[-1]
        Xnew = data[0,(Xmin<=data[0])&(data[0]<=Xmax)]
        Ynew = F(Xnew)
        bkg.curve.X = Xnew
        bkg.curve.Y = Ynew
    except Exception as err:
        # Exceptions: interpolation can fail for whatever reason
        # In such a case we print error and return an empty array
        print(err)
        print(type(err))
        return(np.array([]))

def subtract_background(data, bkg):
    '''
    Subtract background
    = subtract interpolated background curve from original data;
    the data with subtracted bkgr are added as new column to data variable.  
    
    Parameters
    ----------
    data : 2D numpy array
        The array contains two colums [X,Intensity].
    bkg : bdata.bkg object
        The object contains several items,
        namely interpolated background curve.

    Returns
    -------
    data : 2D numpy array
        The array with 3 columns [X,Intensity,BackgroundCorrectedIntensity].
    '''
    # (1) Add one more column to data variable.
    data = np.insert(data,2,data[1],0)
    # (2) Get Xmin and Xmax of background curve.
    Xmin = bkg.curve.X[0]
    Xmax = bkg.curve.X[-1]
    # (3) Define range in which the backgrou5nd is subtracted.
    bkg_range = (Xmin<=data[0]) & (data[0]<=Xmax)
    # (4) Zero intensities below Xmin & above Xmax.
    data[2] = np.where(bkg_range,data[1],0)
    # (5) Subtract background from intensities between Xmin and Xmax
    data[2,bkg_range] = data[2,bkg_range] - bkg.curve.Y
    # (6) Set possible negative intensities after bkgr subtraction to zero
    data[2,data[2]<0] = 0
    # (7) Return modified data array
    # (the last column the array contains background-corrected intensities
    return(data)
