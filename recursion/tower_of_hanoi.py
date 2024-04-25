from stacks_and_queues.stack_and_queue import Stack


def tower_of_hanoi(num_rings):
    result = []
    src_stack = Stack([i for i in range(num_rings, 0, -1)])
    dest_stack = Stack()
    aux_stack = Stack()
    def compute_steps(num_rings_to_move: int, _src_stack: Stack, _dest_stack: Stack, _aux_stack: Stack, _src, _dest, _aux):
        if num_rings_to_move > 0:
            compute_steps(num_rings_to_move - 1, _src_stack, _aux_stack, _dest_stack, _src, _aux, _dest)
            _dest_stack.push(_src_stack.pop())
            result.append((_src, _dest))
            compute_steps(num_rings_to_move - 1, _aux_stack, _dest_stack, _src_stack, _aux, _dest, _src)
    compute_steps(num_rings, src_stack, dest_stack, aux_stack, "source", "destination", "auxillary")
    return result


def tower_of_hanoi_iterative(num_rings):
    result = []
    src_stack = Stack([i for i in range(num_rings, 0, -1)])
    aux_stack = Stack()
    dest_stack = Stack()
    src, aux, dest = "source", "auxillary", "destination"
    def move_disk_bw_poles(src_stack: Stack, dest_stack: Stack, src_name, dest_name):
        src_disk = src_stack.peek()
        dest_disk = dest_stack.peek()

        if not src_disk or (dest_disk and src_disk > dest_disk):
            src_stack.push(dest_stack.pop())
            result.append((dest_name, src_name))
        elif not dest_disk or (src_disk and dest_disk > src_disk):
            dest_stack.push(src_stack.pop())
            result.append((src_name, dest_name))

    if num_rings % 2 == 0:
        aux, dest = dest, aux
    
    total_moves = 2 ** num_rings - 1

    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk_bw_poles(src_stack, dest_stack, src, dest)
        elif i % 3 == 2:
            move_disk_bw_poles(src_stack, aux_stack, src, aux)
        else:
            move_disk_bw_poles(dest_stack, aux_stack, dest, aux)
    return result


def operation_with_mandatory_aux(num_rings):
    """minimum number of operations subject to the constraint that each operation must 
    involve aux peg"""
    result = []
    src_stack = Stack([i for i in range(num_rings, 0, -1)])
    dest_stack = Stack()
    aux_stack = Stack()
    def compute_steps(num_rings_to_move: int, _src_stack: Stack, _dest_stack: Stack, _aux_stack: Stack, _src, _dest, _aux):
        if num_rings_to_move > 0:
            compute_steps(num_rings_to_move - 1, _src_stack, _dest_stack, _aux_stack, _src, _dest, _aux)
            _aux_stack.push(_src_stack.pop())
            result.append((_src, _aux))
            compute_steps(num_rings_to_move - 1, _src_stack, _dest_stack, _aux_stack, _src, _dest, _aux)
            _dest_stack.push(_aux_stack.pop())
            result.append((_aux, _dest))
            # compute_steps(num_rings_to_move - 1, _dest_stack, _aux_stack, _src_stack, _dest, _aux, _src)
            # compute_steps(num_rings_to_move - 1, _aux_stack, _src_stack, _dest_stack, _aux, _src, _dest)
            # compute_steps(num_rings_to_move - 1, _src_stack, _dest_stack, _aux_stack, _src, _dest, _aux)
    compute_steps(num_rings, src_stack, dest_stack, aux_stack, "source", "destination", "auxillary")
    return result


def clockwise_moves_only():
    """minimum number of operations subject to the constraint that each transfer must 
    be from src to dest, dest to aux, or aux to src"""
    pass


def direct_src_to_dest_not_allowed():
    """minimum number of operations subject to the constraint that a ring can never be 
    transferred directly from src to dest (transfers from dest to src are allowed)"""
    pass


def relaxed_constraints_but_largest_ring_must_be_lowest():
    """minimum number of operations when the stacking constraint is relaxed to the
    following-the largest ring on a peg must be the lowest ring on the peg. (The remaining rings on
    the peg can be in any order)"""
    pass


def double_disks():
    """You have 2n disks of n different sizes, two of each size. You cannot place a larger disk on a
    smaller disk, but can place a disk of equal size on top of the other. Compute the minimum number
    of moves to transfer the 2n disks from src to dest"""
    pass


def black_or_white_2n_disks():
    """You have 2n disks which are colored black or white. You cannot place a white disk directly
    on top of a black disk. Compute the minimum number of moves to transfer the 2n disks from src to
    dest"""
    pass


def four_pegs_available():
    """minimum number of operations if you have a fourth peg, aux2"""
    pass


def main():
    num_rings = 2
    # print(tower_of_hanoi(num_rings))
    # print(tower_of_hanoi_iterative(num_rings))
    print(operation_with_mandatory_aux(num_rings))


if __name__ == "__main__":
    main()


"""
s -> a
a -> d
s -> a
d -> a
a -> s
a -> d
s - > a
a -> d
"""