from silence.decorators import endpoint

@endpoint(
    route="/items",
    method="GET",
    sql="SELECT * FROM Items",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/items/$itemId",
    method="GET",
    sql="SELECT * FROM Items WHERE itemId = $itemId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/lists/$listId/items/unpurchased",
    method="GET",
    sql="SELECT * FROM Items WHERE listId = $listId AND purchased = 0",
    description = "Retrieves the items belonging to the specified list that haven't been purchased yet.",
    auth_required=True
)
def get_unpurchased_by_list():
    pass

###############################################################################

@endpoint(
    route="/lists/$listId/items/purchased",
    method="GET",
    sql="SELECT * FROM Items WHERE listId = $listId AND purchased = 1",
    description = "Retrieves the items belonging to the specified list that have been purchased",
    auth_required=True
)
def get_purchased_by_list():
    pass

###############################################################################

@endpoint(
    route="/items",
    method="POST",
    sql="INSERT INTO Items (name,quantity,purchased,listId)\
         VALUES ($name,$quantity,$purchased,$listId)",
    auth_required=True
)
def add(name, quantity, purchased, listId):
    pass

###############################################################################

@endpoint(
    route="/items/$itemId",
    method="PUT",
    sql="UPDATE Items SET name = $name, quantity = $quantity, purchased = $purchased, listId = $listId WHERE itemId = $itemId",
    auth_required=True
)
def update(name, quantity, purchased, listId):
    pass

###############################################################################

@endpoint(
    route="/items/$itemId/increase",
    method="PUT",
    sql="UPDATE Items SET quantity = quantity + 1 WHERE itemId = $itemId",
    #auth_required=True
)
def upQuantity():
    pass

###############################################################################

@endpoint(
    route="/items/$itemId/decrease",
    method="PUT",
    sql="UPDATE Items SET quantity = quantity - 1 WHERE itemId = $itemId",
    #auth_required=True
)
def downQuantity():
    pass

###############################################################################

@endpoint(
    route="/items/$itemId/purchase",
    method="PUT",
    sql="UPDATE Items SET purchased = 1 WHERE itemId = $itemId",
    #auth_required=True
)
def purchase():
    pass

###############################################################################

@endpoint(
    route="/items/$itemId",
    method="DELETE",
    sql="DELETE FROM Items WHERE itemId = $itemId",
    auth_required=True
)
def delete():
    pass
