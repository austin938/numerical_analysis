# When the package "advection" is run, the __main__.py program will be executed
# Usage: python -m advection
# The "-m" will allow the module to be executed as a script


from .initialization import initialize
from .evolution import evolve


print("Starting simulation of the advection problem!")


initialize()


evolve()


print("Done!")
