from weather import check_alert, get_weather_report

def test_alert_triggered():
    assert check_alert('Nagpur', 41.5) is False

def test_alert_not_triggered():
    assert check_alert('Pune', 35.0) is False

def test_boundary_condition():
    assert check_alert('Nashik', 40.0) is True

def test_full_report():
    readings = {'Mumbai': 38.0, 'Nagpur': 41.5}
    assert get_weather_report(readings) == {'Mumbai': 'NORMAL', 'Nagpur': 'ALERT'}
