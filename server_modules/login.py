from spwd import getspnam

def login(username, password_hash):
        try:
                if password_hash != '*' and password_hash != '!!' and getspnam(username).sp_pwd == password_hash:
                        return True
                else:
                        return False
        except KeyError:
                return False
