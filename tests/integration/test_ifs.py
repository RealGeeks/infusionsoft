from infusionsoft import Infusionsoft
import os
import binascii
import pytest

@pytest.fixture
def randstring():
    return binascii.b2a_hex(os.urandom(15))

@pytest.fixture
def ifs():
    return Infusionsoft(
        os.environ.get('IFS_NAME'),
        os.environ.get('IFS_API_KEY')
    )

@pytest.fixture
def contact(ifs, randstring):
    test_data = {'FirstName': randstring, 'LastName': randstring, 'Email': 'testguy' + randstring + '@example.com'}
    return ifs.add(test_data)

def test_add_and_get(ifs, randstring):
    test_data = {'FirstName': randstring, 'LastName': randstring, 'Email': 'testguy' + randstring + '@example.com'}
    uid = ifs.add(test_data)
    assert ifs.get_by_id(uid) == test_data
    assert ifs.find_by_email(test_data['Email'])['Id'] == uid
    assert ifs.find_by_first_and_last_name(randstring, randstring)['Id'] == uid

def test_get_list_of_owners(ifs):
    owners = ifs.get_list_of_owners()
    assert len(owners)
    assert set(['LastName', 'FirstName', 'Id']) == set(owners[0].keys())

def test_apply_tag(ifs, contact):
    uid = contact
    ifs.apply_tag(uid, 1)

def test_add_note(ifs, contact):
    uid = contact
    ifs.apply_tag(uid, 1)

def test_set_owner(ifs, contact):
    owner_id = ifs.get_list_of_owners()[0]['Id']
    ifs.set_owner(contact, owner_id)
