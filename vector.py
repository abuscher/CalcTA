# -------------------------------------------------------------------------------
# Name:        Vector
# Purpose:
#
# Author:      Austin
#
# Created:     16/06/2013
# Copyright:   (c) Austin 2013
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import math
import random
import fractions


def dot(a, b):
    dot = 0
    for i in range(len(a)):
        dot += a[i] * b[i]
    return dot


def norm(a):
    mag = 0
    for i in range(len(a)):
        mag += a[i] ** 2
    return math.sqrt(mag)


class vector(object):
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self, length):
        bank = {}
        if length == 2:
            bank[0] = [1, 4]
            bank[1] = [3, 8]
            bank[2] = [1, 1]
            bank[3] = [2, 3]
            bank[4] = [7, 1]
            bank[5] = [2, 5]
            bank[6] = [3, 4]
            bank[7] = [1, 6]
            bank[8] = [1, 3]

        if length == 3:
            bank[0] = [1, 1, 1]
            bank[1] = [1, 1, 2]
            bank[2] = [1, 1, 3]
            bank[3] = [1, 1, 4]
            bank[4] = [1, 1, 6]
            bank[5] = [1, 2, 1]
            bank[6] = [1, 2, 2]
            bank[7] = [1, 2, 3]
            bank[8] = [1, 2, 4]
            bank[9] = [1, 2, 6]
            bank[10] = [1, 3, 1]
            bank[11] = [1, 3, 2]
            bank[12] = [1, 3, 3]
            bank[13] = [1, 4, 1]
            bank[14] = [1, 4, 2]
            bank[15] = [1, 4, 5]
            bank[16] = [1, 4, 7]
            bank[17] = [1, 5, 4]
            bank[18] = [1, 6, 1]
            bank[19] = [1, 6, 2]
            bank[20] = [1, 6, 6]
            bank[21] = [1, 7, 4]
            bank[22] = [2, 1, 1]
            bank[23] = [2, 1, 2]
            bank[24] = [2, 1, 3]
            bank[25] = [2, 1, 4]
            bank[26] = [2, 1, 6]
            bank[27] = [2, 2, 1]
            bank[28] = [2, 2, 3]
            bank[29] = [2, 3, 1]
            bank[30] = [2, 3, 2]
            bank[31] = [2, 3, 3]
            bank[32] = [2, 3, 4]
            bank[33] = [2, 4, 1]
            bank[34] = [2, 4, 3]
            bank[35] = [2, 6, 1]
            bank[36] = [3, 1, 1]
            bank[37] = [3, 1, 2]
            bank[38] = [3, 1, 3]
            bank[39] = [3, 2, 1]
            bank[40] = [3, 2, 2]
            bank[41] = [3, 2, 3]
            bank[42] = [3, 2, 4]
            bank[43] = [3, 3, 1]
            bank[44] = [3, 3, 2]
            bank[45] = [3, 4, 2]
            bank[46] = [4, 1, 1]
            bank[47] = [4, 1, 2]
            bank[48] = [4, 1, 5]
            bank[49] = [4, 1, 7]
            bank[50] = [4, 2, 1]
            bank[51] = [4, 2, 3]
            bank[52] = [4, 3, 2]
            bank[53] = [4, 5, 1]
            bank[54] = [4, 7, 1]
            bank[55] = [5, 1, 4]
            bank[56] = [5, 4, 1]
            bank[57] = [6, 1, 1]
            bank[58] = [6, 1, 2]
            bank[59] = [6, 1, 6]
            bank[60] = [6, 2, 1]
            bank[61] = [6, 6, 1]
            bank[62] = [7, 1, 4]
            bank[63] = [7, 4, 1]
            bank[64] = [1, 1, -1]
            bank[65] = [1, 1, -2]
            bank[66] = [1, 1, -3]
            bank[67] = [1, 1, -4]
            bank[68] = [1, 1, -6]
            bank[69] = [1, 2, -1]
            bank[70] = [1, 2, -2]
            bank[71] = [1, 2, -3]
            bank[72] = [1, 2, -4]
            bank[73] = [1, 2, -6]
            bank[74] = [1, 3, -1]
            bank[75] = [1, 3, -2]
            bank[76] = [1, 3, -3]
            bank[77] = [1, 4, -1]
            bank[78] = [1, 4, -2]
            bank[79] = [1, 4, -5]
            bank[80] = [1, 4, -7]
            bank[81] = [1, 5, -4]
            bank[82] = [1, 6, -1]
            bank[83] = [1, 6, -2]
            bank[84] = [1, 6, -6]
            bank[85] = [1, 7, -4]
            bank[86] = [2, 1, -1]
            bank[87] = [2, 1, -2]
            bank[88] = [2, 1, -3]
            bank[89] = [2, 1, -4]
            bank[90] = [2, 1, -6]
            bank[91] = [2, 2, -1]
            bank[92] = [2, 2, -3]
            bank[93] = [2, 3, -1]
            bank[94] = [2, 3, -2]
            bank[95] = [2, 3, -3]
            bank[96] = [2, 3, -4]
            bank[97] = [2, 4, -1]
            bank[98] = [2, 4, -3]
            bank[99] = [2, 6, -1]
            bank[100] = [3, 1, -1]
            bank[101] = [3, 1, -2]
            bank[102] = [3, 1, -3]
            bank[103] = [3, 2, -1]
            bank[104] = [3, 2, -2]
            bank[105] = [3, 2, -3]
            bank[106] = [3, 2, -4]
            bank[107] = [3, 3, -1]
            bank[108] = [3, 3, -2]
            bank[109] = [3, 4, -2]
            bank[110] = [4, 1, -1]
            bank[111] = [4, 1, -2]
            bank[112] = [4, 1, -5]
            bank[113] = [4, 1, -7]
            bank[114] = [4, 2, -1]
            bank[115] = [4, 2, -3]
            bank[116] = [4, 3, -2]
            bank[117] = [4, 5, -1]
            bank[118] = [4, 7, -1]
            bank[119] = [5, 1, -4]
            bank[120] = [5, 4, -1]
            bank[121] = [6, 1, -1]
            bank[122] = [6, 1, -2]
            bank[123] = [6, 1, -6]
            bank[124] = [6, 2, -1]
            bank[125] = [6, 6, -1]
            bank[126] = [7, 1, -4]
            bank[127] = [7, 4, -1]
            bank[128] = [1, -1, 1]
            bank[129] = [1, -1, 2]
            bank[130] = [1, -1, 3]
            bank[131] = [1, -1, 4]
            bank[132] = [1, -1, 6]
            bank[133] = [1, -2, 1]
            bank[134] = [1, -2, 2]
            bank[135] = [1, -2, 3]
            bank[136] = [1, -2, 4]
            bank[137] = [1, -2, 6]
            bank[138] = [1, -3, 1]
            bank[139] = [1, -3, 2]
            bank[140] = [1, -3, 3]
            bank[141] = [1, -4, 1]
            bank[142] = [1, -4, 2]
            bank[143] = [1, -4, 5]
            bank[144] = [1, -4, 7]
            bank[145] = [1, -5, 4]
            bank[146] = [1, -6, 1]
            bank[147] = [1, -6, 2]
            bank[148] = [1, -6, 6]
            bank[149] = [1, -7, 4]
            bank[150] = [2, -1, 1]
            bank[151] = [2, -1, 2]
            bank[152] = [2, -1, 3]
            bank[153] = [2, -1, 4]
            bank[154] = [2, -1, 6]
            bank[155] = [2, -2, 1]
            bank[156] = [2, -2, 3]
            bank[157] = [2, -3, 1]
            bank[158] = [2, -3, 2]
            bank[159] = [2, -3, 3]
            bank[160] = [2, -3, 4]
            bank[161] = [2, -4, 1]
            bank[162] = [2, -4, 3]
            bank[163] = [2, -6, 1]
            bank[164] = [3, -1, 1]
            bank[165] = [3, -1, 2]
            bank[166] = [3, -1, 3]
            bank[167] = [3, -2, 1]
            bank[168] = [3, -2, 2]
            bank[169] = [3, -2, 3]
            bank[170] = [3, -2, 4]
            bank[171] = [3, -3, 1]
            bank[172] = [3, -3, 2]
            bank[173] = [3, -4, 2]
            bank[174] = [4, -1, 1]
            bank[175] = [4, -1, 2]
            bank[176] = [4, -1, 5]
            bank[177] = [4, -1, 7]
            bank[178] = [4, -2, 1]
            bank[179] = [4, -2, 3]
            bank[180] = [4, -3, 2]
            bank[181] = [4, -5, 1]
            bank[182] = [4, -7, 1]
            bank[183] = [5, -1, 4]
            bank[184] = [5, -4, 1]
            bank[185] = [6, -1, 1]
            bank[186] = [6, -1, 2]
            bank[187] = [6, -1, 6]
            bank[188] = [6, -2, 1]
            bank[189] = [6, -6, 1]
            bank[190] = [7, -1, 4]
            bank[191] = [7, -4, 1]
            bank[192] = [1, -1, -1]
            bank[193] = [1, -1, -2]
            bank[194] = [1, -1, -3]
            bank[195] = [1, -1, -4]
            bank[196] = [1, -1, -6]
            bank[197] = [1, -2, -1]
            bank[198] = [1, -2, -2]
            bank[199] = [1, -2, -3]
            bank[200] = [1, -2, -4]
            bank[201] = [1, -2, -6]
            bank[202] = [1, -3, -1]
            bank[203] = [1, -3, -2]
            bank[204] = [1, -3, -3]
            bank[205] = [1, -4, -1]
            bank[206] = [1, -4, -2]
            bank[207] = [1, -4, -5]
            bank[208] = [1, -4, -7]
            bank[209] = [1, -5, -4]
            bank[210] = [1, -6, -1]
            bank[211] = [1, -6, -2]
            bank[212] = [1, -6, -6]
            bank[213] = [1, -7, -4]
            bank[214] = [2, -1, -1]
            bank[215] = [2, -1, -2]
            bank[216] = [2, -1, -3]
            bank[217] = [2, -1, -4]
            bank[218] = [2, -1, -6]
            bank[219] = [2, -2, -1]
            bank[220] = [2, -2, -3]
            bank[221] = [2, -3, -1]
            bank[222] = [2, -3, -2]
            bank[223] = [2, -3, -3]
            bank[224] = [2, -3, -4]
            bank[225] = [2, -4, -1]
            bank[226] = [2, -4, -3]
            bank[227] = [2, -6, -1]
            bank[228] = [3, -1, -1]
            bank[229] = [3, -1, -2]
            bank[230] = [3, -1, -3]
            bank[231] = [3, -2, -1]
            bank[232] = [3, -2, -2]
            bank[233] = [3, -2, -3]
            bank[234] = [3, -2, -4]
            bank[235] = [3, -3, -1]
            bank[236] = [3, -3, -2]
            bank[237] = [3, -4, -2]
            bank[238] = [4, -1, -1]
            bank[239] = [4, -1, -2]
            bank[240] = [4, -1, -5]
            bank[241] = [4, -1, -7]
            bank[242] = [4, -2, -1]
            bank[243] = [4, -2, -3]
            bank[244] = [4, -3, -2]
            bank[245] = [4, -5, -1]
            bank[246] = [4, -7, -1]
            bank[247] = [5, -1, -4]
            bank[248] = [5, -4, -1]
            bank[249] = [6, -1, -1]
            bank[250] = [6, -1, -2]
            bank[251] = [6, -1, -6]
            bank[252] = [6, -2, -1]
            bank[253] = [6, -6, -1]
            bank[254] = [7, -1, -4]
            bank[255] = [7, -4, -1]
        picks = random.sample(range(len(bank)), 3)

        self.point = bank[picks[0]]
        self.vec1 = bank[picks[1]]
        self.vec2 = bank[picks[2]]

        if length == 2:
            self.norm1 = math.sqrt(self.vec1[0] ** 2 + self.vec1[1] ** 2)
            self.norm2 = math.sqrt(self.vec2[0] ** 2 + self.vec2[1] ** 2)

        if length == 3:
            self.norm1 = math.sqrt(self.vec1[0] ** 2 + self.vec1[1] ** 2 + self.vec1[2] ** 2)
            self.norm2 = math.sqrt(self.vec2[0] ** 2 + self.vec2[1] ** 2 + self.vec2[2] ** 2)

    # We can also add our own functions. When our ball bounces,
    # its vertical velocity will be negated. (no gravity here!)
    def dotproduct(self):
        self.dot = self.vec1[0] * self.vec2[0] + self.vec1[1] * self.vec2[1] + self.vec1[2] * self.vec2[2]

    def crossproduct(self):
        self.cross = (self.vec1[1] * self.vec2[2] - self.vec2[1] * self.vec1[2], \
                      -self.vec1[0] * self.vec2[2] + self.vec2[0] * self.vec1[2], \
                      self.vec1[0] * self.vec2[1] - self.vec2[0] * self.vec1[1])

    def calcangle(self):
        self.dotproduct()
        # print self.dot/(self.norm1*self.norm2)
        self.angle = math.acos(self.dot / (self.norm1 * self.norm2)) * 180. / math.pi

    def makeline(self, bounds=[0, 1]):
        self.point2 = []
        for i in range(3):
            self.point2.append(self.point[i] + self.vec1[i] * (bounds[1] - bounds[0]))
        (a, b) = (self.point, self.vec1)
        string = '(' + str(self.point[0] - self.vec1[0] * bounds[0]) + '+' + str(self.vec1[0]) + '*t,' \
                 + str(self.point[1] - self.vec1[1] * bounds[0]) + '+' + str(self.vec1[1]) + '*t,' \
                 + str(self.point[2] - self.vec1[2] * bounds[0]) + '+' + str(self.vec1[2]) + '*t)'

        string = string.replace(',0+', ',')
        string = string.replace(',0-', ',-')
        string = string.replace('(0+', '(')
        string = string.replace('(0-', '(-')
        string = string.replace('+0*t', '')
        string = string.replace('+1*t', '+t')
        string = string.replace('-1*t', '-t')
        string = string.replace('+-', '-')
        self.line = string

    def makeplane(self):
        self.point2 = []
        self.point3 = []
        for i in range(3):
            self.point2.append(self.point[i] + self.vec1[i])
            self.point3.append(self.point[i] + self.vec2[i])
        self.crossproduct()
        (a, b, c) = self.cross
        d = -self.point[0] * a - self.point[1] * b - self.point[2] * c
        divisor = reduce(fractions.gcd, (a, b, c, d))
        if divisor != 1:
            a /= divisor
            b /= divisor
            c /= divisor
            d /= divisor
        if d == 0:
            end = ''
        else:
            end = "+" + str(d)

        string = str(a) + "*x+" + str(b) + "*y+" + str(c) + "*z" + end
        string = string.replace('+-', '-')
        # string=string.replace('0*x+','')
        string = string.replace('+0*y+', '+')
        string = string.replace('+0*z+', '+')
        # string=string.replace('0*x-','')
        string = string.replace('+0*y-', '-')
        string = string.replace('+0*z-', '-')
        # string=string.replace('1*','')
        self.plane = string
        # replace 0y, '', '0x', '', '0z',''
        # find  gcd of xyz


def main():
    a = vector(3)
    a.makeline(bounds)
    print a.line
    print a.point, a.point2


if __name__ == '__main__':
    main()
