from datetime import datetime, timedelta, timezone

# Define a custom time zone (UTC+3:00)
custom_timezone = timezone(timedelta(hours=3))

# Create a datetime object with a specific time zone
dt_with_timezone = datetime(2023, 1, 1, 12, 0, tzinfo=custom_timezone)

# Display the original datetime with timezone information
print("Original Datetime with Timezone:", dt_with_timezone)

# Convert the datetime to a different time zone (UTC)
utc_timezone = timezone.utc
dt_utc = dt_with_timezone.astimezone(utc_timezone)

# Display the converted datetime in UTC
print("Converted Datetime in UTC:", dt_utc)
