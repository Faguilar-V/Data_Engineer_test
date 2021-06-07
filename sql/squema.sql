########################## 1.2 LOAD DATA ########################################333
CREATE DATABASE companydb
    WITH 
    OWNER = faguilar
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
-- Table: public.orders

-- DROP TABLE public.orders;

CREATE TABLE IF NOT EXISTS public.payments
(
    charge_id character varying(255) NOT NULL,
    company_name character varying(130),
    company_id character varying(255) NOT NULL,
    amount numeric(55, 2) NOT NULL,
    order_status character varying(30) NOT NULL,
    create_at date NOT NULL,
    update_at date,
);


ALTER TABLE public.payments
    OWNER to faguilar;

############################## 1.4. DATA DISPERTION #########################################
CREATE TABLE charges AS
	SELECT charge_id, amount, created_at, update_at, company_id FROM payments;

ALTER TABLE public.charges
    ALTER COLUMN charge_id SET NOT NULL;

ALTER TABLE public.charges
    ALTER COLUMN amount SET NOT NULL;

ALTER TABLE public.charges
    ALTER COLUMN created_at SET NOT NULL;

ALTER TABLE public.charges
    ALTER COLUMN company_id SET NOT NULL;
ALTER TABLE public.charges
    ADD PRIMARY KEY (charge_id);

ALTER TABLE public.charges
    OWNER to faguilar;

CREATE TABLE companies AS
	SELECT DISTINCT company_id, company_name FROM payments;

ALTER TABLE public.companies
    ADD PRIMARY KEY (company_id);

ALTER TABLE public.companies
    OWNER to faguilar;

ALTER TABLE public.charges
   ADD CONSTRAINT fk_company
   	FOREIGN KEY (company_id) 
   		REFERENCES companies(company_id);