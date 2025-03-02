import random

def flip_coin():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

def main():
    while True:
        try:
            num_flips = int(input("How many times would you like to flip the coin? "))
            if num_flips <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        heads = 0
        tails = 0
        
        for _ in range(num_flips):
            result = flip_coin()
            print(result)
            if result == "Heads":
                heads += 1
            else:
                tails += 1
        
        print(f"\nTotal Heads: {heads}")
        print(f"Total Tails: {tails}")
        
        again = input("Flip again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
