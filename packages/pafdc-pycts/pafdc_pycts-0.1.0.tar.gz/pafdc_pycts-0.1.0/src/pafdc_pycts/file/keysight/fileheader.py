import numpy as np

class FileHeader:
    def __init__(self, buffer, offset=0):
        self.offset = offset
        self.file_cookie = np.frombuffer(buffer, dtype='S2', count=1, offset=self.offset).astype(str)[0]
        self.offset += 2
        self.file_version = np.frombuffer(buffer, dtype='S2', count=1, offset=self.offset).astype(str)[0]
        self.offset += 2
        self.file_size = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
        self.waveform_count = np.frombuffer(buffer, dtype='int32', count=1, offset=self.offset).astype(np.int32)[0]
        self.offset += 4
