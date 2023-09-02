class Compound:
    def __init__(self,compound):
        self.compound = compound
        self.cyc = ''
        self.root_word = ''
        self.secondary_prefix = ''
        self.c_atoms = None
        self.hyd_atoms = None

        if self.compound == "CH4":
            print("Methane")
        else:
            root_word = ["Meth", "Eth", "Prop", "But", "Pent", "Hex", "Hept", "Oct", "Non", "Dec"]
            functionals = ['-(OH)','-(CO)-','-(CHO)','-(COOH)','-(NH2)']
            halogens = ['Cl','Br','F','I']
            secondary_prefix = ''
            cyc = ''
            FuncTrue = False
            halTrue = False
            AmTrue = False

            for i in self.compound:
                if i == "H":
                    hyd_place = self.compound.find(i)
                if i == "C":
                    carb_place = self.compound.find(i)

            for i in functionals:
                if i in self.compound:
                    func_place = self.compound.find(i)
                    self.functional_group = i
                    FuncTrue = True

            for i in halogens:
                if i in self.compound:
                    hal_place = self.compound.find(i)
                    self.halogen_grp = i
                    halTrue = True

            c_atoms  = int(self.compound[carb_place+1:hyd_place])
            if FuncTrue: 
                hyd_atoms = int(self.compound[hyd_place+1:func_place]) + 1
            elif halTrue:
                hyd_atoms = int(self.compound[hyd_place+1:hal_place])
            elif AmTrue:
                hyd_atoms = int(self.compound[hyd_place+1:func_place]) + 1
            else:
                hyd_atoms = int(self.compound[hyd_place+1:])

            if hyd_atoms == 2*c_atoms + 2:
                self.secondary_prefix += 'ane'
            elif hyd_atoms == 2*c_atoms:
                self.secondary_prefix += 'ene'
            elif hyd_atoms == 2*c_atoms - 2:
                self.secondary_prefix += 'yne'
            elif hyd_atoms == 2*c_atoms + 1:
                self.secondary_prefix += 'yl'
            elif hyd_atoms == c_atoms:
                cyc += 'Cyclo-'
                self.secondary_prefix += 'ane' 

            alc_ = ['-(OH)']
            ald_ = ['-(CHO)']
            ket_ = ['-(CO)-']
            am_ = ['-(NH2)']
            cbxylics = ['-(COOH)']
            if FuncTrue:
                if self.functional_group in alc_:
                    self.Alcohols(root_word[c_atoms - 1])
                if self.functional_group in ald_:
                    self.Aldehydes(root_word[c_atoms])
                if self.functional_group in ket_:
                    self.Ketones()
                if self.functional_group in am_:
                    self.Amines(root_word[c_atoms - 1])
                if self.functional_group in cbxylics:
                    self.Carboxylics(root_word[c_atoms])
                
            elif halTrue:
                self.Halogen(root_word[c_atoms - 1])
            else:
                self.Hydrocarbons(root_word[c_atoms - 1])

    def Hydrocarbons(self,root_word):
        self.root_word = root_word
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix}')


    def Halogen(self, root_word):
        self.root_word = root_word
        print("Halogen detected\n")
        hal = {'Cl': 'Chloride', 'Br': 'Bromide', 'I': 'Iodide', 'F': 'Fluoride'}
        hal_prefix = hal.get(self.halogen_grp, "Unknown")
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + hal_prefix}')

    def Alcohols(self,root_word):
        self.root_word = root_word
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + "ol"}')

    
    def Aldehydes(self,root_word):
        self.root_word = root_word
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + "-al"}')


    def Ketones(self):
        print("KETONES")
        lst = self.compound.split("-(CO)-")


        def findpac(compound):

            c_place = compound.find("C")
            h_place = compound.find("H")
            c_atoms = int(compound[c_place + 1:h_place])
            h_atoms = int(compound[h_place + 1:])

            root_word = ["Meth", "Eth", "Prop", "But", "Pent", "Hex", "Hept", "Oct", "Non", "Dec"]
            secondary_prefix = ''
            cyc = ''
            if h_atoms == 2*c_atoms + 2:
                secondary_prefix += 'ane'
            elif h_atoms == 2*c_atoms:
                secondary_prefix += 'ene'
            elif h_atoms == 2*c_atoms - 2:
                secondary_prefix += 'yne'
            elif h_atoms == 2*c_atoms + 1:
                secondary_prefix += 'yl'
            elif h_atoms == c_atoms:
                cyc += 'Cyclo-'
                secondary_prefix += 'ane'

            return cyc + root_word[c_atoms-1] + secondary_prefix
        R1 = findpac(lst[0])
        R2 = findpac(lst[1])

        if R1 == R2:
            print((f"The IUPAC name of your given compound is: {'di'+ R1+'Ketone'}"))
        else:
            print(f"The IUPAC name of your given compound is: {R1 + R2 + 'Ketone'}")
        
    def Carboxylics(self,root_word):
            self.root_word = root_word
            print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + "-oic acid"}')
            pass
    def Amines(self,root_word):
            self.root_word = root_word
            print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + " amine"}')
            
c = input("enter a compound: ")
ele = Compound(c)
