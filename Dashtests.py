import dash
from dash import Dash, dcc, html, Input, Output, callback
import pytest
from dash.testing.application_runners import import_app



app = import_app("quantium")

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("h1", "Impact of Pink Morsels Price Increase on Sales")

def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("div#sales-chart")

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("div#region-selector")

if __name__ == '__main__':
    pytest.main([__file__])
