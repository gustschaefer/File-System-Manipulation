# programa para renomear todas as imagens de uma pasta a partir de sua classe.
""" ex: classe bmm => 	bmm0.jpg
			bmm1.jpg 
			bmm2.jpg 
			...
			bmm787.jpg
"""

import os

path = "/file/path"
classe = "class1"
files = os.listdir(path)

for index, file in enumerate(files):
   os.rename(os.path.join(path, file), os.path.join(path, classe+str(index)+".jpg"))
