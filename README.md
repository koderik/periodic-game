# periodic-game
Periodic table game


info about hur man updaterar labels
https://www.delftstack.com/howto/python-tkinter/how-to-change-the-tkinter-label-text/

code graveyard:

test code for generating guess answers when guessing weight
```
num_1, num_2 = abs(random.randint(int_weight-20, int_weight+20))
    dec_1, dec_2 = abs(random.randint(0, 300))
    ans_1 = str(num_1)+"."+str(dec_1)
    ans_2= str(num_2)+"."+str(dec_2)
    guess_dict = {}
```
get alternative
```
def get_alternative(name):
    guess = name
    while guess == name:
        guess = random.choice(list(a_dict.keys()))
    return guess
```