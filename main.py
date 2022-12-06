import svgwrite
import os

def binary(num):
    ret = str(bin(num))[2:].zfill(8)
    return ret

lettere = [
    [" ", "space"],
    ["!", "exclam"],
    ["\"", "quotedbl"],
    ["#", "numbersign"],
    ["$", "dollar"],
    ["%", "percent"],
    ["&", "ampersand"],
    ["'", "quotesingle"],
    ["(", "parenleft"],
    [")", "parenright"],
    ["*", "asterisk"],
    ["+", "plus"],
    [",", "comma"],
    ["-", "hyphenminus"],
    [".", "period"],
    ["/", "slash"],

    ["0", "zero"],
    ["1", "one"],
    ["2", "two"],
    ["3", "three"],
    ["4", "four"],
    ["5", "five"],
    ["6", "six"],
    ["7", "seven"],
    ["8", "eight"],
    ["9", "nine"],

    [":", "colon"],
    [";", "semicolon"],
    ["<", "less"],
    ["=", "equal"],
    [">", "greater"],
    ["?", "question"],
    ["@", "at"],

    ["A", "A"],
    ["B", "B"],
    ["C", "C"],
    ["D", "D"],
    ["E", "E"],
    ["F", "F"],
    ["G", "G"],
    ["H", "H"],
    ["I", "I"],
    ["J", "J"],
    ["K", "K"],
    ["L", "L"],
    ["M", "M"],
    ["N", "N"],
    ["O", "O"],
    ["P", "P"],
    ["Q", "Q"],
    ["R", "R"],
    ["S", "S"],
    ["T", "T"],
    ["U", "U"],
    ["V", "V"],
    ["W", "W"],
    ["X", "X"],
    ["Y", "Y"],
    ["Z", "Z"],

    ["[", "bracketleft"],
    ["\\", "backslash"],
    ["]", "bracketright"],
    ["^", "asciicircum"],
    ["_", "underscore"],
    ["`", "grave"],

    ["a", "a"],
    ["b", "b"],
    ["c", "c"],
    ["d", "d"],
    ["e", "e"],
    ["f", "f"],
    ["g", "g"],
    ["h", "h"],
    ["i", "i"],
    ["j", "j"],
    ["k", "k"],
    ["l", "l"],
    ["m", "m"],
    ["n", "n"],
    ["o", "o"],
    ["p", "p"],
    ["q", "q"],
    ["r", "r"],
    ["s", "s"],
    ["t", "t"],
    ["u", "u"],
    ["v", "v"],
    ["w", "w"],
    ["x", "x"],
    ["y", "y"],
    ["z", "z"],

    ["{", "braceleft"],
    ["|", "bar"],
    ["}", "braceright"],
    ["~", "asciitilde"],
    ["£", "sterling"],
    ["§", "section"],
    ["°", "degree"],

    ["À", "Agrave"],
    ["Á", "Aacute"],
    ["Â", "Acircumflex"],
    ["Ã", "Atilde"],
    ["Ä", "Adieresis"],
    ["Å", "Aring"],
    ["Æ", "AE"],
    ["Ç", "Ccedilla"],
    ["È", "Egrave"],
    ["É", "Eacute"],
    ["Ê", "Ecircumflex"],
    ["Ë", "Edieresis"],
    ["Ì", "Igrave"],
    ["Í", "Iacute"],
    ["Î", "Icircumflex"],
    ["Ï", "Idieresis"],
    ["Ò", "Ograve"],
    ["Ó", "Oacute"],
    ["Ô", "Ocircumflex"],
    ["Õ", "Otilde"],
    ["Ö", "Odieresis"],
    ["Ù", "Ugrave"],
    ["Ú", "Uacute"],
    ["Û", "Ucircumflex"],
    ["Ü", "Udieresis"],

    ["à", "agrave"],
    ["á", "aacute"],
    ["â", "acircumflex"],
    ["ã", "atilde"],
    ["ä", "adieresis"],
    ["å", "aring"],
    ["æ", "ae"],
    ["ç", "ccedilla"],
    ["è", "egrave"],
    ["é", "eacute"],
    ["ê", "ecircumflex"],
    ["ë", "edieresis"],
    ["ì", "igrave"],
    ["í", "iacute"],
    ["î", "icircumflex"],
    ["ï", "idieresis"],
    ["ò", "ograve"],
    ["ó", "oacute"],
    ["ô", "ocircumflex"],
    ["õ", "otilde"],
    ["ö", "odieresis"],
    ["ù", "ugrave"],
    ["ú", "uacute"],
    ["û", "ucircumflex"],
    ["ü", "udieresis"]
]

# Escluso il simbolo dell'euro perché codice di 14 cifre ["€", "euro"]

for lettera in lettere:
    ascii = ord(lettera[0])
    binario = binary(ascii)
    print(f'{lettera[1].ljust(15)} {lettera[0]}\t{"#"+str(ascii)}\t{binario}')
    nomefile = f'{str(ascii).ljust(4)} {lettera[1]} - {binario}.svg'
    
    contatore = 0
    elementiRiga = 3
    contatoreRiga = 0
    sizeRect = 10
    sizeSep = 0

    sizeDwg = elementiRiga * sizeRect + (elementiRiga + 1) * sizeSep
    directory = "generate"
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory, nomefile)
    
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