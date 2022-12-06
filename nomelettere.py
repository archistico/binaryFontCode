def binary(num):
    ret = str(bin(num))[2:].zfill(8)
    return ret

text = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜàáâãäåæçèéêëìíîïòóôõöùúûü0123456789/*-+<>,.-;:_°§@#[]\|!"£$%&()='?^~`{} """

lettere = [
    [" ", "space"],
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
    
    ["", ""],
]

# ["", ""],

for lettera in lettere:
    ascii = ord(lettera[0])
    binario = binary(ascii)
    print(lettera[0], "\t", lettera[1], "\t", ascii, "\t", binario)