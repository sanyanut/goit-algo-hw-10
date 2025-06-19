import pulp

prob = pulp.LpProblem("Optimize Limonade And Fruit Juice Production", pulp.LpMaximize)

limonade = pulp.LpVariable("limonade", lowBound=0, cat="Integer")
juice = pulp.LpVariable("juice", lowBound=0, cat="Integer")

prob += limonade + juice, "Total_Products"

prob += 2 * limonade + juice <= 100, "Water_Limit"
prob += limonade <= 50, "Sugar_Limit"
prob += limonade <= 30, "LemonJuice_Limit"
prob += 2 * juice <= 40, "FruitPuree_Limit"

prob.writeLP("LimonadeJuiceProduction.lp")
prob.solve()

print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Limonade Amount: {limonade.varValue}")
print(f"Fruit Juice Amount: {juice.varValue}")
print(f"Total Products Amount: {pulp.value(prob.objective)}")
