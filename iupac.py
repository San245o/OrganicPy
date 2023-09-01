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
            functionals = ['Cl','Br','F','I','-(OH)','-(CO)-','-(CHO)',]
            secondary_prefix = ''
            cyc = ''
            FuncTrue = False

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
            
            c_atoms  = int(self.compound[carb_place+1:hyd_place])
            if FuncTrue: 
                hyd_atoms = int(self.compound[hyd_place+1:func_place])
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
            hal_ = ['Cl','Br','F','I']
            alc_ = ['-(OH)']
            ald_ = ['-(CHO)']
            ket_ = ['-(CO)-']
            if FuncTrue:
                if self.functional_group in hal_:
                    self.Halogen(root_word[c_atoms - 1])
                if self.functional_group in alc_:
                    self.Alcohols(root_word[c_atoms - 1])
                if self.functional_group in ald_:
                    self.Aldehydes(root_word[c_atoms])
                if self.functional_group in ket_:
                    self.Ketones()

                    
            else:
                self.Hydrocarbons(root_word[c_atoms - 1])



    def Hydrocarbons(self,root_word):
        self.root_word = root_word
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix}')


    def Halogen(self, root_word):
        self.root_word = root_word
        print("Halogen detected\n")
        hal = {'Cl': 'Chloride', 'Br': 'Bromide', 'I': 'Iodide', 'F': 'Fluoride'}
        hal_prefix = hal.get(self.functional_group, "Unknown")
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + hal_prefix}')

    def Alcohols(self,root_word):
        self.root_word = root_word
        print("alcohols")
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + "ol"}')

    
    def Aldehydes(self,root_word):
        print("aldehydes")
        self.root_word = root_word
        print(f'The IUPAC name of your given compound is: {self.cyc + self.root_word + self.secondary_prefix + "-al"}')


    def Ketones(self):
        print("ketones")
        pass 
    
c = input("enter a compound: ")
ele = Compound(c)
