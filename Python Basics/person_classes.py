class Person:
    def __init__(self, first_name, last_name, health, status):
        "initialize attributes to be used in/available for all class methods in this class, and for class objects created by this class."
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.status = status
         
    def introduce(self):
        "all people introduce themselves"
        print("Hello, my name is {} {}".format(self.first_name, self.last_name))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.first_name))
        elif emotion == 2:
            print("{} is sad right now".format(self.first_name))
    
    def status_change(self):
        if self.health == 100:
            print("{} is totally health!".format(self.first_name))
        elif self.health >= 76:
            print("{} feels tired.".format(self.first_name))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.first_name))
        elif  self.health >= 40:
            print("{} goes to the doctor".format(self.first_name))
        else:
            print("{} is unconscious.".format(self.first_name))


Dana = Person("Dana", "Younis", 100, status=True)
Younis = Person("Younis", "Abdullah", 88, status=False)
Hajar = Person("Hajar", "Emam", 70, status=True)

print("{} is my friend? {}".format(Dana.first_name, Dana.status))
print("{} is my friend? {}".format(Younis.first_name, Younis.status))

Dana.introduce()
Younis.introduce()
Hajar.introduce()

Dana.status_change()
Younis.status_change()
Hajar.status_change()



class Enemy(Person):
    def __init__(self,weapon, first_name, last_name, health, status):
        super().__init__(first_name, last_name, health, status)
        self.weapon = weapon
    

    def introduce(self):
        print("I will kill you")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)
    
    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.first_name))
    
    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.first_name))
        if other.status == True:
            other.status = False

Eslam =  Enemy('rock', 'Eslam', 'Mohammed', 75, status=False)

Eslam.hurt(Younis)
Eslam.insult(Hajar)
Eslam.steal(Younis)
Eslam.introduce()