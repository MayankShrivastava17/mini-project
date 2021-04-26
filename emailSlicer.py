email = input("What is your email id ").strip()

user_name = email[:email.index('@')]

domain_name = email[email.index('@')+1:]

result = "Your username is '{}' and your domain is '{}'".format(user_name, domain_name)

print(result)
