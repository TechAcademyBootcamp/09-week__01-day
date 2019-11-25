
import math

################################################################################
## Class Quad
################################################################################

class Quad( object ):
    
    def __init__( self, AB=None, DA=None, A=None ):
        """
        Initialize an object of type Quad.
        """
        
        self.__sideAB = AB
        self.__sideDA = DA
        self.__angleA = A
        self.__valid = False

        pass # REPLACE

    def __validate( self ):
        #
        # Determine if a Quad is valid.
        #

        pass # REPLACE
    
    def __repr__( self ):
        """
        Return a string (the representation of a Quad).
        """

        pass # REPLACE

    def __str__( self ):
        """
        Return a string (the representation of a Quad).
        """

        pass # REPLACE

    def is_valid( self ):
        """
        Return a Boolean (is the Quad valid?).
        """
        
        pass # REPLACE

    def is_rectangle( self ):
        """
        Return a Boolean (is the Quad a rectangle?)
        """
        
        pass # REPLACE

    def is_rhombus( self ):
        """
        Return a Boolean (is the Quad a rhombus?)
        """
    
        pass # REPLACE

    def is_square( self ):
        """
        Return a Boolean (is the Quad a square)?
        """
        
        pass # REPLACE

    def sides( self ):
        """
        Return a tuple containing the Quad's four sides.
        """
    
        pass # REPLACE
    
    def angles( self ):
        """
        Return a tuple containing the Quad's four angles (in degrees) 
        """

        pass # REPLACE

    def perimeter( self ):
        """
        Return a float representing the Quad's perimeter.
        """

        pass # REPLACE
    
    def area( self ):
        """
        Return a float representing the Quad's area.
        """

        pass # REPLACE

    def scale( self, factor=1.0 ):
        """
        Scale all four of a Quad's sides by the same factor.
        """

        pass # REPLACE
