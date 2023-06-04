import random, string

import sys

from time import sleep

print("")

print("╔════════════════════════════════════════════════════════════════════╗")

print("║ ███╗   ██╗██╗████████╗██████╗  ██████╗  ██████╗ ███████╗███╗   ██╗ ║")

print("║ ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝ ██╔════╝████╗  ██║ ║")

print("║ ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║██║  ███╗█████╗  ██╔██╗ ██║ ║")

print("║ ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║██║   ██║██╔══╝  ██║╚██╗██║ ║")

print("║ ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝███████╗██║ ╚████║ ║")

print("║ ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ║")

print("╠═══════════════════════════════╦════════════════════════════════════╝")

print("║ https://discord.gg/fC6yymUKDX ║")

print("╠═══════════════════════════════╣")

print("║ NitroGen by The UraniuM       ║")

print("╠═══════════════════════════════╝")

amount = int(input("║Number of generated code: "))

value = 1

while value <= amount:

    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))

    f = open("Generated Code.txt", "a+")

    f.write(f"{code}\n")

    f.close()

    print("╠═════════╦═════════════════════════════════════╗")

    print(f"║Generated║{code}║")

    print("╠═════════╩═════════════════════════════════════╝")

    value += 1

words = "║Generated code in «Generated Code.txt»."

for char in words:

    sleep(0.1)

    sys.stdout.write(char)

    sys.stdout.flush()

sleep(1.0)
