email = 'nitesh.yadav@gmail.com'
mask_ = email.find('@')
mask__ = email[0] + '*******' + email[mask_ -1:]
print(mask__)
