class Inventory:

    def __init__(
        self,
        inventory_id,
        comic_id,
        action_type,   # IMPORT / EXPORT / MOVE
        quantity,
        note,
        created_at=None
    ):

        self.inventory_id = inventory_id
        self.comic_id = comic_id
        self.action_type = action_type
        self.quantity = quantity
        self.note = note
        self.created_at = created_at

    def __str__(self):

        return (
            f"\nInventory ID: {self.inventory_id}"
            f"\nComic ID: {self.comic_id}"
            f"\nAction: {self.action_type}"
            f"\nQuantity: {self.quantity}"
            f"\nNote: {self.note}"
            f"\nCreated: {self.created_at}"
        )