# lib imports
from manim import *
from MF_Tools import *

# project imports
from animationParts.partOne import *
from animationParts.partTwo import *
from animationParts.partThree import *
from animationParts.partFour import *


class Animation(Scene):
    def construct(self):
        self.camera.background_color = "#111111"
        # Block 1
        
        # part 1
        #begining_of_part_one(self)
        part_one(self)
        
        # part 2        
        # begining_of_part_two(self)
        # part_two_main(self)
        
        # part 3
        # begining_of_part_three(self)
        # part_three_main(self)

        # part 4
        # begining_of_part_four(self)
        #part_four_main(self)
        
        
        # Block 2