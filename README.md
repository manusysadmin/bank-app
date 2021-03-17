# Bank App Project

A single-page application with RESTful API that consists of a Django backend and Angular frontend. 
It presents product recommendations to a registered user based on the answers to a questionnaire.

It uses persistence in the form of a PostgreSQL database.


Method | Path | Description | User Role
--- | --- | --- | ---
POST | /api/login | Authenticate user | None (Anonymous)
POST | /api/register | Create user | None (Anonymous)
GET | /api/products/search?age={age}&income={income}&student={student} | Get product(s) by criteria | User
GET | /api/manage/products | Get all products | Admin, Product Manager
GET | /api/manage/products/{productName} | Get specific product | Admin, Product Manager
POST | /api/manage/products/add | Create product | Admin, Product Manager
PUT | /api/manage/products/{productName} | Update product | Admin, Product Manager
DELETE | /api/manage/products/{productName} | Delete product | Admin, Product Manager
GET | /api/manage/users | Get all users | Admin
GET | /api/manage/users/{id} | Get specific user | Admin
PUT | /api/manage/users/{id} | Update user | Admin
DELETE | /api/manage/users/{id} | Delete user | Admin

