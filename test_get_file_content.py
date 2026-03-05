from functions.get_file_content import get_file_content

TRUNC_MSG = '[...File "lorem.txt" truncated at 10000 characters]'

def main():
    # 1) Truncation test
    content = get_file_content("calculator", "lorem.txt")
    print('get_file_content("calculator", "lorem.txt") truncation check:')
    print("  length:", len(content))
    print("  ends_with_trunc_msg:", content.endswith(TRUNC_MSG))
    print()

    # 2) Required test cases (print outputs)
    print('get_file_content("calculator", "main.py"):')
    print(get_file_content("calculator", "main.py"))
    print("\n" + "-" * 60 + "\n")

    print('get_file_content("calculator", "pkg/calculator.py"):')
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n" + "-" * 60 + "\n")

    print('get_file_content("calculator", "/bin/cat"):')
    print(get_file_content("calculator", "/bin/cat"))
    print("\n" + "-" * 60 + "\n")

    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()