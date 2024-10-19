import uuid

# generate uuid from a string using uuid5
uuid_string = "nadjib"
namespace = uuid.UUID("00000000-0000-0000-0000-000000000000")
# Replace with your own namespace UUID
uuid_object = uuid.uuid5(namespace, uuid_string)

print(uuid_object)
