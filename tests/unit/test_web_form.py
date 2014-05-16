import mock
from infusionsoft.client import Infusionsoft

@mock.patch('infusionsoft.client.requests')
def test_submit_web_form(requests):
    ifs = Infusionsoft('foo','bar')
    ifs.submit_web_form(1234, 'test', {'key': 'value'})
    requests.post.assert_called_with(
        'https://foo.infusionsoft.com/app/form/process/1234', 
        data={
            'infusionsoft_version': '1.29.8.45', 
            'inf_form_name': 'test', 
            'inf_form_xid': 1234, 
            'submit': 'Submit', 
            'key': 'value'
        }
    )

