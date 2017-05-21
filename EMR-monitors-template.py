# Make sure you replace the API and/or APP key below
# with the ones for your account

from datadog import initialize, api

options = {
    'api_key': '1fb1a9cb893fdcdfc1e2043fdc8b28ee',
    'app_key': 'efbe855b1b460fb3a60dfc827ef2f8fb1fda1214'
}

initialize(**options)

# Create a new monitor
options1 = {
    "notify_no_data": False,
    "thresholds": {'critical': 50, 'warning': 30},
    "no_data_timeframe": 20,
    "require_full_window": True
}
tags = ["account","host"]
api.Monitor.create(type="metric alert", query="avg(last_5m):avg:aws.elasticmapreduce.memory_available_mb{*} by {account,host} > 50", name="Abhi-Test-1", message="{{#is_alert}}We have an alert{{/is_alert}} {{#is_alert_recovery}} \nAlert got resolved{{/is_alert_recovery}}  @abhi.naidu@reancloud.com", tags=tags, options=options1)

options2 = {
    "notify_no_data": False,
    "thresholds": {'critical': 50, 'warning': 30},
    "no_data_timeframe": 20,
    "require_full_window": True
}
tags = ["account","host"]
api.Monitor.create(type="metric alert", query="avg(last_5m):avg:aws.elasticmapreduce.jobs_failed{*} by {account,host} > 50", name="Abhi-Test-2", message="{{#is_alert}}We have an alert{{/is_alert}} {{#is_alert_recovery}} \nAlert got resolved{{/is_alert_recovery}}  @abhi.naidu@reancloud.com", tags=tags, options=options2)

options3 = {
    "notify_no_data": False,
    "thresholds": {'critical': 50, 'warning': 30},
    "no_data_timeframe": 20,
    "require_full_window": True
}
tags = ["account","host"]
api.Monitor.create(type="metric alert", query="avg(last_5m):avg:aws.elasticmapreduce.is_idle{*} by {account,host} > 50", name="Abhi-Test-3", message="{{#is_alert}}We have an alert{{/is_alert}} {{#is_alert_recovery}} \nAlert got resolved{{/is_alert_recovery}}  @abhi.naidu@reancloud.com", tags=tags, options=options3)

options4 = {
    "notify_no_data": False,
    "thresholds": {'critical': 50, 'warning': 30},
    "no_data_timeframe": 20,
    "require_full_window": True
}
tags = ["account","host"]
api.Monitor.create(type="metric alert", query="avg(last_5m):avg:aws.elasticmapreduce.hbase_backup_failed{*} by {account,host} > 50", name="Abhi-Test4", message="{{#is_alert}}We have an alert{{/is_alert}} {{#is_alert_recovery}} \nAlert got resolved{{/is_alert_recovery}}  @abhi.naidu@reancloud.com", tags=tags, options=options4)

options5 = {
    "notify_no_data": False,
    "thresholds": {'critical': 50, 'warning': 30},
    "no_data_timeframe": 20,
    "require_full_window": True
}
tags = ["account","host"]
api.Monitor.create(type="metric alert", query="avg(last_5m):avg:aws.elasticmapreduce.corrupt_blocks{*} by {account,host} > 50", name="Abhi-Test-5", message="{{#is_alert}}We have an alert{{/is_alert}} {{#is_alert_recovery}} \nAlert got resolved{{/is_alert_recovery}}  @abhi.naidu@reancloud.com", tags=tags, options=options5)

options6 = {
    "notify_no_data": False,
    "thresholds": {'critical': 50, 'warning': 30},
    "no_data_timeframe": 20,
    "require_full_window": True
}
tags = ["account","host"]
api.Monitor.create(type="metric alert", query="avg(last_5m):avg:aws.elasticmapreduce.capacity_remaining_gb{*} by {account,host} > 50", name="Abhi-Test-6", message="{{#is_alert}}We have an alert{{/is_alert}} {{#is_alert_recovery}} \nAlert got resolved{{/is_alert_recovery}}  @abhi.naidu@reancloud.com", tags=tags, options=options6)

options7 = {
    "notify_no_data": False,
    "thresholds": {'critical': 50, 'warning': 30},
    "no_data_timeframe": 20,
    "require_full_window": True
}
tags = ["account","host"]
api.Monitor.create(type="metric alert", query="avg(last_5m):avg:aws.elasticmapreduce.apps_failed{*} by {account,host} > 50", name="Abhi-Test-7", message="{{#is_alert}}We have an alert{{/is_alert}} {{#is_alert_recovery}} \nAlert got resolved{{/is_alert_recovery}}  @abhi.naidu@reancloud.com", tags=tags, options=options7)
