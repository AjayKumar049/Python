#Example on object Class Inheritance Method(Master-ChildConcept)
class Soap(object):
    def __init__(self, vegetableoil,distilledwater):
        self.vegetableoil = vegetableoil
        self.distilledwater = distilledwater
    def showfeatures(self):
        print(self.vegetableoil)
        print(self.distilledwater)
    def showfeaturesDetails(self):
        print('The {}  used for the soap'.format(self.vegetableoil))
        print('The {}  used for the soap'.format(self.distilledwater))

class Dove(Soap):
    def __init__(self, vegetableoil,distilledwater,LauricAcid, SodiumStearate):
        self.LauricAcid = LauricAcid
        self.SodiumStearate = SodiumStearate
        Soap.__init__(self,vegetableoil,distilledwater)
    def showfeaturesDetails(self):
        print('The {}  used for the soap'.format(self.vegetableoil))
        print('The {} used for the soap'.format(self.distilledwater))
        print('The {}   used for the soap'.format(self.LauricAcid))
        print('The {}   used for the soap'.format(self.SodiumStearate))

D = Soap('vegetableoil','distilledwater')
D.showfeatures()
D.showfeaturesDetails()

D = Dove('vegetableoil','distilledwater','LauricAcid', 'SodiumStearate')
D.showfeatures()
D.showfeaturesDetails()
 




    