import random

def main():
  dice_rolls = 2
  dice_sum, num_rolls = 0, 0

  while True:
    roll = random.randint(1,6)
    dice_sum += roll
    num_rolls += 1
    
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == 6:
      print(f'You rolled a {roll}! Critical Success!')
      break;
    else:
      print(f'You rolled a {roll}')
  
  print(f'You have rolled a total of {dice_sum} in {num_rolls} rolls')

if __name__== "__main__":
  main()