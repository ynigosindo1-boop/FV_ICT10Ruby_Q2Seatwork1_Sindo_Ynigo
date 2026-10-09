from pyscript import document

names = ['Joseph Smith', 'Edrian Correa', 'Sean Ho', 'Son Goku', 'Annika Fernandez']

def membership(e):
    firstname = document.getElementById("first_name").value.strip()
    lastname = document.getElementById("last_name").value.strip()
    
    fullname = f"{firstname} {lastname}"

    is_member = fullname in names 

    messages = (
        f"Sorry {fullname}, you didn't get in.",
        f"Congratulations {fullname}! You got in!"
    )

    result_message = messages[is_member]

    document.getElementById("result").innerText = result_message