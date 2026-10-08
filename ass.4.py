
secret_message = input("Enter the secret message (substring): ")
coded_message = input("Enter the coded message (string): ")
if secret_message in coded_message:
    print(f"The secret message '{secret_message}' is found in the coded message.")
else:
    print(f"The secret message '{secret_message}' is not found in the coded message.")