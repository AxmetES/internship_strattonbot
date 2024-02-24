from datetime import datetime

# timestamp = 1708775160
# dt_object = datetime.utcfromtimestamp(timestamp)
#
# print("Unix Timestamp:", timestamp)
# print("Converted Date and Time (UTC):", dt_object)

timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
print(timestamp)