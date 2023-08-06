# PasswordStore

Python3 utility used to generate complex passwords from one master password.

# Usage

Run `passwordstore` for the first time to generate a password protected secret.
Backup the secret in order to not lose your passwords.

After that you can run `passwordstore` to generate a password and to store it in your clipboard.

Passwords are not stored anywhere and are simply regenerated from secret and identifier.
This means that you can generate same passwords on different machines without needing to sync anything.
