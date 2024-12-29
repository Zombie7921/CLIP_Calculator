import os

def get_prompt_from_folder(prompt_dir):
    """
    Reads the first .txt file in the given folder and returns its content as a string.
    If multiple files are found, prompts the user to select one.
    """
    if not os.path.exists(prompt_dir):
        raise FileNotFoundError(f"Prompt directory '{prompt_dir}' does not exist.")

    txt_files = [f for f in os.listdir(prompt_dir) if f.endswith(".txt")]
    if not txt_files:
        raise FileNotFoundError(f"No .txt files found in the directory '{prompt_dir}'.")

    # If only one file, use it
    if len(txt_files) == 1:
        selected_file = txt_files[0]
    else:
        # Prompt user to select a file if multiple files are present
        print("Multiple prompts files found:")
        for idx, file_name in enumerate(txt_files, start=1):
            print(f"{idx}. {file_name}")
        choice = input("Select a prompts file by number (default is 1): ").strip()
        selected_file = txt_files[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= len(txt_files) else txt_files[0]

    # Read the selected file
    prompt_file_path = os.path.join(prompt_dir, selected_file)
    with open(prompt_file_path, "r", encoding="utf-8") as file:
        prompt = file.read().strip()
    print(f"Using prompts from file: {prompt_file_path}")
    return prompt
