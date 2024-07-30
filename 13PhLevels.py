ph=float(input("Ingrese el pH(0-14): "))
if ph  > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")