members = ["Tom", "Mark", "Travis"]

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end = " ")
        print()
        
class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thumb", "Bling"])
        
class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Bam", "Boom"])
        
    def count(self):
        n = 1
        while n <= 4:
            print(n)
            n += 1
            
    def spontaneously_combust(self):
        print('"Spontaneously Combusts"')
        
class Band(object):
    def hire(self):
        for people in members:
            members.append(input())
            return members
        
    def fire(self):
        for people in members:
            members.remove(input())
            return members
        
    def play_music(self):
        Drummer.count(self)
        # Drummer.solo(3)
        # Guitarist.solo(3)
        # Bassist.solo(3)