from openni import Device

device = Device.open_any()
depth_stream = device.create_depth_stream()
depth_stream.start()

frame = depth_stream.read_frame()
depth_data = frame.get_buffer_as_uint16()

depth_stream.stop()
depth_stream.destroy()
device.close()