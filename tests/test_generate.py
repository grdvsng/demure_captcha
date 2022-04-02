import re

from os      import path as os_path
from sys     import path as sys_path
from pathlib import Path

ROOT_DIR = os_path.join(  str( Path( __file__ ).parent.parent ), 'src', 'bin' )

sys_path.append( ROOT_DIR )

from phrase import generate


def test_len( ):
    assert 5 == len( generate( 5 ) )

def test_lowwer( ):
    p = re.compile( '[a-z]' )
    w =  generate( 5, True, False )

    assert ''.join( [ x for x in p.findall( w ) ] ) == w

def test_upper( ):
    p = re.compile( '[A-Z]' )
    w =  generate( 15, False, False )

    assert len( p.findall( w ) ) > 0

def test_numbers( ):
    p = re.compile( '[0-9]' )
    w =  generate( 15, False, True )

    assert len( p.findall( w ) ) > 0