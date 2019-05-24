class Solution:
    int_buf = [None] * 4
    int_ptr = 0
    int_bytes = 0

    def read4(self):
        if self.int_bytes == self.int_ptr:
            self.int_bytes = read4(self.int_buf)
            self.int_ptr = 0

    def read(self, buf, n):
        buf_pos = 0
        self.read4()

        while n - buf_pos > 0 and self.int_bytes > self.int_ptr:
            can_read = min(self.int_bytes - self.int_ptr, n - buf_pos)
            buf[buf_pos:buf_pos + can_read] = self.int_buf[self.int_ptr:self.int_ptr + can_read]

            buf_pos += can_read
            self.int_ptr += can_read

            self.read4()

        return buf_pos
