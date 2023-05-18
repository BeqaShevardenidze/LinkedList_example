import os
import random

def Cls():
    os.system("cls")
Cls()
print("""
{1} -  linkd list პირველი ეტაპი, ინიციალიზაცია
---------------------------------------------------------------
{2} -  linkd list მეორე ეტაპი, შემოგვაქვს მეორე კლასი LinkedList
{3} -  მეორე ეტაპის გარჩევა, ხელით დამატება ელემენტების Node-ში
        კითხვა: რას ნიშნავს class '__main__.Node',
                სტრუქტურულად როგორ ამატებს ერთ ელემენტს მეორეს
{4} -  მეორე ეტაპის გარჩევა, ელემენტების ციკლით დამატება Node-ში
{5} -  მეორე ეტაპის გარჩევა, ელემენტების random-ით დამატება Node-ში
---------------------------------------------------------------
{6} -  მეორე ეტაპის გარჩევა, მეორე კლასის დამატებით (დამატემა სათითაო ელემენტებით)
{7} -  მეორე ეტაპის გარჩევა, მეორე კლასის დამატებით (ელემენტების დამატება ციკლით)
{8} -  მეორე ეტაპის გარჩევა, მეორე კლასის დამატებით (ელემენტების დამატება random-ით)330-ზე მეტ ელემენტს ვერ ბეჭდავს
        კითხვა: როგორ შევინახო 330-ზე მეტი ელემენტი?
---------------------------------------------------------------
{9} -  linked list-ის ზომის გაგება
{10} -  linked list-ის ზომის გაგება temp ელემენტის გარეშე
        კითხვა: head-ს საიდან გადაეცემა next-ი?
---------------------------------------------------------------
{11} - linked list-ის შემოტრიალება, მრავალჯერ გამოძახება. init() ფუნქცია
---------------------------------------------------------------
{12} - linked list-ის შემოტრიალება, leet code
---------------------------------------------------------------
{13} - linked list-ის პირველი 5 ელემენტის გამოტანა

----------------------------Append----------------------------
{14} - linked list append
{15} - linked list append for Loop
{16} - linked list append for Loop random

----------------------------Insert----------------------------
{17} - linked list inser if index == 0
{18} - linked list inser if index == length + 1
{19} - linked list inser if 0 < index < length + 1
""")

x = input(">>>> ")
match x:
    case '1':
        Cls()
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

            def __str__(self):
                return f"[{self.data}]->{self.next}"
            
        # n1 ობიექტის ინიციალიზაცია
        n1 = Node(10)
        print(f"n1 = {n1}")

        # -------------------------------------------------------
        # n2 ობიექტის ინიციალიზაცია
        n2 = Node(15)
        print(f"n2 = {n2}")

        # n1 - ის next ელემენტის და n2 ობიექტის მიბმა n1-ში
        n1.next = n2
        print(f"n1.next + n2 = {n1}")

        # -------------------------------------------------------
        # n3 ობიექტის ინიციალიზაცია
        n3 = Node(20)
        print(f"n3 = {n3}")

        # n1 - ის next ელემენტის და n3 ობიექტის მიბმა n1-ში
        n1.next = n3
        print(f"n1 next + n3 = {n1}")    #n1 -ის next ელემენტს (n2) გადაეწერა n3 - ის მნიშვნელობა


# ///////////////////////////////////////////////////////
    case '2':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"


        class LinkedList:
            def __init__(self) -> None:
                self.head = None

            def __str__(self) -> str:
                return str(self.head)
            
        
        # ---------------------------------------
        linked_list = LinkedList()  # linked_list-ს მივანიჭეთ LinkedList() კლასი
        temp = Node(1)      #temp -ს მივანიჭეთ Node(1) კლასის მნიშვნელობა - temp = 1
        linked_list.head = temp     #linked_list-ის head მივანიჭეთ temp-ის მნიშვნელობა ანუ 1
        for i in range(2, 5):       # ციკლში i = ორიდან ხუთამდე ელემენტებს
            temp.next = Node(i)     #temp-ის next ელემენტს ვანიჭებთ Node(i) კლასის მნიშვნელობებს ანუ 2 დან 5მდე ელემენტებს
            temp = temp.next        #temp ცვლადს ვანიჭებთ temp.next-ის მნიშვნელობებს 

        print(linked_list)


# ///////////////////////////////////////////////////////
    case '3':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        n1.next = n2
        n2.next = n3

        print(n1)
        print(type(n1.data))
        print(type(n1))


# ///////////////////////////////////////////////////////
    case '4':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        my_node = Node(0)     #my_node-ს გადაეცემა Node(0) ის მნიშვნელობა ანუ 0 
        temp = Node(1)      
        my_node.next = temp
        for i in range(2, 10):
            temp.next = Node(i)
            temp = temp.next
            print(temp)

        print(my_node)


# ///////////////////////////////////////////////////////
    case '5':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
        
        my_node = Node(random.randint(1, 101))
        temp = Node(random.randint(1, 101))
        my_node.next = temp

        for i in range(10):
            temp.next = Node(random.randint(1, 101))
            temp = temp.next

        print(my_node)

# ///////////////////////////////////////////////////////
    case '6':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self) -> None:
                self.head = None

            def __str__(self) -> str:
                return str(self.head)
            
        linked_list = LinkedList()
        my_node1 = Node(0)
        my_node2 = Node(1)
        my_node3 = Node(2)

        my_node1.next = my_node2
        my_node2.next = my_node3


        linked_list.head = my_node1     #linked_list -ის პირველი ელემენტი ხდება linked_list.head მნიშვნელობით my_node1 ანუ 0-ანი


        print(linked_list)


# ///////////////////////////////////////////////////////
    case '7':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self) -> None:
                self.head = None

            def __str__(self) -> str:
                return str(self.head)
            
        linked_list = LinkedList()
        temp = Node(0)
        linked_list.head = temp

        for i in range(1, 10):
            temp.next = Node(i)
            temp = temp.next

        print(linked_list)


# ///////////////////////////////////////////////////////
    case '8':
        Cls()
        class Node:
            def __init__(self,data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self) -> None:
                self.head = None

            def __str__(self) -> str:
                return str(self.head)
            
        linked_list = LinkedList()
        temp = Node(random.randint(0, 101))

        linked_list.head = temp

        for i in range(330):
            temp.next = Node(random.randint(0,101))
            temp = temp.next

        print(linked_list)


# ///////////////////////////////////////////////////////
    case '9':
        Cls()
        class Node:
            def __init__(self,data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self) -> None:
                self.head = None

            def __str__(self) -> str:
                return str(self.head)
            
            # temp-ს ვანიჭებთ self.head
            # სანამ temp არ უდრის None-ს მანამდე სრულდება while ციკლი
            # while ციკლში temp-ს ვანიჭებთ temp.next ელემენტს  (ანუ temp-ის მომდევნო ელემენტის მნიშვნელობას და სანამ None არ შეხვდება მანამდე სტულდება while ციკლი)
            def length(self):
                count = 0 
                temp = self.head
                while temp is not None:
                    count += 1
                    temp = temp.next
                return count
            

        linked_list = LinkedList()
        temp = Node(1)
        temp2 = Node(2)
        temp3 = Node(3)
        
        linked_list.head = temp
        temp.next = temp2
        temp2.next = temp3

        print(linked_list)
        print(linked_list.length())


# ///////////////////////////////////////////////////////
    case '10':
        Cls()
        class Node:
            def __init__(self,data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self) -> None:
                self.head = None
            
            def __str__(self) -> str:
                return str(self.head)
            
            def length(self):
                count = 0
                while self.head:
                    count += 1
                    self.head = self.head.next
                return count
            

        linked_list = LinkedList()
        temp = Node(1)
        temp2 = Node(2)
        temp3 = Node(3)
        
        linked_list.head = temp
        temp.next = temp2
        temp2.next = temp3

        print(linked_list)
        print(linked_list.length())
        print(linked_list.length())


# ///////////////////////////////////////////////////////
    case '11':
        Cls()
        class Node:
            def __init__(self,data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self) -> None:
                self.head = None
            
            def __str__(self) -> str:
                return str(self.head)
            
            def length(self):
                count = 0
                while self.head:
                    count += 1
                    self.head = self.head.next
                return f"linked list length = {count} element"
            
            def init(self):
                linked_list = LinkedList()
                temp = Node(0)
                linked_list.head = temp
                for i in range(1, 11):
                    temp.next = Node(i)
                    temp = temp.next
                return linked_list
            
        linked_list = LinkedList()

        print(linked_list.init())
        print(linked_list.init())
        print(linked_list.init())
        print(linked_list.init())


# ///////////////////////////////////////////////////////
    case '12':
        Cls()
        class ListNode:
            def __init__(self, val = 0, next=None) -> None:
                self.val = val
                self.next = next

            def __str__(self) -> str:
                return f"[{self.val}]->{self.next}"

        class Solution:
            def reverseList(self, head: ListNode) -> ListNode:
                if not head:
                    return head
                
                temp = head
                tail = ListNode(val=head.val)
                while temp.next:
                    temp = temp.next
                    tail = ListNode(val=temp.val, next=tail)
                return tail
            
        
        listnode_1 = ListNode(1)
        listnode_2 = ListNode(2)
        listnode_3 = ListNode(3)
        listnode_4 = ListNode(4)
        listnode_5 = ListNode(5)

        listnode_1.next = listnode_2
        listnode_2.next = listnode_3
        listnode_3.next = listnode_4
        listnode_4.next = listnode_5

        linkedlist1 = Solution()

        print(listnode_1)
        print(linkedlist1.reverseList(listnode_1))


# ///////////////////////////////////////////////////////
    case '13':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self) -> None:
                self.head = None
            
            def __str__(self) -> str:
                return str(self.head)
            
            def length(self):
                count = 0
                while self.head:
                    count+=1
                    self.head = self.head.next
                return count
                
            def creat(self):
                linked_list = LinkedList()
                node = Node(0)
                linked_list.head = node
                for i in range(1, 11):
                    node.next = Node(i)
                    node = node.next
                return linked_list

            def create_rand(self):
                linked_list = LinkedList()
                node = Node(random.randint(0,101))
                linked_list.head = node
                for i in range(0,10):
                    node.next = Node(random.randint(0,101))
                    node = node.next
                return linked_list
            
            def f_node(self):
                node0 = Node(0)
                node1 = Node(1)
                node2 = Node(2)
                node3 = Node(3)
                node4 = Node(4)

                node0.next = node1
                node1.next = node2
                node2.next = node3
                node3.next = node4

                return node0
            
        node_head = LinkedList().f_node()

        position = 1

        while node_head is not None:
            if position == 4:
                element = node_head.next
                print(element)
                break
            node_head == node_head.next
            position+=1


# ///////////////////////////////////////////////////////
    case '14':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                return f"[{self.data}]->{self.next}"
            
        class LinkedList:
            def __init__(self, value) -> None:
                self.head = Node(value)

            def append(self,value):
                current_node = self.head
                while current_node.next:
                    current_node = self.head.next
                new_node = Node(value)
                current_node.next = new_node

            def __str__(self) -> str:
                return str(self.head)
            
        linked_list = LinkedList(0)
        linked_list.append(1)
        linked_list.append(2)
        print(linked_list)


# ///////////////////////////////////////////////////////
    case '15':
        Cls()
        class Node:
            def __init__(self,data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                if self.next:
                    return f"[{self.data}]->{self.next}"
                else:
                    return f"[{self.data}]"

            
        class LinkedList:
            def __init__(self,value) -> None:
                self.head = Node(value)

            def append(self, value):
                carrent_node = self.head
                while carrent_node.next:
                    carrent_node = carrent_node.next
                new_node = Node(value)
                carrent_node.next = new_node

            def forLoop(self,index):
                linked_list = LinkedList(1)
                for i in range(2,index):
                    linked_list.append(i)
                return linked_list

            def __str__(self, ) -> str:
                return str(self.head)
            
        linked_list = LinkedList(0)
        new_list = linked_list.forLoop(11)
        print(new_list)


# ///////////////////////////////////////////////////////
    case '16':
        Cls()
        class Node:
            def __init__(self,data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                if self.next:
                    return f"[{self.data}]->{self.next}"
                else:
                    return f"[{self.data}]"
                
        class LinkedList:
            def __init__(self,value) -> None:
                self.head = Node(value)

            def append(self, value):
                carrent_node = self.head
                while carrent_node.next:
                    carrent_node = carrent_node.next
                new_node = Node(value)
                carrent_node.next = new_node

            def forLoop(self,index):
                linked_list = LinkedList(1)
                for i in range(2,index):
                    linked_list.append(i)
                return linked_list

            def for_rand(self,):
                linked_list = LinkedList(random.randint(0,101))
                for i in range(10):
                    linked_list.append(random.randint(0,101))
                return linked_list

            def __str__(self) -> str:
                return str(self.head)
            
        linked_list = LinkedList(0).for_rand()
        print(linked_list); print()


# ///////////////////////////////////////////////////////
    case '17':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

            def __str__(self) -> str:
                if self.next is not None:
                    return f"[{self.data}]->{self.next}"
                else:
                    return f"[{self.data}]"
                
        class LinkedList:
            def __init__(self, value) -> None:
                self.head = Node(value)
                self.length = 1

            def append(self, value):
                current_node = self.head
                while current_node.next:
                    current_node = current_node.next
                new_node = Node(value)
                current_node.next = new_node
                self.length += 1

            def insert(self, index, value):
                if index == 0:
                    temp = self.head
                    self.head = Node(value)
                    self.head.next = temp
                    self.length += 1


            def __str__(self) -> str:
                return str(self.head)
                
        
        node = LinkedList(0)
        node.append(1)
        node.append(2)
        node.append(3)

        node.insert(0,-1)

        print(node)
        print(node.length)


# ///////////////////////////////////////////////////////
    case '18':
        Cls()
        class Node:
            def __init__(self, data) -> None:
                self.data = data
                self.next = None

        class LinkedList:
            def __init__(self, value) -> None:
                self.head = Node(value)
                self.length = 1

            def append(self,value):
                current_node = self.head
                while current_node.next:
                    current_node = current_node.next
                current_node.next = Node(value)
                self.length += 1

            def insert(self, index, value):
                last_index = self.length - 1
                if index == 0:
                    current_node = self.head
                    self.head = Node(value)
                    self.head.next = current_node
                    self.length += 1
                elif index == last_index + 1:
                    self.append(value)

            def printList(self):
                current_node = self.head
                print(current_node.data)
                while current_node.next:
                    current_node = current_node.next
                    print(current_node.data)

        
        my_list = LinkedList(3)
        my_list.append("a")
        my_list.insert(0,-1)
        my_list.insert(3,"b")
        my_list.printList()
        print("length = ",my_list.length)


# ///////////////////////////////////////////////////////
    case '19':
        Cls()
        class Node:
            def __init__(self,data) -> None:
                self.data = data
                self.next = None

        class LinkedList:
            def __init__(self, value) -> None:
                self.head = Node(value)

            def append(self, value):
                current_node = self.head
                while current_node.next:
                    current_node = current_node.next
                current_node.next = Node(value)

            def printList(self):
                current_node = self.head
                print(current_node.data)
                while current_node.next:
                    current_node = current_node.next
                    print(current_node.data)

        my_list = LinkedList(1)
        my_list.append(100)
        my_list.printList()            