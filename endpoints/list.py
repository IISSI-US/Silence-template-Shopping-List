from silence.decorators import endpoint

@endpoint(
    route="/lists",
    method="GET",
    sql="SELECT * FROM Lists",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/lists/$listId",
    method="GET",
    sql="SELECT * FROM Lists WHERE listId = $listId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/lists/user/$userId",
    method="GET",
    sql="SELECT * FROM Lists WHERE userId = $userId",
    description = "Retrieves the lists belonging to the specified user.",
    auth_required=True
)
def get_by_user():
    pass

###############################################################################

@endpoint(
    route="/lists",
    method="POST",
    sql="INSERT INTO Lists (name, userId)\
         VALUES ($name, $userId)",
    auth_required=True
)
def add(name, userId):
    if(len(name) < 5):
        raise HTTPError(400, "The list's name should be 5 or more characters long.")

###############################################################################

@endpoint(
    route="/lists/$listId",
    method="PUT",
    sql="UPDATE Lists SET name = $name, userId = $userId WHERE listId = $listId",
    auth_required=True
)
def update(name, userId):
    if(len(name) < 5):
        raise HTTPError(400, "The new name should be 5 or more characters long.")


###############################################################################

@endpoint(
    route="/lists/$listId",
    method="DELETE",
    sql="DELETE FROM Lists WHERE listId = $listId",
    auth_required=True
)
def delete():
    pass
