class Wave:
    def __init__(self, wave_num, row, num):
        self._wave_num = wave_num
        self._row = row
        self._num = num


    @property
    def wave_num(self):
        return self._wave_num

    @property
    def row(self):
        return self._row

    @property
    def num(self):
        return self._num

