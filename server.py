def main(welcome, user_name = 'You'): #greeting/main function
  user_name = input('What is your name?\n')
  return '{}, {}'.format(welcome,user_name)
  
if __name__ == '__main__':
  main()