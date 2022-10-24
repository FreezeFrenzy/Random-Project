from time import sleep
import random

#HP
playerHP = 100
enemyHP = 100

#PLAYER ATTACK
while playerHP > 1:
	print("Player HP:", playerHP)
	print("Enemy HP:", enemyHP)
	sleep(1)
	print("")
	print("[Enemies ahead! what will you do?]")
	print("1.Attack 2.Heal")
	attack = input("\n>>>")
	if attack == "1":
		playerATK = random.randint(1,2)
		if playerATK == 1:
			print("\n[You dealt 30 dmg!]\n")
			enemyHP -= 30
			sleep(1)
		elif playerATK == 2:
			print("\n[The enemy dodged your attack!]\n")
			sleep(1)
	if attack == "2":
		if playerHP <= 85:
			print("\n[You drink a healing potion]")
			sleep(1)
			print("[15 HP Restored!]\n")
			sleep(1)
			playerHP += 15
		elif playerHP >= 85:
			print("\n[You cant heal when your HP is above 85!]\n")
			sleep(1)
	
	#WIN/LOSE
	if playerHP < 1:
		print("[You lose..]")
		break
	
	if enemyHP < 1:
		print("[You win!]")
		break
		
	#ENEMY ATTACK
	enemyATK = random.randrange(8,20)
	print("Player HP:", playerHP)
	print("Enemy HP:", enemyHP)
	print("")
	sleep(1)
	print("[Enemy dealt {} dmg!]\n".format(enemyATK))
	sleep(1)
	playerHP -= enemyATK
	
	#WIN/LOSE 2
	if playerHP < 1:
		print("[You lose..]")
		
	if enemyHP < 1:
		print("[You win!]")