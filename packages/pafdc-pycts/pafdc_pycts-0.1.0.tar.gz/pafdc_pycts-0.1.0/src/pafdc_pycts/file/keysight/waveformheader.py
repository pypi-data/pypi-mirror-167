
class WaveformHeader:
    def __init__(self, buffer, offset=0):
        self.offset = offset
        self.header_size = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.waveform_type = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.waveform_buffers = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.points = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.count = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.x_display_range = np.frombuffer(buffer, dtype='float32', count=1, offset=self.offset).astype(np.float32)[0]
        self.offset += 4
        self.x_display_origin = np.frombuffer(buffer, dtype='float64', count=1, offset=self.offset).astype(np.float64)[0]
        self.offset += 8
        self.x_increment = np.frombuffer(buffer, dtype='float64', count=1, offset=self.offset).astype(np.float64)[0]
        self.offset += 8
        self.x_origin = np.frombuffer(buffer, dtype='float64', count=1, offset=self.offset).astype(np.float64)[0]
        self.offset += 8
        self.x_units = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.y_units = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.date_string = np.frombuffer(buffer, dtype='S16', count=1, offset=self.offset).astype(str)[0]
        self.offset += 16
        self.time_string = np.frombuffer(buffer, dtype='S16', count=1, offset=self.offset).astype(str)[0]
        self.offset += 16
        self.frame_string = np.frombuffer(buffer, dtype='S24', count=1, offset=self.offset).astype(str)[0]
        self.offset += 24
        self.waveform_string = np.frombuffer(buffer, dtype='S16', count=1, offset=self.offset).astype(str)[0]
        self.offset += 16
        self.time_tag = np.frombuffer(buffer, dtype='float64', count=1, offset=self.offset).astype(np.float64)[0]
        self.offset += 8
        self.segment_index = np.frombuffer(buffer, dtype='uint32', count=1, offset=self.offset).astype(np.uint32)[0]
        self.offset += 4
        self.offset = self.header_size + offset

        self.time = np.linspace(0, self.x_display_range, self.points, endpoint=False) - self.x_origin
