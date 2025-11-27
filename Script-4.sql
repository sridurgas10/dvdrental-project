
 3. PostgreSQL Views

customer_rental_history_view — shows each customer’s total rentals and payments.

Endpoints:
GET /reports/customer-history/
GET /reports/film-availability/


select *from customer c 

select *from rental r 

select *from inventory

create or replace view customer_rental_history as
select c.customer_id,count(r.rental_id) as total_rentals,sum(p.amount) as total_payment from customer c
left join rental r on c.customer_id = r.customer_id
left join payment p on r.rental_id = p.rental_id
group by c.customer_id
order by c.customer_id



select *from customer_rental_history



--film_availability_view — shows available stock count per film.
create or replace view film_availability as
select f.film_id,f.title,count(i.inventory_id) as total_stock,count(r.rental_id) filter (where r.return_date is null) as rented_count,
    count(i.inventory_id) - count(r.rental_id) filter (where r.return_date is null) as available_stock from film f
join inventory i on f.film_id = i.film_id
left join rental r on i.inventory_id = r.inventory_id
group by f.film_id, f.title
order by f.film_id



select *from film_availability



--------------------------------------------------------------------------------------
select *from staff 

calculate_total_rental_cost(customer_id INT)



--function(1):
create or replace function calculate_total_rental_cost(customer_id int)
returns float
language plpgsql
as $$
declare
    rental_cost float;
begin
    select sum(amount) into rental_cost from payment p
    where p.customer_id = customer_id;
    return rental_cost;
end;
$$;

SELECT calculate_total_rental_cost(5)

select*from payment


select*from category

select*from customer

--function (2)get_overdue_rentals(days INT) → Returns rentals not returned within given days.
--get_overdue_rentals(days INT)

CREATE OR REPLACE FUNCTION get_overdue_rentals(days INT)
RETURNS SETOF rental
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT *FROM rental WHERE return_date IS NULL AND rental_date < NOW() - make_interval(days);
END;
$$;


select get_overdue_rentals(7)


select*from rental


---------------------------------------------------------------
-- Function to update inventory when a rental is returned
create or replace function update_inventory_on_return()
returns trigger 
language plpgsql
as
$$
begin
    update inventory
    set last_update = now()
    where inventory_id = new.inventory_id;
    return new;
end;
$$ ;

create trigger trg_update_inventory
after update of return_date on rental
for each row
when (new.return_date is not null)
execute function update_inventory_on_return();



select inventory_id,last_update from inventory where inventory_id = 367;

select*from rental


select rental_id,inventory_id,return_date from rental where rental_id = 1;

update rental set return_date = now() where rental_id = 1;

-----------------------------------------------------------------------------
---when payment is insert log in to new audit table

create table payment_audit_table(
    
    payment_id int,
    customer_id int,
    staff_id int,
    rental_id int,
    amount numeric(10,2),
    payment_date timestamp,
    
    changed_at timestamp default current_timestamp
);

create or replace function audit_table()
returns trigger
language plpgsql
as 
$$
begin
	insert into  payment_audit_table(payment_id,customer_id,staff_id,rental_id,amount, payment_date)
    values (new.payment_id, new.customer_id,new.staff_id,new.rental_id,new.amount, new.payment_date);
    return new;
	
end;
$$;

create trigger trg_payment_insert
after insert on payment
for each row
execute function audit_table();


select *from payment


insert into payment(payment_id,customer_id,staff_id,rental_id, amount, payment_date) 
values (1,6,4,103, 100.00, now());


select * from payment_audit_table;
------------------------------------------------------------------------------------------

--GET /reports/top-customers/Top 5 customers by payment volume.
create or replace view top5_customer
as
select c.customer_id,c.first_name,c.last_name,sum(p.amount) as total_amount from customer c 
join payment p on c.customer_id=p.customer_id
group by c.customer_id , c.first_name, c.last_name order by sum(p.amount) desc
limit 5

select *from top5_customer



--Most rented films in the last 30 days.GET /reports/top-films/


create or replace view  top10_films 
as
select f.film_id,f.title ,count(r.rental_id) as  rental_count from rental r  join inventory i on i.inventory_id=r.inventory_id
join film f on f.film_id=i.film_id 
where r.rental_date >= now() - interval '30 days'
group by f.title,f.film_id order by count(r.rental_id) desc
limit 10


select *from  top10_films 


--Staff performance (number of rentals processed).GET /reports/staff-performance/

create or replace view staff_performance_view
as
select staff_id,count(r.rental_id) as totoal_rentals from rental r
group by staff_id order by count(r.rental_id) desc


select *from staff_performance_view


--------------------------------------------------------------------------------------------------