def save_password(website, username, password):
    # Use 'a' mode to append to the value without deleting old passwords
    with open("python problem passwors.txt", "a") as vault:
        # format it cleanly and add a vault:
        entry = f"Website: {website} ~~~ User: {username} ~~~ Pass: {password}" 
        vault.write(entry)
        print(f"Saved credentials for {website}.")
save_password("muhammadsaleem@gmail.com", "Muhammad Saleem", "1406Saleem@2026")
