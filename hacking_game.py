"""
MemoryEditor Simulator (safe, educational)

This script simulates the behavior of a memory editor like the one described
in your article but works on a local bytearray that acts as "process memory".
You can:
 - populate the simulated memory with values
 - search for an integer value (32-bit unsigned, little-endian)
 - refine search results by checking the same addresses for a new value
 - replace values at found addresses

This is safe to run and is intended for learning and testing only.
"""

import struct
import random
import sys

class MemoryEditorSimulator:
    def __init__(self, size: int = 1024 * 1024):
        """Create a simulated memory buffer of `size` bytes (default 1 MB)."""
        self.memory = bytearray(size)
        self.base_address = 0x10000000  # just a fake base address for display
        self.size = size

    def write_u32(self, address_offset: int, value: int):
        """Write a 32-bit unsigned integer (little-endian) at offset."""
        if address_offset < 0 or address_offset + 4 > self.size:
            raise ValueError("Address out of range")
        self.memory[address_offset:address_offset+4] = struct.pack("<I", value)

    def read_u32(self, address_offset: int) -> int:
        """Read 32-bit unsigned int from offset."""
        if address_offset < 0 or address_offset + 4 > self.size:
            raise ValueError("Address out of range")
        return struct.unpack("<I", self.memory[address_offset:address_offset+4])[0]

    def populate_with_value(self, value: int, count: int):
        """Randomly scatter `count` occurrences of value across memory."""
        placed = 0
        tried = set()
        while placed < count:
            offset = random.randrange(0, self.size - 4)
            # avoid overwriting same spot repeatedly
            if offset in tried:
                continue
            tried.add(offset)
            self.write_u32(offset, value)
            placed += 1

    def fill_random(self):
        """Fill all memory with random bytes (to make the simulation realistic)."""
        for i in range(self.size):
            self.memory[i] = random.randrange(0, 256)

    def search_value(self, value: int) -> list:
        """
        Search the whole simulated memory for 4-byte little-endian occurrences
        of `value`. Returns a list of offsets (addresses relative to base).
        """
        search_bytes = struct.pack("<I", value)
        results = []
        # naive scan (byte-by-byte)
        i = 0
        limit = self.size - 4
        while i <= limit:
            if self.memory[i:i+4] == search_bytes:
                results.append(i)
                i += 4  # advance past the found value to avoid overlapping matches
            else:
                i += 1
        return results

    def search_next_value(self, addresses: list, next_value: int) -> list:
        """From a list of offsets, keep only those where the current 4 bytes == next_value."""
        search_bytes = struct.pack("<I", next_value)
        results = []
        for addr in addresses:
            if 0 <= addr <= self.size - 4:
                if self.memory[addr:addr+4] == search_bytes:
                    results.append(addr)
        return results

    def replace_value(self, addresses: list, new_value: int):
        """Replace the 4 bytes at each address with new_value."""
        b = struct.pack("<I", new_value)
        for addr in addresses:
            if 0 <= addr <= self.size - 4:
                self.memory[addr:addr+4] = b

    def display_addresses(self, addresses: list, limit: int = 10):
        """Pretty print addresses as hex (show first `limit` entries)."""
        print(f"Found {len(addresses)} addresses:")
        for i, addr in enumerate(addresses[:limit]):
            print(f"  {hex(self.base_address + addr)}  (offset {addr})")
        if len(addresses) > limit:
            print(f"  ...and {len(addresses) - limit} more")

def run_cli():
    mem = MemoryEditorSimulator(size=512 * 1024)  # 512 KB simulated memory
    print("MemoryEditor Simulator (safe demo)")
    print("Filling simulated memory with random bytes...")
    mem.fill_random()

    # Let's put some known values in memory so searches return hits:
    while True:
        try:
            initial_value = int(input("Enter an initial value to scatter (e.g. 12345): ").strip())
            break
        except ValueError:
            print("Please enter a valid integer.")
    while True:
        try:
            count = int(input("How many scattered occurrences to place (e.g. 20): ").strip())
            break
        except ValueError:
            print("Please enter a valid integer.")

    mem.populate_with_value(initial_value, count)
    print(f"Scattered {count} occurrences of {initial_value} in simulated memory.\n")

    # Main interactive loop
    found = mem.search_value(initial_value)
    mem.display_addresses(found)

    while True:
        print("\nOptions:")
        print("  1) refine search (enter new observed value)")
        print("  2) replace current found addresses with a new value")
        print("  3) show found addresses")
        print("  4) re-search the whole memory for a new initial value")
        print("  5) exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                nv = int(input("Enter the NEW observed value (to filter addresses): ").strip())
            except ValueError:
                print("Invalid integer.")
                continue
            found = mem.search_next_value(found, nv)
            print("After refinement:")
            mem.display_addresses(found)
        elif choice == "2":
            if not found:
                print("No addresses to replace.")
                continue
            try:
                rep = int(input("Enter the value to write at all found addresses: ").strip())
            except ValueError:
                print("Invalid integer.")
                continue
            mem.replace_value(found, rep)
            print(f"Wrote {rep} to all {len(found)} addresses.")
        elif choice == "3":
            mem.display_addresses(found, limit=50)
        elif choice == "4":
            try:
                new_init = int(input("Enter new initial value to search for: ").strip())
            except ValueError:
                print("Invalid integer.")
                continue
            found = mem.search_value(new_init)
            mem.display_addresses(found)
        elif choice == "5":
            print("Exiting simulator. Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    try:
        run_cli()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
