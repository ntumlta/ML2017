number = {'Kobe': 24, 'Lebron': 23}
for k, n in number.items():
    print(k,n)
player = ['Duncan', 'Dirk']
team = ['Spurs', 'Mavs']
for p, t in zip(player, team):
    print('{0} from {1}'.format(p,t))

