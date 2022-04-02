import unittest

from os      import path as os_path
from sys     import path as sys_path
from pathlib import Path
from PIL     import Image

ROOT_DIR = os_path.join(  str( Path( __file__ ).parent.parent ), 'src', 'bin' )

sys_path.append( ROOT_DIR )

from captcha import generate, Captcha


class TestStringMethods( unittest.TestCase ):
    def test_generate( self ):
        captcha = generate( )

        self.assertIsInstance( captcha, Captcha )

    def test_words( self ):
        word    = 'ascvfrwef243fr2'
        captcha = generate( word=word )

        self.assertEqual( captcha.words, word )

    def test_image( self ):
        captcha = generate( )

        self.assertIsInstance( captcha.image, Image.Image )