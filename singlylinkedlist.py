class Listnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.node_id = None

class singleLinkedList:


    def __init__(self):
        self.head = None
        self.tail = None


    def add_list_item(self,item):
            node_idd = 0
            if not isinstance(item,Listnode):
                item = Listnode(item)
            if self.head == None:
                self.head = item
                node_idd = node_idd + 1
            else:
                self.tail.next = item
                node_idd = self.tail.node_id + 1
            self.tail = item
            self.tail.node_id = node_idd
            return
    def rem_item(self,node_id):
        current_node = self.head
        current_id = 1
        flag = 0
        previous_node = None
        while current_node is not None:
            if current_id == node_id:
                if previous_node == None:
                    self.head = current_node.next
                    print("Removing node - >",node_id)
                    flag = flag + 1
                else:
                    previous_node.next=current_node.next
                    print("Removing node - >",node_id)
                    flag = flag + 1
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        if flag == 0:
            print("Unknown Node")
        return

    def list_count(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def view_all_elements(self):
        current_node = self.head
        count = 1
        while current_node is not None:
            print ("%s item is :%s"%(count,current_node.data))
            current_node = current_node.next
            count = count + 1
        return
    def search_by_data(self,data):
        current_node = self.head
        flag = 0
        while current_node is not None:
            if current_node.data == data:
                print("Node ID for searched node is:%s with data : %s"%(current_node.node_id,current_node.data))
                flag = flag +1
            current_node = current_node.next
        if flag == 0:
            print("No data found")
        return

def main():
    print("Hello! This is a linked list demo")
    node1 = Listnode(input("Enter the first value:"))
    node2 = Listnode(input("Enter the second value"))
    node3 = Listnode(input("Enter the 3 value:"))
    node4 = Listnode(input("Enter the 4 value"))
    node5 = Listnode(input("Enter the 5 value:"))
    node6 = Listnode(input("Enter the 6 value"))

    thelist = singleLinkedList()
    thelist.add_list_item(node1)
    thelist.add_list_item(node2)
    thelist.add_list_item(node3)
    thelist.add_list_item(node4)
    thelist.add_list_item(node5)
    thelist.add_list_item(node6)
    print("Value of node 1 and node 2",node1.data,node2.data)
    print("Node IDS are",node1.node_id,node2.node_id)
    print("The size of the list is: ",thelist.list_count())

    thelist.view_all_elements()
    data_value = input("Enter the data value you want to search for:")
    thelist.search_by_data(data_value)
    rem_id = input("Enter the node ID you want to remove")

    thelist.rem_item(rem_id)
    thelist.view_all_elements()
main()
