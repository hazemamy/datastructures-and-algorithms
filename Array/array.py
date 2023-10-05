import ctypes


class Array:
    def __init__(self, size):
        self.size = size
        self._capacity = max(16, 2 * size)

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None

    def expand_capacity(self):
        self._capacity *= 2
        print(f"Expand capacity to {self._capacity}")

        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):
            new_memory[i] = self.memory[i]

        del self.memory
        self.memory = new_memory

    def append(self, item):
        if self.size == self._capacity:
            self.expand_capacity()
        self.memory[self.size] = item
        self.size += 1

    def insert(self, idx, item):
        assert 0 <= idx < self.size

        if self.size == self._capacity:
            self.expand_capacity()

        for p in range(self.size - 1, idx - 1, -1):
            self.memory[p + 1] = self.memory[p]
        self.memory[idx] = item
        self.size += 1

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ""
        for i in range(self.size):
            result += str(self.memory[i]) + ", "
        return result


if __name__ == "__main__":
    array = Array(0)
    array.append(56)
    array.append("hello")
    print(array)

    array.insert(0, "A0")
    print(array)

    array.insert(2, "A2")
    print(array)

    array.insert(1, -9)
    print(array)
