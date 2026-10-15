
def budget_remaining(budget, food, transport):
    return budget - food - transport

def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining."


print(f"Normal case: {budget_remaining(2000, 600, 500)}")#Input: budget=2000, food=600, transport=500. Expected output: 900. Actual output:900. Pass")
print(f"Zero case: {budget_remaining(1500, 900, 600)}")#Input: budget=1500, food=900, transport=600. Expected output: 0. Actual output:0. Pass")
print(f"Overspend case: {budget_remaining(1600, 900, 900)}")#Input: budget=1600, food=900, transport=900. Expected output: -200. Actual output:-200. Pass")

print(budget_message("Ada", 500))
print(budget_message("Tobi", -300))

remaining = budget_remaining(2000, 900, 600)
print(remaining)

message = budget_message("Ada", remaining)
print(message)
