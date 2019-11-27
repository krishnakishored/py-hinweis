# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    
    return sum([ 1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string])
    # count = 0
    # index = 0
    # while(index != -1):
    #    index = string.find(sub_string,index,len(string))
    #    if index != -1:
    #        index += 1
    #        count += 1
    # return count




if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)