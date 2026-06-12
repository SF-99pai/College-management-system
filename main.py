from fastapi import FastAPI
from db.database import Base, engine

from models.user import User
from routers import users
from routers import students
from routers import role_permission
from routers import teachers
from routers import courses
from routers import classes
from routers import enrollment
from routers import grades
from routers import attendance
from routers import fee_payment



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="College System"
)

app.include_router(
    users.router
)
app.include_router(
    students.router
)
app.include_router(
    role_permission.router
)
app.include_router(
    teachers.router
)
app.include_router(
    courses.router
)

app.include_router(
    classes.router
)

app.include_router(
    enrollment.router
)

app.include_router(
    grades.router 
)

app.include_router(
    attendance.router   
)

app.include_router(
    fee_payment.router
)

