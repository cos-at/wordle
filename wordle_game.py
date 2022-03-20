from colorama import Fore, Style
from collections import Counter
import pickle
import random

allowed_words=[w.upper() for w in pickle.load(open('allowable_words.pkl','rb'))]
answer_key=['ITCHY','SAVES','COURT','GRANT','PEACH','CROWN','BLAST','OILED','PRINT','DONUT','BRAND','SCOOP','BROWN','MOUSE','SWOON','GOOSE','GOONS','SNOOP','SLOPE']

def find_occ(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def get_color(word,loc,ans,num_occ):
    let=word[loc]
    if let==ans[loc]:
        return 'green'
    else:
        green_num=len(set(find_occ(word,let)).intersection(set(find_occ(ans,let))))
        return 'yellow' if let in ans and num_occ<=Counter(ans)[let]-green_num else 'grey'

def print_with_color(word,colors):
    for i in range(len(word)):
        if colors[i]=='green':
            print(Fore.GREEN,end='')
        elif colors[i]=='yellow':
            print(Fore.LIGHTYELLOW_EX,end='')
        else: 
            print(Fore.WHITE,end='')
        print(word[i]+Style.RESET_ALL,end='')
    print()

print('Guess the word:')

ans=random.choice(answer_key)
cols=[]
i=0
while i!=6 and cols!=['green']*5:
    guess=input().upper()
    print ('\033[1A\033[K',end='')
    if len(guess)!=len(ans) or guess not in allowed_words:
        continue
    cols=[get_color(guess,loc,ans,len(guess[:loc+1].split(let))-1) for loc,let in enumerate(list(guess))]
    print_with_color(guess,cols)
    i+=1

print('Correct!' if cols==['green']*5 else 'The word is',Fore.LIGHTBLUE_EX+ans)
