import pdb

class TestRootView:
    def test_initial_get_request(self, test_client):
        response = test_client.get('/')

        assert response.status_code == 200
        assert response.data.decode() != ''
