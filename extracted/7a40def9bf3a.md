# Q&A - European Offering OTC Settlement Flows - French Version

Source: https://www.euronext.com/sites/default/files/2026-04/qas_-_evolution_des_flux_de_reglement-livraison_de_gre_a_gre.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

             Q&As - Évolution des flux de règlement-livraison de gré à gré


    1. Dans une relation broker–custodian, si le broker décide de changer de CSD et de settler
       ses opérations de marché dans un autre CSD que celui du custodian (par exemple
       Euronext Securities Milan), dois-je également changer de CSD ? Le changement de CSD
      de mon broker aura-t-il un impact sur mes propres coûts de règlement-livraison ?

Non, grâce à T2S, chaque contrepartie peut choisir indépendamment le CSD dans lequel elle détient son
compte.

Cela n’aura pas d’impact sur les coûts, car une opération intra-CSD et une opération cross-CSD ont le
même  tarif :  il s’agit du même type de message et d’opération, seule l’information contenue dans
 l’instruction de règlement-livraison change.


    2. Quels sont les impacts fiscaux immédiats de ce changement ?

Le passage d’un mode de règlement-livraison cross-CSD à un mode intra-CSD n’a pas de conséquence
 fiscale. En revanche, il convient d’analyser les aspects fiscaux si un participant change de CSD.


    3. Le format ou la structure d’un compte de conservation est-il le même dans tous les CSD,
      ou varie-t-il selon le CSD ?

Oui, le format du compte de conservation varie d’un CSD à un autre.

Cette information est clairement précisée dans les SSI (Standard Settlement Instructions) de votre
contrepartie, ce qui vous permet de savoir précisément comment donner vos instructions.


    4. Comment l’instruction est-elle modifiée lorsqu’un dépositaire ou un autre intermédiaire
        intervient ?

Dans ce cas, il est nécessaire d’instruire la partie 1 et la partie 2 (la partie 1 étant la partie instructrice et
 la partie 2 le bénéficiaire final),

en format MT 15022.

:95P::DEAG or REAG//Beneficiary’s BIC CODE PARTY 1

:97A ::SAFE//Safekeeping Account of BIC CODE PARTY 1

:95P::SELL or BUYR//Beneficiary’s BIC CODE PARTY 2

In 20022 - in the same block (receiving or delivering settlement party)

<Pty2>

<Id>

<AnyBIC>BAMEITMMXXX</AnyBIC>

</Id>

<SfkpgAcct>

<Id>885301</Id>

</SfkpgAcct>

</Pty2>



| 1 of 1


                                        PRIVATE