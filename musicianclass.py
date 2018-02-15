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
    def __init__(self, members):
        self.members = members
    
    def hire(self, member):
        self.members.append(member)
        
    def fire(self, member):
        self.members.remove(member)
        
    def play_music(self, length):
        for member in self.members:
            if isinstance(member, Drummer):
                member.count()
        for memeber in self.members:
            memeber.solo(length)
            
if __name__ == "__main__":
    Travis = Drummer()
    Mark = Bassist()
    Tom = Guitarist()
    Blink182 = Band([Mark, Tom, Travis])
    Blink182.play_music(3)