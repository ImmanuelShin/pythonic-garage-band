from abc import ABC, abstractmethod

class Musician(ABC):
  """
  Abstract base class representing a generic musician.

  Attributes:
    name (str): The name of the musician.
    instrument (str): The instrument the musician plays.
  """

  def __init__(self, name):
    """
    Initialize a new musician instance.

    Args:
      name (str): The name of the musician.
    """
    self.name = name

  def get_instrument(self):
    """
    Return the instrument that the musician plays.

    Returns:
      str: The name of the instrument.
    """
    return self.instrument

  @abstractmethod
  def play_solo(self):
    """
    Abstract method to play a solo. Must be implemented in subclasses.
    """
    pass

  @abstractmethod
  def some_method_that_must_be_implemented_in_base_class(self):
    """
    Abstract method to be intentionally left unimplemented by Keyboardist subclass.
    """
    pass

  def __str__(self):
    """
    Return a string representation of the musician.

    Returns:
      str: A string describing the musician.
    """
    return f"My name is {self.name} and I play {self.get_instrument()}"

  def __repr__(self):
    """
    Return an unambiguous string representation of the musician.

    Returns:
      str: A string representation of the Musician instance.
    """
    return f"{self.__class__.__name__} instance. Name = {self.name}"
  
class Guitarist(Musician):
  """
  Represents a guitarist, a subclass of Musician.
  """

  def __init__(self, name):
    """
    Initialize a new guitarist instance.

    Args:
      name (str): The name of the guitarist.
    """
    super().__init__(name)
    self.instrument = "guitar"

  def play_solo(self):
    """
    Perform a guitar solo.

    Returns:
      str: Description of the guitar solo.
    """
    return "face melting guitar solo"
  
  def some_method_that_must_be_implemented_in_base_class(self):
    """
    Implementation of the required abstract method.

    Returns:
      str: A string indicating the method implementation.
    """
    return "incomplete guitar"
    
class Bassist(Musician):
  """
  Represents a bassist, a subclass of Musician.
  """

  def __init__(self, name):
    """
    Initialize a new bassist instance.

    Args:
      name (str): The name of the bassist.
    """
    super().__init__(name)
    self.instrument = "bass"

  def play_solo(self):
    """
    Perform a bass solo.

    Returns:
      str: Description of the bass solo.
    """
    return "bom bom buh bom"

  def some_method_that_must_be_implemented_in_base_class(self):
    """
    Implementation of the required abstract method.

    Returns:
      str: A string indicating the method implementation.
    """
    return "incomplete bass"

class Drummer(Musician):
  """
  Represents a drummer, a subclass of Musician.
  """

  def __init__(self, name):
    """
    Initialize a new drummer instance.

    Args:
      name (str): The name of the drummer.
    """
    super().__init__(name)
    self.instrument = "drums"

  def play_solo(self):
    """
    Perform a drum solo.

    Returns:
      str: Description of the drum solo.
    """
    return "rattle boom crash"

  def some_method_that_must_be_implemented_in_base_class(self):
    """
    Implementation of the required abstract method.

    Returns:
      str: A string indicating the method implementation.
    """
    return "incomplete drum"

class Keyboardist(Musician):
  """
  Represents a keyboardist, a subclass of Musician.
  """

  def __init__(self, name):
    """
    Initialize a new keyboardist instance.

    Args:
      name (str): The name of the keyboardist.
    """
    super().__init__(name)
    self.instrument = "keyboard"

  def play_solo(self):
    """
    Perform a keyboard solo.

    Returns:
      str: Description of the keyboard solo.
    """
    return "keyboard solo"

class Band:
  """
  Represents a band consisting of various musicians.

  Attributes:
    instances (list): A class variable that holds all instances of Band.
    members (list): A list of Musician instances in the band.
    name (str): The name of the band.
    musicians (list): A list of musicians in the band.
  """

  instances = []
  members = []

  def __init__(self, name="Band", musicians=None):
    """
    Initialize a new band instance.

    Args:
      name (str): The name of the band.
      musicians (list): A list of Musician instances.
    """
    self.musicians = musicians or []
    self.members = self.musicians
    self.name = name
    Band.instances.append(self)

  def play_solos(self):
    """
    Have each musician in the band play a solo.

    Returns:
      list: A list of strings describing each musician's solo.
    """
    solos = [musician.play_solo() for musician in self.musicians]
    return solos
  
  @classmethod
  def to_list(cls):
    """
    Get a list of all Band instances.

    Returns:
      list: A list of Band instances.
    """
    return cls.instances

  def __str__(self):
    """
    Return a string representation of the band.

    Returns:
      str: A string describing the band and its members.
    """
    return " ".join([str(musician) for musician in self.musicians])
  
  def __repr__(self):
    """
    Return an unambiguous string representation of the band.

    Returns:
      str: A string representation of the Band instance.
    """
    musician_reprs = repr(self.musicians)
    return f"Band({musician_reprs})"


