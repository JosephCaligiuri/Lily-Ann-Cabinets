from networktables import NetworkTables

NetworkTables.initialize(server="10.0.1.247")


# Get a reference to the "limelight" table
table = NetworkTables.getTable("limelight")


# Get the current values for tx, ty, ta, and ts from the table
tx = table.getNumber('tx', None)
ty = table.getNumber('ty', None)
ta = table.getNumber('ta', None)
ts = table.getNumber('ts', None)

# Print the current values
print("tx:", tx)
print("ty:", ty)
print("ta:", ta)
print("ts:", ts)