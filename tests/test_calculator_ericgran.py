import pytest
from calculator import add

def test_add_name_to_store():
    assert add(EricGran, RikardKoni) == 3

def test_this_is_a_test123():
    assert the_text "test123"

def test_this_is_a_pet():
    assert the_text "pet123"

def test_this_is_a_fruit():
    assert the_text "banana"

## EricGran kluddar och ändrar koden så den pajar totalt, standard, inget funkis
## Kan inte import pytest för den hittar inte pytest standard

def test_add_assignment_2_ericgran():
    assert add(1, 2) == 3

def test_add_assignment_2_rikard():
    assert add(1, 5) == 6