class Node:
    def __init__(self,data):
         self.data = data;
         self.next = None;
         
class Stack:
    def __init__(self) -> None:
        self.top = None;
        self.size = 0;

    def isEmpty(self):
        stringPiha = "Pilha não está vazia";
        if self.items == []:
            print("Pilha vazia")    
            return self.items == [];
        else:
            return stringPiha;
    def push(self, node):
        node.next = self.top;
        self.top = node;
        self.size += 1;

    def pop(self):
        if self.size > 0:
            node = self.top;
            self.top = node.next;
            self.size -= 1;
        else:
            print("Stack is empty")
        
    def peek(self):
        if self.top != None:
            return self.top.data;
        else:
            return "The stack is empty"
        
    def stackSize(self):
        return self.size;
    
    def __str__(self) -> str:
        if self.top != None:
            node = self.top;
            stack_node_list = []
            while node != None:
                stack_node_list.append(node.data);
                node = node.next;
            return "\n".join(stack_node_list);
        else:
            return "Stack is empty";

            
book1 = Node("Book_01");
book2 = Node("Book_02");
book3 = Node("Book_03");
file = Node("File")

stack = Stack();
stack.push(book1);
stack.push(book2);
stack.push(file);

print("\nToda os elementos da Pilha:");
print(stack);
print("\nImprime top da Pilha:");
print(stack.peek());
stack.pop();
print("\nImprime top da Pilha:");
print(stack.peek());
print("\nTamanho da Pilha");
print(stack.stackSize());