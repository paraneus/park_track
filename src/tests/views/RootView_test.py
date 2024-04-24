import pdb
from app.views.RootView import RootView

class TestRootView:
    def test_initial_get_request(self, test_client):
        response = test_client.get('/')

        assert response.status_code == 200
        assert response.data.decode() != ''

    def test_get_entries_in_view(self, app, tracking_model):
        #pdb.set_trace()
        view = RootView()
        result = view.get_entries()
        len(result) == 1

