class Teacher:
    def __init__(self, name):
        self.name = name
    def update_name(self, name):
        self.name = name
teacher_list = []
teacher_list.append( Teacher('MC HotDog') )
teacher_list.append( Teacher('Kris Wu') )
teacher_list.append( Teacher('Will Pan') )
teacher_list[0].update_name('MC HotDog and Ayal Komod')
for i in teacher_list:
    print(i.name)

