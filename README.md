infusionsoft
============

An unofficial Infusionsoft API client for Python

I made this because I didn't like [the official client](https://github.com/infusionsoft/Official-API-Python-Library) and it's not on pypi.

The official client is more of a low-level wrapper around the Infusionsoft API, this library is opinionated,  higher-level and focuses on the task you are tyring to perform, instead of which DataServiceTable you need to manipulate or whatever.

This client only does the things that I needed to do with Infusionsoft, so it's missing a lot of functionality.  I'm not opposed to adding new things.  If you want to add more stuff, add it, add tests for it, and send a pull request.

# Installation

`pip install infusionosft`

# Usage

First initialize the client like this:

```python
from infusionsoft import Infusionsoft
ifs = Infusionsoft(name, api_key)
```

Now you can call methods on it to do things!  

## Add Contacts

This function makes a contact and automatically opts them in to marketing.  Takes a dict with any of the [fields from the Contact table](http://help.infusionsoft.com/developers/tables/contact).

```python
ifs.add({
    'FirstName': 'Kevin',
    'LastName': 'McCarthy',
    'Email': 'me@kevinmccarthy.org',
})
```

## Find Contacts

You can find a contact by email with `ifs.find_by_email('email@address.com)` or by first and last name `ifs.find_by_first_and_last_name('first', 'last')`.   These functions return a user ID

## Get Contact By ID

```python
ifs.get_by_id(1234)
```

This function returns a dict with a bunch of info in it about the contact.


## Get list of owners
```python
ifs.get_lsit_of_owners()
```

Returns a dict with firtst name, ID, and last name of all owners in your IFS system.

## Submit Web Form

This doesn't actually use the IFS API since there is no way to do it through their API that I can find.  Submits a web form, given the form ID, form name, and data you want to post.

```python
ifs.submit_web_form('big_crazy_hex_id', 'Test Web Form', {'ifs_custom_Whatever': 'test value'})
```

## Apply tag

Add a tag to a contact, takes the contact ID and tag Id.

```python
ifs.apply_tag(contact_id, tag_id)
```

## Add note

Add a note to a given contact id with a given title and body string

```python
ifs.add_note(contact_id, note_title, note_body)
```

## Set Owner

Assign the given contact ID to the given owner ID

```python
ifs.set_owner(contact_id, owner_id)
```

## Place Order

Place an order for a list of products, given a contact ID.

```python
ifs.place_order(contact_id, [product1, product2, product3]
```

## Create Opportunity

```python
ifs.create_opportunity(contact_id, title, stage)
```

## Get Opportunities for Contact

```python
ifs.get_opportunities(contact_id, fields)
```
`fields` is an optional sequence containing a list of fields you want from the [Lead table](http://help.infusionsoft.com/developers/tables/lead).  Apparently opportunities are called *Leads* in the api.  Don't ask me why.

## Move Opportunity Stage

```python
ifs.move_opportunity_stage(ifs, contact, stage)
```

Moves all opportunities on a given contact to the stage ID passed in.  Does nothing if the given contact has no opportunities.

# Running tests

If you want to run the integration tests, you'll need an infusionsoft account and API key.  Set the `IFS_API_KEY` and `IFS_NAME` environment variables and run the tests with py.test.  Example:

```bash
IFS_NAME='ab123' IFS_API_KEY=asdfasdfasdfasdfasdfasdfasdfasdf py.test
```

The unit tests can be run without an IFS account.

# Changelog
  * 0.1.1 - Fix bug with setup.py
  * 0.1.0 - Add opportunity features
  * 0.0.1 - Initial release


# License

The MIT License (MIT)

Copyright (c) 2014 Kevin McCarthy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

