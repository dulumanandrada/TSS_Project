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
Apoi se realizeaza testarea aplicatiei.

![exemplu1](https://github.com/dulumanandrada/TSS_Project/assets/94484148/c06e05a5-e18c-4dbf-a21e-e8eba2a6a696)


# Demo
Rularea codului **q-learning.py**

https://github.com/dulumanandrada/TSS_Project/assets/94484148/391f6cd4-9643-49c2-828c-f46c7c1de7d7

# Folosirea unui tool AI
Ca tool de AI am folosit ChatGPT (3.5) pentru a intelege mai bine tema articolului stiintific ales: utilizarea invatarii prin recompensa in testarea sistemelor software. Acesta a adus in vedere prin raspunsul sau avantajele, dar si dezavantajele acestor algoritmi de RL, asa cum sunt prezentate si in lucrarea stiintifica intr-un mod mai elaborat.

>Folosirea reinforcement learning (învățare prin recompensă) în testarea sistemelor software reprezintă o abordare interesantă și promițătoare. Cu toate acestea, trebuie să fie abordată cu atenție și să fie aplicată în mod corespunzător pentru a aduce beneficii reale.

>Iată câteva aspecte importante:
>1. Automatizarea testelor: Reinforcement learning poate fi folosit pentru a automatiza procesul de generare a testelor și de identificare a scenariilor critice de testare. Acest lucru poate duce la reducerea efortului uman necesar pentru testare.
>2. Explorarea mai eficientă a spațiului de testare: Algoritmul de reinforcement learning poate explora spațiul de testare mult mai eficient decât metodele de testare convenționale, identificând rapid și eficient condițiile critice de testare.
>3. Adaptabilitatea la schimbări: Sistemele software sunt în continuă evoluție, iar reinforcement learning poate fi folosit pentru a adapta strategiile de testare în timp real în funcție de schimbările în aplicație sau în mediul în care rulează.
>4. Optimizarea testării continue: Prin utilizarea reinforcement learning, procesul de testare continuă poate fi optimizat pentru a se asigura că noile funcționalități sau modificări ale codului sunt testate în mod adecvat.

>Cu toate acestea, există și unele provocări și aspecte de luat în considerare:
>1. Complexitatea algoritmului: Implementarea reinforcement learning poate fi complexă și necesită o înțelegere profundă a algoritmilor și a domeniului de aplicare.
>2. Definirea funcțiilor de recompensă: Definirea funcțiilor de recompensă adecvate este crucială pentru succesul algoritmului de reinforcement learning în contextul testării software.
>3. Generalizarea rezultatelor: Rezultatele obținute cu ajutorul reinforcement learning trebuie să fie generalizabile și să nu se bazeze doar pe datele de antrenament disponibile.
>4. Securitate și fiabilitate: Este important să se asigure că utilizarea algoritmului de reinforcement learning în testarea sistemelor software nu compromite securitatea sau fiabilitatea acestora.

>În concluzie, utilizarea reinforcement learning în testarea sistemelor software poate aduce numeroase beneficii, dar necesită o planificare și o implementare atentă pentru a asigura succesul și eficacitatea.

De asemenea, la fel ca in cazul concluziilor la care s-au ajuns in articol, algoritmul de Q-learning pare sa fie cel mai potrivit in testarea sistemelor software conform raspunsului generat de ChatGPT.

>Alegerea celui mai potrivit algoritm de reinforcement learning (RL) pentru testarea sistemelor software depinde de natura specifică a sistemului și de obiectivele testării. Iată câteva algoritmi de RL care ar putea fi potriviți pentru această aplicație:
>1. Q-Learning: Q-Learning este un algoritm de învățare a valorii acțiunii care poate fi eficient pentru problemele în care spațiul de stare și acțiune este discret. Este relativ ușor de implementat și poate fi adaptat pentru a identifica și a executa acțiuni optime în cadrul testării software.
>2. Deep Q-Networks (DQN): DQN este o extensie a Q-Learning care utilizează o rețea neurală profundă pentru a aproxima funcția Q. Acesta poate fi potrivit pentru problemele mai complexe în care spațiul de stare și acțiune este continuu sau mare.
>3. Policy Gradient Methods: Aceste metode se concentrează pe învățarea unei politici directe care să maximizeze recompensa. Pot fi potrivite pentru problemele de testare a sistemelor software în care acțiunile nu sunt discrete și nu există o valoare Q definită.


