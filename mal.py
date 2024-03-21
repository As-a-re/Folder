import os

def scan_directory(directory):
    suspicious_files = []
    for root, dirs, files in os.walk(directory):  # Fix variable name 'roots' to 'root'
        for file in files:
            if file.endswith(".exe"):  # Added a dot before "exe" to properly check file extension
                suspicious_files.append(os.path.join(root, file))
    return suspicious_files  # Moved the return statement outside the loop

def main():
    directory_to_scan = "C:\\Program Files"
    suspicious_files = scan_directory(directory_to_scan)
    
    if suspicious_files:
        print("Suspicious files found:")
        for file in suspicious_files:
            print(file)
    else:
        print("No suspicious files found. Your system is clean.")

if __name__ == "__main":  # Corrected if statement to check if '__name__' is equal to '__main__'
    main()
            
                