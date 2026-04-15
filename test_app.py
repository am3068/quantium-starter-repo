import pytest
from dash.testing.application_runners import import_app


# Load app
@pytest.fixture
def app():
    return import_app("app2") 


#  Test 1: Header is present
def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods Sales Visualiser" in header.text


#  Test 2: Graph is present
def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)
    
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


#  Test 3: Radio buttons (region picker) present
def test_radio_present(dash_duo, app):
    dash_duo.start_server(app)
    
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None