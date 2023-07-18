# Need to learn KMP algorithm and Bayer-Moore algorithm

# Rabin Karp Algorithm
class RollingHash:
    def __init__(self, string):
        self._hash = 0
        self._char_count = 0
        self._alphabet_size = 26
        for char in string:
            self.append(char)

    def _char_to_int(self, char):
        return ord(char) - ord("a") + 1
    
    def __eq__(self, value: "RollingHash") -> bool:
        return self._hash == value._hash

    def append(self, char):
        self._char_count += 1
        self._hash = self._hash * self._alphabet_size + self._char_to_int(char)

    def popleft(self, char):
        self._char_count -= 1
        self._hash -= self._char_to_int(char) * self._alphabet_size ** (self._char_count)


def find_substring(string, substring):
    sub_str_hash = RollingHash(substring)
    string_hash = RollingHash(string[:len(substring)])
    ind = len(substring) - 1

    while ind < len(string):
        if sub_str_hash == string_hash:
            return ind - len(substring) + 1
        ind += 1
        string_hash.popleft(string[ind - len(substring)])
        string_hash.append(string[ind])
    return -1


def main():
    string = "Hello world!"
    sub_string = "rld"
    print(find_substring(string=string, substring=sub_string))


if __name__ == "__main__":
    main()
