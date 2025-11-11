



def calculate_bitmask():
    try:
        micron_set_input = input("Enter the micron IDs as a comma-separated list (e.g., 0,87): ")
        micron_set = set(map(int, micron_set_input.split(","))) if micron_set_input else set()
        mic_bit_mask_byte_size = int(input("Enter the bitmask byte size (e.g., 11 or 30): "))

        max_micron_id = mic_bit_mask_byte_size * 8 - 1
        if any(micron_id < 0 or micron_id > max_micron_id for micron_id in micron_set):
            print(f"Error: Micron IDs must be in the range 0 to {max_micron_id}.")
            return

        micron_bit_mask = [0] * mic_bit_mask_byte_size
        for micron_id in micron_set:
            byte_index, bit_position = divmod(micron_id, 8)
            micron_bit_mask[byte_index] |= 1 << bit_position

        print(f"Calculated bitmask: {micron_bit_mask}")
        hex_string = ''.join(f'{byte:02X}' for byte in micron_bit_mask)
        print(f"Calculated bitmask (hex): {hex_string}")

    except ValueError:
        print("Error: Invalid input. Please enter integers only.")

if __name__ == "__main__":
    calculate_bitmask()