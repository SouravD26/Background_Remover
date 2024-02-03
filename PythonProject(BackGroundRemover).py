#-------------------------------------------------------------------------------
# Name:       Sourav Dutta
# Purpose:
#
# Author:      DELL PC
#
# Created:     02-12-2023
# Copyright:   (c) DELL PC 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------
# pip installed
# import remove & esaygui & Image
from rembg import remove
import easygui
from PIL import Image


input_path = easygui.fileopenbox(title='select image file')
output_path = easygui.filesavebox(title='save file to ...')

input = Image.open(input_path)
output = remove(input)
output.save(output_path)