import spidev

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)  # (bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 1000000  # Adjust as needed
spi.mode = 0

# Select Arduino (pull SS low)
spi.xfer([0x00])  # Send any byte to SS pin

# Send data to Arduino
tx_data = [0x01, 0x02, 0x03]  # Example data to send
rx_data = spi.xfer2(tx_data)  # Send data and receive response

# Deselect Arduino (pull SS high)
spi.xfer([0xFF])  # Send any byte to SS pin

# Close SPI bus
spi.close()
