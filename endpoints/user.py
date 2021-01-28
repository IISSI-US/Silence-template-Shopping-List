from silence.decorators import endpoint
from silence.exceptions import HTTPError

@endpoint(
    route="/users",
    method="GET",
    sql="SELECT * FROM Users",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/users/$userId",
    method="GET",
    sql="SELECT * FROM Users WHERE userId = $userId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/users",
    method="POST",
    sql="INSERT INTO Users \
         (username, password, name, surnames) \
         VALUES \
         ($username, $password, $name, $surnames)"
)
def add(username, password, name, surnames):
    if not name or not surnames or not password or not username:
        raise HTTPError(400, "All fields are required")

###############################################################################

@endpoint(
    route="/users/$userId",
    method="PUT",
    sql="UPDATE Users SET username = $username, password = $password, \
         name = $name, surnames = $surnames, \
         WHERE userId = $userId"
)
def update(username, password, name, surnames):
    pass

###############################################################################

@endpoint(
    route="/users/$userId",
    method="DELETE",
    sql="DELETE FROM Users WHERE userId = $userId"
)
def delete():
    pass
