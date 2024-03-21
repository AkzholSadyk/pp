import os

def delete_file(file_path):
    try:
        
        if os.path.exists(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted successfully.")
            else:
                print(f"Error")
        else:
            print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")


file_to_delete = input("Enter the path of the file to delete: ")
delete_file(file_to_delete)