def find_pile(prefix_sum_list, worm_label):
    left, right = 0, len(prefix_sum_list)-1
    while left < right:
        mid = (left + right) // 2
        if worm_label <= prefix_sum_list[mid]:
            right = mid
        else:
            left = mid + 1
    return left + 1     # AS `left` is index, so `position` will be `index+1`

def main():
    no_of_piles = int(input())
    piles_list = list(map(int, input().split()))
    no_of_juicy_worms = int(input())
    juicy_worms_labels = list(map(int, input().split()))

    # Calculate the prefix sum list
    prefix_sum_list = [0] * no_of_piles
    prefix_sum_list[0] = piles_list[0]
    for i in range(1, no_of_piles):
        prefix_sum_list[i] = prefix_sum_list[i - 1] + piles_list[i]

    for worm_label in juicy_worms_labels:
        in_which_pile = find_pile(prefix_sum_list, worm_label)
        print(in_which_pile)

if __name__ == "__main__":
    main()
