import random, string
from pystyle import Colorate, Colors, Center







header_final = """

██╗░░░██╗░█████╗░░█████╗░████████╗░█████╗░
██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
╚██╗░██╔╝██║░░██║██║░░╚═╝░░░██║░░░██║░░██║
░╚████╔╝░██║░░██║██║░░██╗░░░██║░░░██║░░██║
░░╚██╔╝░░╚█████╔╝╚█████╔╝░░░██║░░░╚█████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░░░░╚═╝░░░░╚════╝░\n\n\n\n"""


print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
