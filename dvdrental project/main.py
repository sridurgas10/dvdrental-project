from fastapi import FastAPI
from auth.route import router
from film.route import film_router
from customer.route import customer_router
from rental.route import rental_router
from payment.route import payment_router
from category.route import category_router


app=FastAPI()

app.include_router(router)
app.include_router(film_router)
app.include_router(customer_router)
app.include_router(rental_router)
app.include_router(payment_router)
app.include_router(category_router)
