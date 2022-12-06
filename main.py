import svgwrite
import os

def binary(num):
    ret = str(bin(num))[2:].zfill(8)
    return ret

text = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜàáâãäåæçèéêëìíîïòóôõöùúûü0123456789/*-+<>,.-;:_°§@#[]\|!"£$%&()='?^~`{} """
# altro = """€"""

textlength = len(text)
for char in text:
    ascii = ord(char)
    binario = binary(ascii)
    print(char, "\t", ascii, "\t", binario)
    
    contatore = 0
    elementiRiga = 3
    contatoreRiga = 0
    sizeRect = 10
    sizeSep = 0

    sizeDwg = elementiRiga * sizeRect + (elementiRiga + 1) * sizeSep
    directory = "generate"
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory, str(ascii)+'.svg')
    
    dwg = svgwrite.Drawing(path, size=(str(sizeDwg)+'px', str(sizeDwg)+'px'), profile='tiny')
    dwg.add(dwg.rect((0,0),(sizeDwg,sizeDwg), fill=svgwrite.rgb(255, 255, 255, '%')))
    for cb in binario:
        if contatore > elementiRiga-1:
            contatoreRiga += 1
            contatore = 0
        if cb == '0':
            pass
            #dwg.add(dwg.rect((sizeSep + contatore*sizeRect + contatore*sizeSep, sizeSep + contatoreRiga*sizeRect + contatoreRiga*sizeSep),(sizeRect,sizeRect), fill=svgwrite.rgb(255, 255, 255, '%')))
        elif cb == '1':
            #pass
            dwg.add(dwg.rect((sizeSep + contatore*sizeRect + contatore*sizeSep, sizeSep + contatoreRiga*sizeRect + contatoreRiga*sizeSep),(sizeRect,sizeRect), fill=svgwrite.rgb(0, 0, 0, '%')))
        contatore += 1
    dwg.save()