from sqlalchemy import create_engine

settings = [
    {"DATABASE_URL" : "mysql+pymysql://soncn:tranxuanson2k61810@localhost:3306/pc_shop"},
    {"DEBUG": True},
    {"pool_size": 10},
    {"max_overflow": 20},
    {"pool_pre_ping": True}
]

engine = create_engine(
    settings[0]['DATABASE_URL'],               # link kết nối database
    echo=settings[1]['DEBUG'],                 # log SQL ra terminal khi debug
    pool_size=settings[2]["pool_size"],        # số kết nối tối đa trong pool
    max_overflow=settings[3]["max_overflow"],  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings[4]["pool_pre_ping"] # kiểm tra kết nối trước mỗi lần dùng
)

# Base.metadata.create_all(bind=engine)
# print('Tạo bảng thành công')

#############################################################################################
# Thực hiện tạo bảng, ... học truy vấn ở đây, phần bên trên là kết nối database
#############################################################################################
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Departments(Base):
   __tablename__ = 'departments_sqlalchemy'
   dept_id=Column(Integer, autoincrement=True, primary_key=True)
   dept_name=Column(String(100), nullable=False)
   location=Column(String(255))

class Employees(Base):
   __tablename__ = 'employees_sqlalchemy'
   emp_id=Column(Integer, autoincrement=True, primary_key=True)
   emp_name=Column(String(100), nullable=False)
   dept_id=Column(
      Integer,
      ForeignKey(
         'departments_sqlalchemy.dept_id',
         ondelete='RESTRICT',
         onupdate='CASCADE'
      ),
      nullable=False
   )

# Tạo bảng khi bảng chưa tồn tại
Base.metadata.create_all(bind=engine)
print("Tạo bảng thành công")


# Chèn dữ liệu bằng Session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Thêm dữ liệu vào Departments
dept_1 = Departments(dept_name='IT', location='Ha Noi')
dept_2 = Departments(dept_name='HR', location='Ho Chi Minh')

session.add_all([dept_1, dept_2])

session.commit() # Commit -> thực hiện lưu
print('Chèn dữ liệu vào bảng departments_sqlalchemy thành công')

departments = session.query(Departments).all()
for dept in departments:
   print(dept.dept_id, dept.dept_name, dept.location)