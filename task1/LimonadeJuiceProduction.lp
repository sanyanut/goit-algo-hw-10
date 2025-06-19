\* Optimize_Limonade_And_Fruit_Juice_Production *\
Maximize
Total_Products: juice + limonade
Subject To
FruitPuree_Limit: 2 juice <= 40
LemonJuice_Limit: limonade <= 30
Sugar_Limit: limonade <= 50
Water_Limit: juice + 2 limonade <= 100
Bounds
 0 <= juice
 0 <= limonade
Generals
juice
limonade
End
