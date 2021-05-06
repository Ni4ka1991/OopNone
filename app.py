#!/usr/bin/env python3

from os import system


class Container:

    def __init__( self, first = None, second = None ):

### max_min func ###

        def maxi( a, b ):
            paramList = [ a, b ]
            if( a != b ):
                mx = max(paramList)
                mi = min(paramList)
            return [ mi, mx ]

### max_min func ###

## constructor ##

        self.first = first
        self.second = second
        if( first == None ):
            self.second = second
        elif( second == None ):
            self.first = first
        elif( first != None and second != None ):
            self.first, self.second = maxi( first, second )

## constructor ##

## view ##
    def __str__(self):
         if( self.first == None and self.second == None ):
             return f"[ ]"
         elif( self.first == None ):
             return f"[{self.second}]"
         elif( self.second == None ):
             return f"[{self.first}]"
         else:
             return f"[{self.first:3}, {self.second:3}]"
## view ##

## eq ##

    def __eq__( self, other ):
        a = self.first is other.first
        b = self.second is other.second
        if( a == True and b == True ):
            return True            
        else:
            return False

## eq ##



c1 = Container( )
c2 = Container( 150 )
c3 = Container( 150, 140 )

system( "clear" )
print()
print( c1 )
print( c2 )
print( c3 )
is_eq = ( c3 == c2 )
print( is_eq )
