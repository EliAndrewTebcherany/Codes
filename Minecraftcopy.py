import random
from ursina import *  # type: ignore
from ursina.prefabs.first_person_controller import FirstPersonController  # type: ignore

window.windowed_size = (1570, 900)
app = Ursina()  # type: ignore
player = FirstPersonController()
Sky()  # type: ignore

boxes = []
doors = []

for i in range(50):
    for j in range(50):
        box = Button(color=color.white, model='cube', position=(j, 0, i), texture='Texture/grass.png', parent=scene, origin_y=0.5)  # type: ignore
        boxes.append(box)
        box2 = Button(color=color.white, model='cube', position=(j, -1, i), texture='Texture/nat_stone.png', parent=scene, origin_y=0.5)  # type: ignore
        boxes.append(box2)

selected_block_type = None  # Variable to store the selected block type

def input(key):
    global selected_block_type  # Use the global variable
    for box in boxes:
        if box.hovered:
            if key == '2':
                selected_block_type = 'grass'
            elif key == '1':
                selected_block_type = 'wood'
            elif key == '3':
                selected_block_type = 'leaf'
            elif key == '4':
                selected_block_type = 'plank'
            elif key == '5':
                selected_block_type = 'stone'
            elif key == '6':
                selected_block_type = 'iron'
            elif key == '7':
                selected_block_type = 'gold'
            if key == 'left mouse down':
                boxes.remove(box)
                destroy(box)
            if key == 'right mouse down':
                 if selected_block_type:
                    # Create a new block of the selected type at the hovered block's position
                    new = Button(color=color.white, model='cube', position=box.position + mouse.normal, texture=f'Texture/{selected_block_type}.png', parent=scene, origin_y=0.5)
                    boxes.append(new)


def generate_tree():
    for _ in range(20):
        x = random.randint(4, 46)
        z = random.randint(4, 46)
        tree_height = random.randint(5, 7)  # Random tree height (3 to 10)
        print(f"Generated tree coordinates: x={x}, tree_height={tree_height}, z={z}")
        # Create the wooden trunk
        for y in range(tree_height):
            wood = Button(color=color.white, model='cube', position=(x, y, z), texture='Texture/wood.png', parent=scene, origin_y=0.5)  # type: ignore
            boxes.append(wood)
        # Add leaves (foliage) around the top of the tree
        for dx in range(-1, 2):  # Add leaves around the last log
            for dz in range(-1, 2):
                leaf = Button(color=color.white, model='cube', position=(x + dx, y + 1, z + dz), texture='Texture/leaf.png', parent=scene, origin_y=0.5)  # type: ignore

                boxes.append(leaf)
generate_tree()  # Call the tree generation function

class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.8, 0.1),  # Adjust the scale to fit your screen
            origin=(0.5, 0.5),  # Center the inventory
            position=(0, -0.4),  # Position it at the bottom center of the screen
            texture='white_cube',  # You can replace this with your own inventory background texture
            color=color.dark_gray
        )
        self.item_parent = Entity(parent=self, scale=(1 / 9, 1), position=(-0.4, 0))  # Adjust the scale for the number of slots

if __name__ == '__main__':
    inventory = Inventory()
    # Add placeholder items with textures
    inventory = Inventory()
    # Add placeholder items with textures (in order)
    item2 = Button(parent=inventory.item_parent, origin=(-0.5, 0.5), color=color.brown, position=(-5.5, 0), texture='Texture/wood - inventory.png')
    item1 = Button(parent=inventory.item_parent, origin=(-0.5, 0.5), color=color.green, position=(-4.5, 0), texture='Texture/grass - inventory.png')
    item3 = Button(parent=inventory.item_parent, origin=(-0.5, 0.5), color=color.white, position=(-3.5, 0), texture='Texture/leaf - inventory.png')
    item4 = Button(parent=inventory.item_parent, origin=(-0.5, 0.5), color=color.rgb(139, 69, 19), position=(-2.5, 0), texture='Texture/plank - inventory.png')
    item5 = Button(parent=inventory.item_parent, origin=(-0.5, 0.5), color=color.rgb(211, 211, 211), position=(-1.5, 0), texture='Texture/stone - inventory.png')
    item6 = Button(parent=inventory.item_parent, origin=(-0.5, 0.5), color=color.rgb(211, 211, 211), position=(-0.5, 0), texture='Texture/iron - inventory.png')
    item7 = Button(parent=inventory.item_parent, origin=(-0.5, 0.5), color=color.yellow, position=(0.5, 0), texture='Texture/gold - inventory.png')
    app.run()

