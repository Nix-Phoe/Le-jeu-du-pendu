# Le-jeu-du-pendu (Hangman Game)

## Version Française

### DESCRIPTION
Ce projet est une implémentation interactive du jeu du pendu. Le but est de deviner un mot mystère en proposant des lettres, tout en gérant un nombre limité d'essais.

### INSTALLATION

#### Dépendances
Si vous n'avez pas encore installé pygame, exécutez la commande suivante dans votre terminal :

```bash
pip install pygame
```

### UTILISATION

L'interface du jeu comprend plusieurs éléments :
- Une zone de saisie pour entrer vos lettres
- Un compteur d'essais restants (initialisé à 10)
- Une zone d'affichage du mot à deviner
- Un bouton "Rejouer" pour recommencer une partie

#### Déroulement d'une partie

1. Entrez une lettre que vous pensez faire partie du mot mystère
2. Si la lettre est correcte, elle apparaîtra dans le mot. Sinon, le nombre d'essais diminue
3. Continuez à proposer des lettres jusqu'à découvrir le mot complet ou épuiser vos essais
4. Victoire si vous trouvez le mot avant d'avoir utilisé tous vos essais, défaite dans le cas contraire
5. Cliquez sur le bouton "Rejouer" pour lancer une nouvelle partie

**Note :** Entrer deux fois la même lettre peut soit révéler de nouvelles occurrences de cette lettre, soit n'avoir aucun effet.

### CONTRIBUTION
Développé par Nix-Phoe

---

## English Version

### DESCRIPTION
This project is an interactive implementation of the classic Hangman game. The goal is to guess a hidden word by suggesting letters while managing a limited number of attempts.

### INSTALLATION

#### Dependencies
If you haven't installed pygame yet, run the following command in your terminal:

```bash
pip install pygame
```

### USAGE

The game interface includes several elements:
- An input field to enter your letters
- A remaining attempts counter (initialized at 10)
- A display area for the word to guess
- A "Play Again" button to restart a game

#### How to Play

1. Enter a letter you think is part of the mystery word
2. If the letter is correct, it will appear in the word. Otherwise, the number of attempts decreases
3. Continue suggesting letters until you complete the word or run out of attempts
4. You win if you find the word before using all your attempts, otherwise you lose
5. Click the "Play Again" button to start a new game

**Note:** Entering the same letter twice may either reveal new occurrences of that letter or have no effect.

### CONTRIBUTION
Developed by Nix-Phoe