from carbonai import PowerMeter
power_meter = PowerMeter(project_name="FametoBlame")

@power_meter.measure_power(
    package="pandas, numpy",
    algorithm="data cleaning",
    step="preprocessing",
    data_type="tabular",
    comments="Cleaning of csv files + train-test splitting")

def function():
    return "Ptit pd"