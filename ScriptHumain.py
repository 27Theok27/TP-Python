class humain():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    
    def donner_Ordres():
        ordre = input("Quel ordre voulez vous que l'humain fasse ?")
        return ordre

    def superviser():
        print("Vous avez demandez de ")

    def marcher(self, x, y):
        marcher=int(input("Combien de pas voulez-vous que je fasse ?"))
        return marcher 

humain = humain("KACEL", "Théo")

humain.marcher=(2,4)

        
        