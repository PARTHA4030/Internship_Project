import random


adj = ['Cool', 'Happy', 'Brave', 'Mighty']
nouns = ['Dragon', 'Phoenix', 'Eagle', 'Bear']


def gen_username(include_numbers, include_special_chars):
    adjective = random.choice(adj)
    noun = random.choice(nouns)

    if include_numbers:
        return f"{adjective}{noun}{random.randint(1, 1000)}"
    if include_special_chars:
        return f"{adjective}{noun}{random.choice(['!', '@', '#', '$', '%', '^', '&'])}"
    return f"{adjective}{noun}"


def main():
    print("Welcome to the Username Generator")

  
    number_option = input("Add numbers to username? (yes/no): ").strip().lower() == 'yes'
    special_option = input("Add special characters to username? (yes/no): ").strip().lower() == 'yes'
    num_usernames = int(input("How many usernames? "))

    
    usernames = [gen_username(number_option, special_option) for _ in range(num_usernames)]
    for username in usernames:
        print(username)

   
    with open('usernames.txt', 'w') as file:
        file.write("\n".join(usernames))
    print("Usernames saved to 'usernames.txt'")


if __name__ == '__main__':
    main()
