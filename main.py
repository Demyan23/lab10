import Node
import DoubleLinkedList
import Worker
node1 = Node.ListNode(Worker.Worker("Bob1", "High", "Programer", "2013", 4))
node2 = Node.ListNode(Worker.Worker("Bob2", "Mid", "Manager", "2013", 3))
node3 = Node.ListNode(Worker.Worker("Bob3", "Mid", "Programer", "2013", 5))
node4 = Node.ListNode(Worker.Worker("Bob4", "High", "Manager", "2013", 7))
node5 = Node.ListNode(Worker.Worker("Bob5", "High", "Programer", "2013", 4))
track = DoubleLinkedList.DoubleLinkedList()
for current_node in [node1, node2, node3, node4, node5]:
    track.insert_in_the_end(current_node)

print(track.unordered_search("Bob2"))
print(track.list_length())
track.output_list_forward()
head = track.insertionSort(track.head)
track.remove_list_item_by_id(3)
print("________")
track.output_list_forward()
