from abc import ABC, abstractmethod

class Musician(ABC):

  def get_instrument(self):
    return self.instrument

  def play_solo(self):
    return self.solo

  def __str__(self):
    return f"Hello, I am {self.name}, the {self.get_instrument().lower()} player."

  def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}')"
  
class Guitarist(Musician):

  def __init__(self, name):
    self.name = name
    self.instrument = "Guitar"

  def play_solo(self):
    return "Jimi Hendrix - Little Wing"
    
class Bassist(Musician):

  def __init__(self, name):
    self.name = name
    self.instrument = "Bass"

  def play_solo(self):
    return "Matt Freeman - Maxwell Murder"

class Drummer(Musician):

  def __init__(self, name):
    self.name = name
    self.instrument = "Drum"

  def play_solo(self):
    return "Buddy Rich - Caravan"
  

class Band:
  members = []

  def __init__(self, musicians=None):
    self.musicians = musicians or []
    self.members.append(self)

  def play_solos(self):
    solos = [musician.play_solo() for musician in self.musicians]
    return solos

  def __str__(self):
    return " ".join([str(musician) for musician in self.musicians])
  
  def __repr__(self):
    musician_reprs = repr(self.musicians)
    return f"Band({musician_reprs})"


musicians = [Bassist("Jeremy"), Drummer("Mark")]
band = Band(musicians)
print(len(band.musicians))
print(band.play_solos())
