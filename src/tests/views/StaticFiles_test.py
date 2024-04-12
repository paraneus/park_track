import pdb

class TestStaticFiles:
    def test_retrieve_a_static_file(self, static_file, test_client):
        response = test_client.get(f'/static/{static_file.name}')

        assert static_file.exists()
        assert response.status_code == 200
