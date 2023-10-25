import dash
from dash import Dash, dcc, html, Input, Output, callback
import pytest
from dash.testing.application_runners import import_app


# Import your Dash app
app = import_app("quantium")

# Test 1: Check if the header is present
def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("h1", "Impact of Pink Morsels Price Increase on Sales")

# Test 2: Check if the visualization is present
def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("div#sales-chart")

# Test 3: Check if the region picker is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("div#region-selector")

if __name__ == '__main__':
    pytest.main([__file__])
