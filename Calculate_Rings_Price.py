# You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

#* Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
#* Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
#* Spaces and punctuation are counted as engraved units.

def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

print(cost_of_project("devendra", True)) # Output: 180
print(cost_of_project("Hello World", True)) # Output: 210