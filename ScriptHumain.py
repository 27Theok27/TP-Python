class humain():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    
    def demander_Ordres(self):
        ordre = input("Que voulez-vous faire ?")
        return ordre

    def marcher(self, x, y):
        self.x=int(x)
        self.y=int(y)
        
        print("Vous avez demandé de ", ordre)

    def 