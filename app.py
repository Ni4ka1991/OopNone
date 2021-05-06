#!/usr/bin/env python3

from os import system


class Container:

    def __init__( self, first = None, second = None ):
        
        def maxi( a, b ):
            paramList = [ a, b ]
            if( a != b ):
                mx = max(paramList)
                mi = min(paramList)
            return [ mi, mx ]
        
        if( first != None and second != None ):
            self.first, self.second = maxi( first, second)
        else:
            self.first = first
            self.second = second

    def __str__(self):
        if( self.second == None ):
            return f"[{self.first}]"
        elif( self.first == None and self.second == None ):
            return None
        else:
            return f"[{self.first}, {self.second}]"


c1 = Container( )
c2 = Container( 30 )
c3 = Container( 150, 10 )

system( "clear" )
print()
print( c1 )
print( c2 )
print( c3 )

