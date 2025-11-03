from dataclasses import dataclass

@dataclass
class Block:
    offset: int
    size: int
    next: int | None
    prev: int | None


@dataclass
class Heap:
    blocks: dict[int, Block]
    free_map: dict[int, int]
    size: int
    max_size: int

    def malloc(self, size: int) -> int:
        # find first blocks where we can fit size
        free_block: Block | None = None

        for free_block_offset, free_size in sorted(self.free_map.items()):
            if free_size >= size:
                free_block = self.blocks[free_block_offset]
                break

        if free_block:
            del self.free_map[free_block.offset]

            if free_block.size == size:
                return free_block.offset

            # split the block into two

            # Create two new blocks: left (unallocated), right(allocated)
            left_block = Block(offset=free_block.offset, size=size, next=None, prev=None)
            right_block = Block(offset=free_block.offset + size, size=free_block.size - size, next=None, prev=None)

            # Insert the left block into self.blocks
            self.blocks[left_block.offset] = left_block
            # Insert the right block into self.blocks
            self.blocks[right_block.offset] = right_block

            # Point left to the right block and vice verse
            left_block.next = right_block.offset
            right_block.prev = left_block.offset

            # Point right to the next and vice versa
            right_block.next = free_block.next
            if free_block.next:
                self.blocks[free_block.next].prev = right_block.offset

            # Point left block to the prev block (prev already points to the left)
            left_block.prev = free_block.prev
            if free_block.prev:
                self.blocks[free_block.prev].next = left_block.offset

            # Insert the right block into the free list
            self.free_map[right_block.offset] = right_block.size

            return free_block.offset

        # if not found, bump break and try again
        self.brk(self.size + size)
        return self.malloc(size)

    def merge_with_the_next(self, offset: int) -> None:
        block = self.blocks[offset]
        next_block = self.blocks[block.next]
        next_next_block = self.blocks[next_block.next]

        block.next = next_next_block.offset
        next_next_block.prev = block.offset
        block.size += next_block.size

        del self.free_map[next_block.offset]
        self.free_map[block.offset] = block.size

    def free(self, ptr: int) -> int:
        # validate the ptr in the free list and in the block list
        if ptr in self.free_map:
            raise ValueError("double free")

        if ptr not in self.blocks:
            raise ValueError("invalid address")

        block = self.blocks[ptr]
        block_size = block.size

        self.free_map[ptr] = block_size

        # Merge new free block with adjacent free blocks if any

        if block.next and block.next in self.free_map:
            self.merge_with_the_next(block.offset)

        if block.prev and block.prev in self.free_map:
            self.merge_with_the_next(block.prev)

        return block_size

    def brk(self, new_size: int) -> None:
        if new_size > self.max_size:
            raise ValueError("out of memory")

        old_size = self.size
        self.size = new_size

        # Move dummy block to a new size
        dummy_block = self.blocks[old_size]
        prev_block = self.blocks[dummy_block.prev]

        dummy_block.offset = new_size
        del self.blocks[old_size]
        self.blocks[new_size] = dummy_block

        if prev_block.offset in self.free_map:
            # If the last block is free - extend it
            prev_block.size = new_size - prev_block.offset
        else:
            # If not insert a new free block in the end
            new_block = Block(offset=old_size, size=new_size - old_size, prev=None, next = None)
            new_block.prev = prev_block.offset
            new_block.next = new_size
            dummy_block.prev = old_size


class Allocator:
    heap: Heap
    allocations: dict[int, list[int]]

    def __init__(self, n: int):
        self.heap = Heap(
            size=n, max_size=n, blocks={
                0: Block(size=n, offset=0, next=n, prev=None),
                n: Block(size=0, offset=n, next=None, prev=0),
            },
            free_map={0: n},
        )
        self.allocations = {}

    def allocate(self, size: int, mID: int) -> int:
        try:
            ptr = self.heap.malloc(size)
            if mID in self.allocations:
                self.allocations[mID].append(ptr)
            else:
                self.allocations[mID] = [ptr]

            return ptr
        except:
            return -1
        

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for ptr in self.allocations.pop(mID, []):
            try:
                freed += self.heap.free(ptr)
            except:
                pass

        return freed
