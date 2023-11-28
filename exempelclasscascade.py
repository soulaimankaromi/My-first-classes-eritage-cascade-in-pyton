class DateNaissance:
    def __init__(self,jour,mois,annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee
    def ToString(self):
        return str(self.jour)+"/"+str(self.mois)+"/"+str(self.annee)
class Personne:
    def __init__(self,nom,prenom,datednaissance):
        self.nom = nom 
        self.prenom = prenom
        self.datednaissance = datednaissance
    def Afficher(self):
        print("le nom & le prenom :"+self.nom+" "+self.prenom)
        print("la date de naissance est :"+self.datednaissance.ToString())
class Employe(Personne):
    def __init__(self, nom, prenom, datednaissance,salaire):
        super().__init__(nom, prenom, datednaissance)
        self.salaire = salaire
    def Afficher(self):
        super().Afficher()
        print("le salaire est :"+ str(self.salaire))
class Chef(Employe):
    def __init__(self, nom, prenom, datednaissance, salaire,service):
        super().__init__(nom, prenom, datednaissance, salaire)
        self.service = service
    def Afficher(self):
        super().Afficher()
        print("le service est"+self.service)