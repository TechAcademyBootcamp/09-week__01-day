
import math

################################################################################
## Class Triangle
################################################################################

class Triangle( object ):
    
    def __init__( self, sideA=0.0, sideB=0.0, sideC=0.0 ):
        """
        Initialize an object of type Triangle.
        """
        
        self.__sideA = 0.0
        self.__sideB = 0.0
        self.__sideC = 0.0
        self.__valid = False

        pass # REPLACE

    def __validate( self ):
        #
        # Check the three sides to determine if a Triangle is valid.
        #

        pass # REPLACE
    
    def __repr__( self ):
        """
        Return a string (the representation of a Triangle).
        """

        pass # REPLACE

    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """

        pass # REPLACE

    def is_valid( self ):
        """
        Return a Boolean (is the Triangle valid?).
        """
        
        pass # REPLACE

    def is_equilateral( self ):
        """
        Return a Boolean (is the Triangle an equilateral triangle?)
        """
        
        pass # REPLACE

    def is_isosceles( self ):
        """
        Return a Boolean (is the Triangle an isosceles triangle?)
        """
    
        pass # REPLACE

    def is_scalene( self ):
        """
        Return a Boolean (is the Triangle a scalene triangle?)
        """
        
        pass # REPLACE

    def sides( self ):
        """
        Return a tuple containing the Triangle's three sides.
        """
    
        pass # REPLACE
    
    def angles( self ):
        """
        Return a tuple containing the Triangle's three angles (in degrees) 
        """

        pass # REPLACE

    def perimeter( self ):
        """
        Return a float representing the Triangle's perimeter.
        """

        pass # REPLACE
    
    def area( self ):
        """
        Return a float representing the Triangle's area.
        """

        pass # REPLACE

    def scale( self, factor=1.0 ):
        """
        Scale all three of a Triangle's sides by the same factor.
        """

        pass # REPLACE
