import random as r 

def get_random(list):
    return r.choice(list)

def guess(x,list):
    g = get_random(list)
    if x == g:
        return g
    else:
        list.remove(g)
        return guess(x,list)

def main():
    num = int(input('Number to guess'))
    r_y = int(input("Enter Highest bound: "))   

    list = []
    for i in range(r_y):
        list.append(i) 

    result = guess(num,list)
    print(f"Found the number {result} = {num}")

if __name__ == '__main__':
    main()