MAX_LEN_NUM = 3
MIN_RANGE = 0
MAX_RANGE = 255


def is_valid_range(range):
    return range and MIN_RANGE <= int(range) <= MAX_RANGE


def valid_ip_addresses(ip_address, k):
    valid_address = []
    def valid_ip_addresses_helper(curr_ip_address, k, curr_index):
        if k < 0:
            return
        if k == 0 and curr_index < len(ip_address):
            return
        if k == 0 and curr_index == len(ip_address):
            valid_address.append(curr_ip_address)
            return
        for i in range(curr_index, min(curr_index+3, len(ip_address))):
            curr_range = ip_address[curr_index : i + 1]
            if is_valid_range(curr_range):
                updated_ip_address = f"{curr_ip_address}.{curr_range}" if curr_ip_address else f"{curr_range}"
                valid_ip_addresses_helper(updated_ip_address, k - 1, i + 1)
    
    valid_ip_addresses_helper("", k, 0)
    return valid_address


def main():
    ip_address = "10503244"
    print(valid_ip_addresses(ip_address, 4))


if __name__ == "__main__":
    main()
