ticket_price = 30000

viewers_age = [5, 2, 25, 30, 1]

total_cost = 0 

for age in viewers_age :
    if age >= 3:
        total_cost += ticket_price
    else:
        print (f"Viewer aged {age} gets free ticket.")
        
print(f"Total ticket cost for all viewers : Rp {total_cost:,}")