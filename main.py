# TODO LIST
#-1 TODO read file
#-2 TODO implement VERO (Extended Version of the operations registry) (from now on all actions need do update VERO)
#-3 TODO assert cannonical form
#-4 TODO check for certificate of it being unlimited
#-5 TODO find basic soluction
#-6 TODO identify positive value in c (ci positive means that a bigger xi value would correspond in bigger objective value) 
#-7 TODO increase xi without altering other valus of An, only Ab (respecting restritions)
#-8 TODO assert that new solution is a viable basic solution to a canonical FPI equivalent to the original
#-9 TODO repeat until there are no more positive values



# 1.1 TODO FUTURE - Asser input usage: FOR NOW expecting correct usage

# 8.1 TODO columns that were changed in #5 need to correspond to indentity matrix (gaussian elimination)
# 8.2 TODO objective function needs to be 0 at the columns that were changed (subtract rows from c. its easy since they as alreade I)


# CONVENTIONS:
#   fun() -> Uses action
#   var   -> Uses states

# external imports
import sys

# local imports
import utils as ut
import simplex_module as simplex
import test_module as test

def main():

  # and stores in inp
  c_array, restrictions, b_array = ut.ReadPL('test_text: ')
  print(c_array, restrictions, b_array)

if __name__ == "__main__":
  main()