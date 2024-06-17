from main import Person

def test_init():
    person = Person("Darryl")
    assert person.name == "Darryl"

def test_greeet():
    person = Person("Darryl")
    assert person.name == "Darryl"