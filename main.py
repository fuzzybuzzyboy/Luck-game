try:
	from local_colorama import *; from random import choice; import msvcrt
	print('Use 0 for items and 1 for items info')

	PlayerHealth=BotHealth=int(200)

	def Weapon_attack(Weapon): return choice([20.5, 16.5, 13.5, 11.5, 10.5, 9]) if Weapon == 'Sword' else choice([26.5, 21, 17.5, 15, 13, 11.5]) if Weapon == 'Gun' else choice([37.5, 30, 25, 21.5, 18.5, 16.5]) if Weapon == 'Shotgun' else None

	def Bot():
		global PlayerHealth
		BotItem = {1: 'Sword', 2: 'Gun', 3: 'Shotgun'}.get(choice([1, 2, 3]), None)
		PlayerHealth -= Weapon_attack(BotItem); PlayerHealth = 0 if PlayerHealth < 1 else PlayerHealth
		print(Fore.BLUE + Style.BRIGHT + f"opponent used {BotItem.lower()} and dealt: {Damage} damage.\nYou now have: {PlayerHealth}", Fore.WHITE, Style.RESET); return
	while True:
		if PlayerHealth < 1: exit(Fore.YELLOW + Style.NORMAL + f"Game over. You lost.\n  Your opponent has: {BotHealth} health." + Fore.WHITE + Style.RESET) # checks if player health is under 0 and if so says the game is over and exits the game
		if BotHealth < 1: exit(Fore.YELLOW + Style.NORMAL + f"Game over. You won.\n  You have: {PlayerHealth} health left." + Fore.WHITE + Style.RESET) # checks if bot health is under 0 and if so says the game is over and exits the game
		print("What to do next? :")
		Playingmove = str(msvcrt.getch()).split("'")[1]
		Playingmove = int(Playingmove) if Playingmove.isdigit() else None
		if Playingmove == 0: print(Fore.WHITE + Style.BRIGHT + "Help list\n    " + Fore.BLUE + "0 For this menu, 1 For items info\n    " + Fore.GREEN + "2 For Sword\n    " + Fore.YELLOW + "3 For Gun.\n    4 For Shotgun\n    "+ Fore.RED + "5 For game exit", Fore.WHITE, Style.RESET)
		elif Playingmove == 1: print(Fore.WHITE + Style.BRIGHT + "Item info list\n    " + Fore.BLUE + "Sword info: The sword does 20 damage with a 1-1-5 chance to actually hit.\n    " + Fore.GREEN + "Gun info: The gun does 35 damage a 1-1-5 chance to actually hit.\n    " + Fore.YELLOW + "Shotgun info: The shotgun currently does 50 damage with a 1-1-5 chance to actually hit.", Fore.WHITE, Style.RESET)
		elif Playingmove in [2, 3, 4]:
			Damage = Weapon_attack({2: 'Sword', 3: 'Gun', 4: 'Shotgun'}.get(Playingmove, None))
			BotHealth -= Damage
			if BotHealth < 1: BotHealth=0
			print(Fore.RED + Style.BRIGHT + "Used " + {2: 'sword', 3: 'gun', 4: 'shotgun'}.get(Playingmove, None) + f" and dealt: {Damage} damage\nopponent health: {BotHealth}", Fore.WHITE, Style.RESET)
		elif Playingmove == 5: exit(f"You exited the game\n    The opponent has: {BotHealth} health\n    You currently have: {PlayerHealth} health")
		elif Playingmove == 6: print(Weapon_attack(choice(['Shotgun', 'Gun', 'Sword'])))
		else: print(Style.DIM + Fore.YELLOW + "Invaild" + Fore.WHITE + Style.RESET); pass
		Bot() if Playingmove in [2, 3, 4] else None
except ModuleNotFoundError as e: exit(f'Module not found: {e}\nPlease (pip) install {str(e).split("'")[1]}')