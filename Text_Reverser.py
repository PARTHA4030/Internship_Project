def reverse_text(text, mode):
    return text[::-1] if mode == '1' else ' '.join(text.split()[::-1])

def main():
    while True:
        choice = input("\n1. Reverse Characters\n2. Reverse Words\n3. Exit\nChoose (1/2/3): ")
        if choice == '3':
            print("Goodbye!"); break
        text = input("Enter text: ")
        if text.strip():
            print("Result:", reverse_text(text, choice))
        else:
            print("Error: Empty input.")

if __name__ == "__main__":
    main()
