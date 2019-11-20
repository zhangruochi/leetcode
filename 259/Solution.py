def solution(array,target):
    count = 0
    array.sort()

    for i in range(len(array)-2):
        l = i+1
        r = len(array)-1


        while l < r:
            if array[l] + array[r] < target - array[i]:
                count += (r - l)
                l += 1
            else:
                r -= 1

    return count

if __name__ == '__main__':
    nums = [-2,0,1,3]
    print(solution(nums,2))
