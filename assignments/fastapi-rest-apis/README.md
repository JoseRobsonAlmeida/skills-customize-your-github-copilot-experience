# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice route creation, request validation, and CRUD operations with proper HTTP status codes.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoints

#### Descrição
Set up a FastAPI app and implement basic endpoints to confirm the API is running.

#### Requisitos
O programa concluído deve:

- Create a FastAPI app instance named `app`.
- Implement `GET /` that returns a JSON welcome message.
- Implement `GET /health` that returns `{ "status": "ok" }`.
- Run with Uvicorn and test both endpoints.

### 🛠️ Implement Product CRUD Routes

#### Descrição
Create REST endpoints for managing products using an in-memory list or dictionary.

#### Requisitos
O programa concluído deve:

- Define a `Product` model using Pydantic with `id`, `name`, `price`, and `in_stock`.
- Implement `POST /products` to create a product.
- Implement `GET /products` and `GET /products/{product_id}` to list and fetch products.
- Return `404` when a product does not exist.

### 🛠️ Add Update and Delete Operations

#### Descrição
Complete the CRUD flow by updating and deleting products.

#### Requisitos
O programa concluído deve:

- Implement `PUT /products/{product_id}` to update existing products.
- Implement `DELETE /products/{product_id}` to remove products.
- Return `204 No Content` for successful delete.
- Return clear error messages for invalid IDs.

### 🛠️ Validate Inputs and Query Parameters

#### Descrição
Improve API quality by adding validation and filtering options.

#### Requisitos
O programa concluído deve:

- Enforce `price > 0` using Pydantic validation.
- Add `GET /products?in_stock=true|false` filter support.
- Return `422` automatically for invalid request bodies.
- Test at least one valid and one invalid request for each modified endpoint.
