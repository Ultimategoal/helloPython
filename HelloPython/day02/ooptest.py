class Animal:
    
    def __init__(self):
        self.age = 1
    
    def getOlder(self):
        self.age += 1

ani = Animal()
print(ani.age)
ani.getOlder()
print(ani.age)

class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.skill_lang = 0
        
    def learnFromMama(self):
        self.skill_lang += 1
        
hum = Human()
print("------------------")
print(hum.age)
hum.getOlder()
print(hum.age)
print("------------------")
print(hum.skill_lang)
hum.learnFromMama()
print(hum.skill_lang)
