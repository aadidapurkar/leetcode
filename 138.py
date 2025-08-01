
#TODO doesnt work for LL with non unique node values -- idea fix by making key tuple of value + index
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        keyNodeValValIndexNode = {}
        indexCount = 1
        copyHead = Node(head.val)
        currPosOG = head.next
        currPosCopy = copyHead
        keyNodeValValIndexNode[currPosCopy.val] = (0, currPosCopy)

        # Copy the values of the og list (haven't copied random yet)
        while currPosOG is not None:
            currPosCopy.next = Node(currPosOG.val)
            currPosCopy = currPosCopy.next
            currPosOG = currPosOG.next

            keyNodeValValIndexNode[currPosCopy.val] = (indexCount, currPosCopy)
            indexCount += 1

        # Check deep copy
        #copiedList = self.convertList(copyHead)
        #print(copiedList)

        # Check map    
        for key, value in keyNodeValValIndexNode.items():
            print(f"Key: {key}, Value: {value}")
        
        # Copy random values from OG to copied
        currPosOG = head
        currIndex = 0
        while currPosOG is not None:
            if currPosOG.random:
                print(f"ogval {currPosOG.val}, ograndomval {currPosOG.random.val}")
                keyNodeValValIndexNode[currPosOG.val][1].random = keyNodeValValIndexNode[currPosOG.random.val][1]
            currPosOG = currPosOG.next

        # Check map    
        for key, value in keyNodeValValIndexNode.items():
            if value[1].random:
                print(f"Key: {key}, Value: {value[1].val}, Random: {value[1].random.val}")
            else:
                print(f"Key: {key}, Value: {value[1].val}, Random: {value[1].random}")

        return copyHead
    
    def convertList(self, head):
        list = []
        curr = head
        while curr is not None:
            #print(curr.val)
            if curr.random:
                list.append((curr.val,curr.random.val))
            else:
                list.append(curr.val)
            curr = curr.next
        return list

sol = Solution()
ll = Node(
    x = 1, 
    next = Node(
        x = 2, 
        next = Node(
            x = 3,
            next = Node(
                x = 4
                    )
                )
            ),
        ) 

ll.random = ll.next # Random of val 1 is 2
ll.next.random = ll.next.next.next # Random of val 2 is 4

ll2 = Node(
    x = 3,
    next = Node(
        x = 3,
        next = Node(
            x = 3
        ),
    )
)

ll2.next.random = ll2
#print(sol.convertList(ll))
res = sol.copyRandomList(ll2)
print(sol.convertList(res))