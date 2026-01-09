# Apprentissage et realisation du projet
import pygame
import random

# initialisation
pygame.init()
# mise en place des dehors de l'écran et aussi de tout les parametre:
Blanc = "White"
Noir = "Black"
ecran = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Pendule our Project')

mots_francais = [
    "maison", "chien", "chat", "voiture", "arbre", "fleur", "soleil", "lune", "étoile", "ciel",
    "pluie", "vent", "neige", "feu", "terre", "eau", "rivière", "océan", "lac", "montagne",
    "route", "pont", "rue", "village", "ville", "campagne", "école", "bureau", "hôpital", "magasin",
    "livre", "journal", "papier", "stylo", "crayon", "ordinateur", "téléphone", "internet", "musique", "chanson",
    "film", "théâtre", "peinture", "danse", "sport", "football", "tennis", "vélo", "train", "avion",
    "bateau", "voyage", "vacances", "travail", "argent", "banque", "manger", "boire", "cuisiner", "restaurant",
    "pain", "fromage", "fruit", "pomme", "poire", "orange", "banane", "fraise", "légume", "tomate",
    "carotte", "pomme de terre", "viande", "poisson", "oeuf", "lait", "eau", "thé", "café", "sucre",
    "sel", "poivre", "ami", "famille", "père", "mère", "frère", "sœur", "enfant", "bébé",
    "homme", "femme", "garçon", "fille", "voisin", "maître", "élève", "professeur", "médecin", "policier"
]

running = True
# Mise en place de la police du texte :
police = pygame.font.Font(None, 35)

# Bouton
rejouer = police.render("Rejouer", True, Blanc)
Bouton_shape = rejouer.get_rect(center=(300, 500))

# lettre entrée
lettre = ""
Data = None

# Les réponses manip
reponse = random.choice(mots_francais)
proposition_str = "_" * len(reponse)
print(reponse)

# attempt :
attempt = 10
instruction_attempt = "NOMBRE DE CHANCE RESTANT : "

# Les Texte à utiliser :
j_Bienvenue = police.render('Bienvenue dans le jeu du PENDU', True, Blanc)
j_instruction = police.render("ENTRE UNE LETTRE ", True, Blanc)

# Entrée
champ_de_saisie = pygame.Rect(500, 295, 50, 30)
champ_d_activation = False

while running:
    # les interaction avec les utilisateurs :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if champ_de_saisie.collidepoint(event.pos):
                champ_d_activation = True
            else:
                champ_d_activation = False
            if Bouton_shape.collidepoint(event.pos):
                reponse = random.choice(mots_francais)
                proposition_str = "_" * len(reponse)
                attempt = 10
                print(reponse)
        if event.type == pygame.KEYDOWN:
            # Vérifier si le jeu est terminé avant de traiter les touches
            if proposition_str == reponse or attempt == 0:
                continue

            if event.key == pygame.K_BACKSPACE:
                lettre = lettre[:-1]
            elif event.key == pygame.K_RETURN:
                Data = lettre
                lettre = ""
                proposition_lst = list(proposition_str)  # Convertir en liste
                if Data not in reponse:
                    attempt -= 1

                else:
                    for i, char in enumerate(reponse):
                        if char == Data:
                            proposition_lst[i] = Data

                proposition_str = "".join(proposition_lst)  # Reconvertir en string

            elif event.unicode.isprintable():
                if len(lettre) >= 1:
                    lettre = lettre
                else:
                    lettre = lettre + event.unicode
    j_proposition = police.render(proposition_str, True, Blanc)

    j_attempt = police.render(str(attempt), True, Blanc)

    j_Failure = police.render("OUPS T'AS PERDU", True, "Red")

    j_success = police.render("T'AS GAGNÉ", True, "Green")

    j_intruction_attempt = police.render(instruction_attempt, True, Blanc)

    ecran.fill("Black")
    # Affichage du mot de Bienvenue :
    ecran.blit(j_Bienvenue, j_Bienvenue.get_rect(center=(370, 100)))

    # Affichage du mot de Bienvenue :
    ecran.blit(j_instruction, j_instruction.get_rect(center=(325, 310)))
    ecran.blit(j_proposition, j_proposition.get_rect(center=(360, 200)))
    ecran.blit(j_attempt, j_attempt.get_rect(center=(600, 400)))
    ecran.blit(j_intruction_attempt, j_intruction_attempt.get_rect(center=(350, 400)))

    # Success
    if proposition_str == reponse:
        ecran.blit(j_success, j_success.get_rect(center=(600, 200)))

        # BOUTON Rejouer
        ecran.blit(rejouer, (Bouton_shape.x - 5, Bouton_shape.y - 5))
        pygame.draw.rect(ecran, "white", Bouton_shape, 2)

    # Fail
    if attempt == 0:
        ecran.blit(j_Failure, j_Failure.get_rect(center=(600, 500)))

        # BOUTON Rejouer
        ecran.blit(rejouer, (Bouton_shape.x - 5, Bouton_shape.y - 5))
        pygame.draw.rect(ecran, "white", Bouton_shape, 2)

    # dynamique sur le champ d'ecriture
    couleur_activation = "Grey" if champ_d_activation else "white"

    # Champ d'ecriture
    pygame.draw.rect(ecran, couleur_activation, champ_de_saisie, 2)

    # parametre des affichage des lettres
    lettre_affichage = police.render(lettre, True, "White")

    # affichage
    ecran.blit(lettre_affichage, (champ_de_saisie.x + 5, champ_de_saisie.y))

    # Game changer
    pygame.display.flip()  # mise à jour de l'ecran

# terminus
pygame.quit()
