class Todo:
  def __init__(self, description):
    self._description = description
    self._done = False
  
  @property
  def description(self):
    return self._description

  @description.setter
  def description(self, description):
    self._description = description

  @property
  def done(self):
    return self._done

  def setdone(self):
    self._done = True

  def undone(self):
    self._done = False

  def __str__(self):
    return f"{self.description}, realizada: {'sim' if self.done else 'não'}"

