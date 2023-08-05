import math

class Triangle():
    def __init__(self, from_='var', dict=None, A=None, B=None, C=None, a=None, b=None, c=None):
        if from_ == 'var':
            self.angle = {
                "A":A,
                "B":B,
                "C":C
            }
            self.side = {
                "a":a,
                "b":b,
                "c":c
            }
            self.angleUnknown = 0
            self.sideUnknown = 0
            for each in self.angle:
                if self.angle[each] is None:
                    self.angleUnknown+=1
            for each in self.side:
                if self.side[each] is None:
                    self.sideUnknown+=1

            self.angles = [A, B, C]
            self.sides = [a, b, c]
            self.all = self.angles + self.sides
            self.update()
            self.type = self.getType()
            self.isValid()
        if from_ == 'dict' and not dict == None:

            self.angle = {
                "A": dict['a1'],
                "B": dict['a2'],
                "C": dict['a3']
            }
            self.side = {
                "a": dict['s1'],
                "b": dict['s2'],
                "c": dict['s3']
            }
            #print(self.side, self.angle)
            self.side = self.fixDict(self.side)
            self.angle = self.fixDict(self.angle)
            #print(self.side, self.angle)
            self.angleUnknown = 0
            self.sideUnknown = 0
            for each in self.angle:
                if self.angle[each] is None:
                    self.angleUnknown += 1
            for each in self.side:
                if self.side[each] is None:
                    self.sideUnknown += 1


            self.angles = [self.angle['A'], self.angle['B'], self.angle['C']]
            self.sides = [self.side['a'], self.side['b'], self.side['c']]
            self.all = self.angles + self.sides
            self.update()
            self.isValid()
            #print(self.all, self.side, self.angle)

            self.type = self.getType()

    def sas(self):
        side1 = self.sides[0]#float(input('Enter side 1: '))
        angle1 = self.angles[0]#float(input('Enter angle 1: ')) * (math.pi / 180)
        side2 = self.sides[1]#float(input('Enter side 2: '))

        side3 = math.sqrt(side1 ** 2 + side2 ** 2 - 2 * side1 * side2 * math.cos(angle1))
        angle2 = math.asin((side1 * math.sin(angle1)) / side3) * (180 / math.pi)
        angle3 = math.asin((side2 * math.sin(angle1)) / side3) * (180 / math.pi)
        perimeter = side1 + side2 + side3

        return abs(side3), abs(angle2), abs(angle3), perimeter

    def asa(self):
        angle1 = self.angles[0]
        side1 = self.sides[0]
        angle2 = self.angles[1]

        angle3 = math.pi - angle1 - angle2
        side2 = (side1 * math.sin(angle1)) / math.sin(angle3)
        side3 = (side2 * math.sin(angle2)) / math.sin(angle1)
        angle3 = angle3 * (180 / math.pi)
        perimeter = side1 + side2 + side3

        return abs(side2), abs(side3), abs(angle3), perimeter
    def aas(self):
        angle1 = self.angles[0]
        angle2 = self.angles[1]
        side1 = self.sides[0]

        angle3 = math.pi - angle1 - angle2
        side2 = (side1 * math.sin(angle3)) / math.sin(angle1)
        side3 = (side1 * math.sin(angle2)) / math.sin(angle1)
        perimeter = side1 + side2 + side3
        angle3 = angle3 * (180 / math.pi)

        return abs(side2), abs(side3), abs(angle3), perimeter

    def sss(self):
        side1 =self.sides[0]
        side2 = self.sides[1]
        side3 = self.sides[2]

        angle2 = math.acos((side1 ** 2 + side2 ** 2 - side3 ** 2) / (2 * side1 * side2))
        angle3 = math.asin((side1 * math.sin(angle2)) / side3) * (180 / math.pi)
        angle1 = math.asin((side2 * math.sin(angle2)) / side3) * (180 / math.pi)
        angle2 = angle2 * (180 / math.pi)
        perimeter = side1 + side2 + side3

        return abs(angle1), abs(angle2), abs(angle3), perimeter
    def getPos(self, obj, l):
        ind = l.index(obj)
        if ind == 0:
            return 'a1'
        if ind == 1:
            return 'a2'
        if ind == 2:
            return 'a3'
        if ind == 3:
            return 's1'
        if ind == 4:
            return 's2'
        if ind == 5:
            return 's3'
    def isValid(self):
        self.update()
        try:
            if int(self.sides[0]) + int(self.sides[1]) <= int(self.sides[2]):
                raise Exception('Not a valid triangle')
        except:
            pass
        try:
            if int(self.sides[2]) + int(self.sides[1]) <= int(self.sides[0]):
                raise Exception('Not a valid triangle')
        except:
            pass
        try:
            if int(self.sides[0]) + int(self.sides[2]) <= int(self.sides[1]):
                raise Exception('Not a valid triangle')
        except:
            pass

        try:
            if int(self.angles[0]) + int(self.angles[1]) + int(self.angles[2]) != 180:
                raise Exception('Not a valid triangle')
        except:
            pass


    def fixDict(self, dict):
        self.tempDict = dict
        self.k = list(dict.keys())
        self.v = list(dict.values())
        for i in range(len(self.k)):
            if self.v[i] == '' or None:
                self.tempDict.update({self.k[i]: None})
            else:
                self.tempDict.update({self.k[i]: self.v[i]})
        return self.tempDict


    def getType(self):
        self.update()
        self.temp = 0
        try:
            for i in range(len(self.angles)):
                if int(self.angles[i]) < 90:
                    self.temp +=1
            if self.temp == 3:
                self.type = 'Acute'
                return
            self.temp = 0
            self.r = 0
            self.a = 0
            for i in range(len(self.angles)):
                if int(self.angles[i]) == 90:
                    self.r +=1
                if int(self.angles[i]) < 90:
                    self.a += 1
            if self.r == 1 and self.a == 2:
                self.type = 'Right Angled'
                return
            self.r = 0
            self.a = 0
            self.o = 0
            for i in range(len(self.angles)):
                if int(self.angles[i]) > 90:
                    self.o +=1
                if int(self.angles[i]) < 90:
                    self.a += 1
            if self.o == 1 and self.a == 2:
                self.type = 'Obtuse'
                return
            self.type = 'Not enough information at this stage'
        except:
            self.type = 'Not enough information at this stage'
    # def solve(self, Return='dict'):
    def solve(self, Return):

        try:
            if Return == 'turple':
                return self.sss()
            if Return == 'dict':
                self.temp = {}
                self.tempAtt = list(self.sss())
                self.temp.update({'a1':self.tempAtt[0]})
                self.temp.update({'a2': self.tempAtt[1]})
                self.temp.update({'a3': self.tempAtt[2]})
                self.temp.update({'s1': self.sides[0]})
                self.temp.update({'s2': self.sides[1]})
                self.temp.update({'s3': self.sides[2]})
                self.temp.update({'p': self.tempAtt[3]})
                #print(self.temp)
                #print(self.temp)
                return self.temp
        except Exception as e:
            print(e)
        try:
            if Return == 'turple':
                return self.aas()
            if Return == 'dict':
                self.temp = {}
                self.tempAtt = list(self.aas())
                self.temp.update({'a1': self.angles[0]})
                self.temp.update({'a2': self.angles[1]})
                self.temp.update({'a3': self.tempAtt[2]})
                self.temp.update({'s1': self.sides[0]})
                self.temp.update({'s2': self.tempAtt[0]})
                self.temp.update({'s3': self.tempAtt[1]})
                self.temp.update({'p': self.tempAtt[3]})
                #print(self.temp)
                return self.temp

        except Exception as e:
            print(e)
            pass
        try:
            if Return == 'turple':
                return self.aas()
            if Return == 'dict':
                self.temp = {}
                self.tempAtt = list(self.aas())
                self.temp.update({'a1': self.angles[0]})
                self.temp.update({'a2': self.tempAtt[1]})
                self.temp.update({'a3': self.tempAtt[2]})
                self.temp.update({'s1': self.sides[0]})
                self.temp.update({'s2': self.sides[1]})
                self.temp.update({'s3': self.tempAtt[0]})
                self.temp.update({'p': self.tempAtt[3]})
                #print(self.temp)
                return self.temp
        except Exception as e:
            print(e)
            pass
        try:
            if Return == 'turple':
                return self.asa()
            if Return == 'dict':
                self.temp = {}
                self.tempAtt = list(self.asa())
                self.temp.update({'a1': self.angles[0]})
                self.temp.update({'a2': self.angles[1]})
                self.temp.update({'a3': self.tempAtt[2]})
                self.temp.update({'s1': self.sides[0]})
                self.temp.update({'s2': self.tempAtt[0]})
                self.temp.update({'s3': self.tempAtt[1]})
                self.temp.update({'p': self.tempAtt[3]})
                #print(self.temp)
                return self.temp
        except:
            pass

            #raise TypeError(e)
            #return '''Error: {}
#Provide values next time'''.format(e)



    def __str__(self):
        self.getType()
        self.update()
        return '''Triangle Info
Type: {}
Angles: {}
Sides: {}
Perimeter: {}'''.format(self.type, self.angles, self.sides, self.solve(Return='dict')['p'])

    def __len__(self):
        self.update()
        return len(self.all)
    def __int__(self):
        return int(len(self))
    def __float__(self):
        return float(int(self))

    def getAngle(self, a1__, a2__):
        return str(180 - int(a1__) - int(a2__))
    def congruent(self, to):
        if isinstance(to, Triangle):
            #t.isValid()
            self.tempTriangle = to
            t1 = {}
            t1.update({'s1': self.update()[0]})
            t1.update({'s2': self.update()[1]})
            t1.update({'s3': self.update()[2]})
            t1.update({'a1': self.update()[3]})
            t1.update({'a2': self.update()[4]})
            t1.update({'a3': self.update()[5]})

            t2 = {}
            t2.update({'s1': self.tempTriangle.update()[0]})
            t2.update({'s2': self.tempTriangle.update()[1]})
            t2.update({'s3': self.tempTriangle.update()[2]})
            t2.update({'a1': self.tempTriangle.update()[3]})
            t2.update({'a2': self.tempTriangle.update()[4]})
            t2.update({'a3': self.tempTriangle.update()[5]})

            sides = []
            # c = 0
            test = ''
            if not t1['s1'] == '' and not t1['s2'] == '' and not t1['s3'] == '' and not t2['s1'] == '' and not t2[
                                                                                                                   's2'] == '' and not \
            t2['s3'] == '':
                if t1['s1'] == t2['s1'] and t1['s2'] == t2['s2'] and t1['s3'] == t2['s3']:
                    test = test + 'SSS '
            else:
                # print('Not given values')
                pass

            angles1 = []
            angles2 = []
            try:
                angles1.append(t1['a1'])
                angles1.append(t1['a2'])
                angles1.append(t1['a3'])
                # print(angles1, angles2)
                # print(t2)
                angles2.append(t2['a1'])
                angles2.append(t2['a2'])
                angles2.append(t2['a3'])
                # print(angles1, angles2)
            except Exception as e:
                print(e)
            if 1 == 1:
                if angles1[2] == '' and not angles1[1] == '' and not angles1[0] == '':
                    angles1[2] = self.getAngle(angles1[1], angles1[0])
                    t1.update({'a3': angles1[2]})
                if angles1[1] == '' and not angles1[0] == '' and not angles1[2] == '':
                    angles1[1] = self.getAngle(angles1[0], angles1[2])
                    t1.update({'a2': angles1[1]})
                if angles1[0] == '' and not angles1[1] == '' and not angles1[2] == '':
                    angles1[0] = self.getAngle(angles1[1], angles1[2])
                    t1.update({'a1': angles1[0]})
                # print(angles1)

                if angles2[2] == '' and not angles2[1] == '' and not angles2[0] == '':
                    angles2[2] = self.getAngle(angles2[1], angles2[0])
                    t2.update({'a3': angles2[2]})
                if angles2[1] == '' and not angles2[0] == '' and not angles2[2] == '':
                    angles2[1] = self.getAngle(angles2[0], angles2[2])
                    t2.update({'a2': angles2[1]})
                if angles2[0] == '' and not angles2[1] == '' and not angles2[2] == '':
                    angles2[0] = self.getAngle(angles2[1], angles2[2])
                    t2.update({'a1': angles2[0]})

                print(t1, t2)
                cont = 0
                # print(test)
                if not t1['s1'] == '' and not t1['a3'] == '' and not t1['a1'] == '' and not t2['s1'] == '' and not t2[
                                                                                                                       'a3'] == '' and not \
                t2['a1'] == '':
                    if t1['s1'] == t2['s1'] and t1['a1'] == t2['a1'] and t1['a3'] == t2['a3']:
                        test = test + 'ASA '
                        # print('1')
                        cont = 1
                if cont == 0 and not t1['s3'] == '' and not t1['a2'] == '' and not t1['a1'] == '' and not t2[
                                                                                                              's3'] == '' and not \
                t2['a2'] == '' and not t2['a1'] == '':
                    if t1['s3'] == t2['s3'] and t1['a1'] == t2['a1'] and t1['a2'] == t2['a2']:
                        test = test + 'ASA '
                        cont = 1
                        # print('2')
                if cont == 0 and not t1['s2'] == '' and not t1['a2'] == '' and not t1['a3'] == '' and not t2[
                                                                                                              's2'] == '' and not \
                t2['a2'] == '' and not t2['a3'] == '':
                    if t1['s2'] == t2['s2'] and t1['a2'] == t2['a2'] and t1['a3'] == t2['a3']:
                        test = test + 'ASA '
                        cont = 1
                        # print('3')

                # SAS
                cont = 0
                if not t1['s1'] == '' and not t1['s3'] == '' and not t1['a1'] == '' and not t2['s1'] == '' and not t2[
                                                                                                                       's3'] == '' and not \
                t2['a1'] == '':
                    if t1['s1'] == t2['s1'] and t1['s3'] == t2['s3'] and t1['a1'] == t2['a1']:
                        test = test + 'SAS '
                        cont = 1
                if cont == 0:
                    if not t1['s2'] == '' and not t1['s3'] == '' and not t1['a2'] == '' and not t2['s2'] == '' and not \
                    t2['s3'] == '' and not t2['a2'] == '':
                        if t1['s2'] == t2['s2'] and t1['s3'] == t2['s3'] and t1['a2'] == t2['a2']:
                            test = test + 'SAS '
                            cont = 1
                if cont == 0:
                    if not t1['s2'] == '' and not t1['s1'] == '' and not t1['a3'] == '' and not t2['s2'] == '' and not \
                    t2['s1'] == '' and not t2['a3'] == '':
                        if t1['s2'] == t2['s2'] and t1['s1'] == t2['s1'] and t1['a3'] == t2['a3']:
                            test = test + 'SAS '
                            cont = 1

                # RHS
                cont = 0
                if not t1['s1'] == '' and not t1['s3'] == '' and not t1['a1'] == '' and not t2['s1'] == '' and not t2['s3'] == '' and not t2['a1'] == '':
                    if t1['s1'] == t2['s1'] and t1['s3'] == t2['s3'] and t1['a1'] == 90 and t2['a1'] == 90:
                        test = test + 'RHS '
                        cont = 1
                if cont == 0:
                    if not t1['s2'] == '' and not t1['s3'] == '' and not t1['a2'] == '' and not t2['s2'] == '' and not t2['s3'] == '' and not t2['a2'] == '':
                        if t1['s2'] == t2['s2'] and t1['s3'] == t2['s3'] and t1['a2'] == 90 and t2['a2'] == 90:
                            test = test + 'RHS '
                            cont = 1
            # except Exception as e:
            # print(e)#

            # print(angles1)
            # print(angles2)
            print(test)
            if not test == '':
                return ('These triangles are congruent by:' + test)
            else:
                return ('These triangles are not congruent by: SSS, ASA or SAA')
        else:
            raise TypeError('Not a triangle')



    def update(self, w='all', r='list'):
        if w == 'all':
            #print(dict(self.solve(Return='dict')))
            # self.angle.update({'A': self.solve(Return='dict')['a1']})
            #print(self.solve(Return='dict'))
            try:
                self.sa = self.solve(Return='dict')
            except:
                self.sa = self.solve(Return='dict')
            #print(self.sa)
            try:
                self.angle.update({'A': self.sa['a1']})
                self.angle.update({'B': self.sa['a2']})
                self.angle.update({'C': self.sa['a3']})

                self.side.update({'a': self.sa['s1']})
                self.side.update({'b': self.sa['s2']})
                self.side.update({'c': self.sa['s3']})
            except:
                pass

            #print(self.side, self.angle, self.sides, self.angles)

            self.sides = []
            self.sides.append(self.side['a'])
            self.sides.append(self.side['b'])
            self.sides.append(self.side['c'])

            self.angles = []
            self.angles.append(self.angle['A'])
            self.angles.append(self.angle['B'])
            self.angles.append(self.angle['C'])

            self.all = self.angles + self.sides

            #print(self.angles, self.sides)
            if r == 'list':
                return list(self.sides + self.angles)
            elif r == 'dict':
                return self.side, self.angle
            else:
                pass
        if w == 'sides' or w == 'side':
            pass
#caps - angles
#lowercase - sides

if __name__ == '__main__':
    t1 = {'a1': 12, 'a2': 90, 'a3': 80, 's1': 20, 's2':20, 's3':50}
    t2 = {'a1': 10, 'a2': 90, 'a3': 80, 's1': 20, 's2': 50, 's3': 50}
    t = Triangle(from_='dict', dict=t1)
    f = Triangle(from_='dict', dict=t2)

    print(f.congruent(t))


