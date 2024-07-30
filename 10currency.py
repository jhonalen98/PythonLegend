pesos=(int(input("Cuantos pesos tienes: ")))
soles=(int(input("Cuantos soles tienes: ")))
reales=(int(input("Cuantos reales tienes: ")))
pesosUSD=pesos*0.00025
solesUSD=soles*0.27
realesUSD=reales*0.18
usd=pesosUSD+solesUSD+realesUSD
print(usd)