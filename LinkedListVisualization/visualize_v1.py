import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def get_nodes(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        return nodes

def update_graph(num, linked_list, ax):
    ax.clear()
    nodes = linked_list.get_nodes()
    
    # Adjust plot limits based on the number of nodes
    num_nodes = len(nodes)
    ax.set_xlim(0, max(15, 2 + num_nodes * 4))  # Ensure enough space for nodes
    ax.set_ylim(0, 2)
    ax.axis('off')

    x = 1
    for i, node in enumerate(nodes):
        # Draw node rectangle
        rect = patches.FancyBboxPatch((x, 0.5), 2, 0.5, boxstyle="round,pad=0.1", edgecolor='black', facecolor='lightblue')
        ax.add_patch(rect)
        # Add node value and address text with adjusted positions
        next_addr = hex(id(node.next)) if node.next else 'None'
        ax.text(x + 1, 0.75, f'Value: {node.value}', ha='center', va='center', fontsize=10)
        ax.text(x + 1, 0.55, f'Next: {next_addr}', ha='center', va='center', fontsize=8)
        # Draw arrow to next node
        if i < len(nodes) - 1:
            ax.annotate('', xy=(x + 3, 0.75), xytext=(x + 2, 0.75),
                        arrowprops=dict(arrowstyle='->', color='black'))
        x += 4

def animate(frame):
    if frame < len(values):
        linked_list.append(values[frame])
    update_graph(frame, linked_list, ax)

# Example data
values = [10, 20, 30, 40]
linked_list = LinkedList()

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=len(values) + 1, repeat=False, interval=1500)

plt.show()
