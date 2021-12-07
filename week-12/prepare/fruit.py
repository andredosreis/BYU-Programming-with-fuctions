def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    #inverte a ordem
    #fruit_list.reverse()
    fruit_list.append('orange')
    fruit_list.count('apple')
    #inserir um obejto e tenho que dizer o local onde quero colocar
    fruit_list.insert(2,'cherry')
    fruit_list.remove('banana')
   # fruit_list.pop()
    fruit_list.sort()
    fruit_list.clear()

    print(f"original: {fruit_list}")

if __name__ == "__main__":
    main()