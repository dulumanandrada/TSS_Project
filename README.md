# Proiect: Analiza unei lucrari stiintifice

Lucrarea stiintifica aleasa:
[The role of Reinforcement Learning in software testing](https://www.sciencedirect.com/science/article/pii/S0950584923001805?via%3Dihub)

[Raport articol stiintific](https://docs.google.com/document/d/1q4jXPAGfIrMbYedmCHlNhVHoduHIfxo2PNLlyycfJ0E/edit)


## Q-learning
### Descriere mini-aplicatie
Avemn o matrice de tip 5x5, o stare initiala (0,0) si o stare finala (4,4) in care dorim sa ajungem.
Exista 4 tipuri de mutari pe grid: UP, DOWN, LEFT, RIGHT.
Pentru fiecare actiune facuta, se va oferi un reward in functie de cat de aproape sau departe este agentul de starea finala, astfel:
- distanta euclidiana dintre starea finala si cea actuala * (-10)
- +100 daca este starea finala

Se realizeaza antrenarea agentului folosind Q-learning pentru a ajunge in starea finala in cat mai putine mutari.
Apoi se realizeaza testarea acestuia.

![exemplu1](https://github.com/dulumanandrada/TSS_Project/assets/94484148/c06e05a5-e18c-4dbf-a21e-e8eba2a6a696)


# Demo
Rularea codului **q-learning.py**

https://github.com/dulumanandrada/TSS_Project/assets/94484148/391f6cd4-9643-49c2-828c-f46c7c1de7d7

