# In-House Order Tracker

A REST API for tracking in-house orders (office supplies, cafeteria restocks, lunch deliveries) from creation through pickup. I built it to practice API design in Python with **FastAPI**.

## Features
- Full CRUD for orders
- Look up orders by ID or customer name
- Track order status: `pending` → `ready` → `picked_up`
- Request validation with Pydantic models
- Interactive API docs generated automatically by FastAPI

## Tech Stack
Python · FastAPI · Pydantic · Uvicorn

## Endpoints
| Method | Route | Description |
|---|---|---|
| `GET` | `/orders` | List all orders |
| `GET` | `/orders/{order_id}` | Get one order by ID |
| `GET` | `/orders/Customer/{name}` | Find an order by customer name |
| `POST` | `/orders` | Create a new order (starts as `pending`) |
| `PATCH` | `/orders/{order_id}` | Update any fields on an order |
| `DELETE` | `/orders/{order_id}` | Delete an order |

## Getting Started
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```
Then open **http://localhost:8000/docs** to try the endpoints in your browser.

## Roadmap
- [ ] Save orders to a database instead of in memory
- [ ] Partial-match customer search for customer service lookups
