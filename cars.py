showroom = set()
showroom.add("Tesla")
showroom.add("Grand Marquis")
showroom.add("Mini Hardtop")
showroom.add("MR2 Spyder")

print(len(showroom))

showroom.add("Tesla")
print(showroom)

showroom.update({"Ranger", "Tacoma"})
print(showroom)

showroom.update({"Avalon", "Zebra"})
print(showroom)

showroom.discard("Ranger")
showroom.discard("Zebra")
print(showroom)