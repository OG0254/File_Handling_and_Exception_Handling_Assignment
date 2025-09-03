def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content (converts to uppercase), and writes to a new file.
    Includes comprehensive error handling.
    
    Args:
        input_filename (str): Name of the input file
        output_filename (str): Name of the output file
    """
    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Modify the content (converting to uppercase as an example)
        modified_content = content.upper()
        
        # Write modified content to output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Successfully read {input_filename} and wrote modified content to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}' or '{output_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: '{input_filename}' contains non-text data or incorrect encoding.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

def main():
    """
    Main function to get filename from user and process the file.
    """
    try:
        # Get input filename from user
        input_filename = input("Enter the name of the file to read: ")
        
        # Generate output filename (adding '_modified' to input filename)
        output_filename = f"modified_{input_filename}"
        
        # Call the file processing function
        modify_and_write_file(input_filename, output_filename)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Unexpected error in main: {str(e)}")

if __name__ == "__main__":
    main()