'''
Module bground.bdata
The module defines three simple clasess.
The classes keep data for definition of background.
'''

class XYpoints:
    '''
    XYpoints = object containing two lists X,Y.
    XYpoints object = background points = employed in object bkg below.
    '''
    
    def __init__(self, X=[], Y=[]):
        '''
        Initialize XYpoints = object containing two lists X,Y.
        X,Y = list of X,Y-coordinates of the user-defined background points.
        '''
        self.X = X
        self.Y = Y
        
    def add_point(self,Xcoord,Ycoord):
        '''
        Add one background point to the list (object XYlist = bkgr points).
        '''
        self.X.append(Xcoord)
        self.Y.append(Ycoord)

class XYcurve:
    '''
    XYcurve = object containing two 1D numpy arrays X,Y.
    XYcurve object = background curve = employed in object bkg below. 
    '''
    
    def __init__(self, X=[], Y=[]):
        '''
        Initialize XYpoints = object containing two 1D numpy arrays X,Y.
        X,Y = list of X,Y-coordinates of the user-defined background points.
        '''
        self.X = X
        self.Y = Y

class bkg:
    '''
    User-defined background.
    '''
    
    def __init__(self, basename, 
                 points = XYpoints([],[]), 
                 curve = XYcurve([],[]),
                 itype = 'linear'):
        '''
        Initialize background.

        Parameters
        ----------
        basename : str
            Basename of output file = filename without extension.
            The extension will be added automatically according to context.
        points : bdata.XYpoints object
            Coordinates of user-defined backround points.
        curve  : bdata.XYcurve object
            Backround curve = X,Y of all points of the calculated background.
        itype : string; default is 'linear' 
            Interpolation type = interpolation during backround calculation.
            Implemented interpolation types: 'linear', 'quadratic', 'cubic'.
            
        Returns
        -------
        None; the result is the initialized object: bdata.bkg.
        
        Technical notes
        ---------------
        * In function definition, we use XYpoints([],[]) and XYcurve([],[]).
        * The empty arrays should eliminate possible non-zero values
          from possible previous run in Spyder.
        * Nevertheless, in current version this is not sufficient
          and the background in the main program must be initialized
          with empty objects XYpoints and XYcurve as well.
        * At the moment, I regard this as a Python mystery.
        '''
        self.basename = basename
        self.points   = points
        self.curve    = curve 
        self.itype    = itype
