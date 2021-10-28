"""
Имаме n човека наредени в кръг с номера от 1 до n, които участват в игра на броене наречена броенка. Играта е със следните правила:

    Започваме да броим от човека с номер 1.

    Отброяваме m човека участващи в кръга. Последният отброен човек (с номер m) излиза от кръга.

    Повтаряме стъпка 2 (продължавайки да броим от следващия участник), докато в кръга остане само един участник. Нека номерът на участника да бъде p.

Създайте нова функция с име find_winner:

find_winner(n, m)

която по подадени като аргументи n и m връща p.

Напишете и код на езика Python, които да въвежда от клавиатурата n и m и да отпечатва p на екрана. 

Примерни данни find_winner( 8, 3 ) --> 7, find_winner( 11, 5 ) --> 8.
"""


def remove_by_index(l, idx):
    """ Removes an element at position idx in list l.
     Returns the result list as new object. """
    return l[:idx] + l[idx + 1:]


def find_winer(n, m):
	players = list(range(1, n+1))
	print(players)
	curr = 0

	while(len(players)>1):
		curr += m 

		if curr >= len(players):
			print("c:", curr)
			curr = curr % m
		# print(curr)
		# print(players[curr-1])
		i = players.pop(curr-1)
		print("p:", i)
		print("i", curr)
		print(players)
		curr -= 1
		# print(len(players))

	
	return players[0]

if __name__ ==  "__main__":

	# n = int(input("Please, enter people count: "))
	# m = int(input("Please, enter the counting number: "))

	# (n, m) = (10, 4)
	# (n, m) = (8, 3)
	(n, m) = (11, 5)
	p = find_winer(n,m)
	print("Thewinner is: ", p)
	print() 