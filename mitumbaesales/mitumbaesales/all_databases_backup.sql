--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md53175bce1d3201d16594cebf9d7eb3f9d';
CREATE ROLE student;
ALTER ROLE student WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'md57c7815cb7f16994ea0847edc82377091';






--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "data_class" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: data_class; Type: DATABASE; Schema: -; Owner: student
--

CREATE DATABASE data_class WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE data_class OWNER TO student;

\connect data_class

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: cla; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA cla;


ALTER SCHEMA cla OWNER TO postgres;

--
-- Name: mitumba_esales; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA mitumba_esales;


ALTER SCHEMA mitumba_esales OWNER TO postgres;

--
-- Name: school; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA school;


ALTER SCHEMA school OWNER TO postgres;

--
-- Name: schools; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA schools;


ALTER SCHEMA schools OWNER TO postgres;

--
-- Name: trashion; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA trashion;


ALTER SCHEMA trashion OWNER TO postgres;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA mitumba_esales;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


--
-- Name: order_status; Type: TYPE; Schema: mitumba_esales; Owner: postgres
--

CREATE TYPE mitumba_esales.order_status AS ENUM (
    'Pending',
    'Paid',
    'Shipped'
);


ALTER TYPE mitumba_esales.order_status OWNER TO postgres;

--
-- Name: payment_method; Type: TYPE; Schema: mitumba_esales; Owner: postgres
--

CREATE TYPE mitumba_esales.payment_method AS ENUM (
    'M-Pesa'
);


ALTER TYPE mitumba_esales.payment_method OWNER TO postgres;

--
-- Name: payment_status; Type: TYPE; Schema: mitumba_esales; Owner: postgres
--

CREATE TYPE mitumba_esales.payment_status AS ENUM (
    'Pending',
    'Success',
    'Failed'
);


ALTER TYPE mitumba_esales.payment_status OWNER TO postgres;

--
-- Name: product_category; Type: TYPE; Schema: mitumba_esales; Owner: postgres
--

CREATE TYPE mitumba_esales.product_category AS ENUM (
    'High-Quality',
    'Fashion Finds'
);


ALTER TYPE mitumba_esales.product_category OWNER TO postgres;

--
-- Name: user_role; Type: TYPE; Schema: mitumba_esales; Owner: postgres
--

CREATE TYPE mitumba_esales.user_role AS ENUM (
    'buyer',
    'trader'
);


ALTER TYPE mitumba_esales.user_role OWNER TO postgres;

--
-- Name: order_status; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.order_status AS ENUM (
    'Pending',
    'Paid',
    'Shipped'
);


ALTER TYPE public.order_status OWNER TO postgres;

--
-- Name: payment_method; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.payment_method AS ENUM (
    'M-Pesa'
);


ALTER TYPE public.payment_method OWNER TO postgres;

--
-- Name: payment_status; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.payment_status AS ENUM (
    'Pending',
    'Success',
    'Failed'
);


ALTER TYPE public.payment_status OWNER TO postgres;

--
-- Name: product_category; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.product_category AS ENUM (
    'High-Quality',
    'Fashion Finds'
);


ALTER TYPE public.product_category OWNER TO postgres;

--
-- Name: user_role; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.user_role AS ENUM (
    'buyer',
    'trader'
);


ALTER TYPE public.user_role OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: classes; Type: TABLE; Schema: cla; Owner: postgres
--

CREATE TABLE cla.classes (
    class_id character varying(10) NOT NULL,
    class_name character varying(50) NOT NULL
);


ALTER TABLE cla.classes OWNER TO postgres;

--
-- Name: cart_items; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.cart_items (
    cart_item_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    cart_id uuid NOT NULL,
    product_id uuid NOT NULL,
    quantity integer DEFAULT 1 NOT NULL,
    unit_price numeric(10,2) NOT NULL,
    subtotal numeric(10,2) GENERATED ALWAYS AS (((quantity)::numeric * unit_price)) STORED,
    added_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT cart_items_quantity_check CHECK ((quantity > 0))
);


ALTER TABLE mitumba_esales.cart_items OWNER TO postgres;

--
-- Name: carts; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.carts (
    cart_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    buyer_id uuid NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE mitumba_esales.carts OWNER TO postgres;

--
-- Name: mitumba_esales_discounts; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.mitumba_esales_discounts (
    discount_id character varying(10) NOT NULL,
    name character varying(255) NOT NULL,
    discount_type character varying(50) NOT NULL,
    value numeric(10,2) NOT NULL,
    min_purchase_amount numeric(10,2) DEFAULT 0.00,
    max_discount_amount numeric(10,2) DEFAULT NULL::numeric,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE mitumba_esales.mitumba_esales_discounts OWNER TO postgres;

--
-- Name: mitumba_esales_offer_discounts; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.mitumba_esales_offer_discounts (
    offer_discount_id character varying(10) NOT NULL,
    offer_id integer NOT NULL,
    discount_id character varying(10) NOT NULL
);


ALTER TABLE mitumba_esales.mitumba_esales_offer_discounts OWNER TO postgres;

--
-- Name: mitumba_esales_offers; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.mitumba_esales_offers (
    offer_id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    offer_type character varying(50) NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    is_active boolean DEFAULT true,
    priority integer DEFAULT 100,
    usage_limit integer,
    uses_count integer DEFAULT 0,
    applies_to character varying(255) DEFAULT 'all_products'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE mitumba_esales.mitumba_esales_offers OWNER TO postgres;

--
-- Name: mitumba_esales_offers_offer_id_seq; Type: SEQUENCE; Schema: mitumba_esales; Owner: postgres
--

CREATE SEQUENCE mitumba_esales.mitumba_esales_offers_offer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mitumba_esales.mitumba_esales_offers_offer_id_seq OWNER TO postgres;

--
-- Name: mitumba_esales_offers_offer_id_seq; Type: SEQUENCE OWNED BY; Schema: mitumba_esales; Owner: postgres
--

ALTER SEQUENCE mitumba_esales.mitumba_esales_offers_offer_id_seq OWNED BY mitumba_esales.mitumba_esales_offers.offer_id;


--
-- Name: notifications; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.notifications (
    notification_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    user_id uuid NOT NULL,
    message text NOT NULL,
    notifications_type character varying(20),
    is_read boolean DEFAULT false,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT notifications_notifications_type_check CHECK (((notifications_type)::text = ANY ((ARRAY['Order update'::character varying, 'Payment Confirmation'::character varying, 'General Alert'::character varying])::text[])))
);


ALTER TABLE mitumba_esales.notifications OWNER TO postgres;

--
-- Name: offer_products; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.offer_products (
    offer_product_id character varying(255) NOT NULL,
    offer_id integer NOT NULL,
    product_id uuid NOT NULL
);


ALTER TABLE mitumba_esales.offer_products OWNER TO postgres;

--
-- Name: order_items; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.order_items (
    order_item_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    order_id uuid NOT NULL,
    product_id uuid NOT NULL,
    quantity integer NOT NULL,
    unit_price numeric(10,2) NOT NULL,
    subtotal numeric(10,2) GENERATED ALWAYS AS (((quantity)::numeric * unit_price)) STORED,
    added_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT order_items_quantity_check CHECK ((quantity > 0))
);


ALTER TABLE mitumba_esales.order_items OWNER TO postgres;

--
-- Name: orders; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.orders (
    order_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    buyer_id uuid NOT NULL,
    status mitumba_esales.order_status DEFAULT 'Pending'::mitumba_esales.order_status,
    total_price numeric(10,2) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE mitumba_esales.orders OWNER TO postgres;

--
-- Name: payments; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.payments (
    payment_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    order_id uuid NOT NULL,
    buyer_id uuid NOT NULL,
    amount numeric(10,2) NOT NULL,
    payment_method mitumba_esales.payment_method DEFAULT 'M-Pesa'::mitumba_esales.payment_method NOT NULL,
    payment_status mitumba_esales.payment_status DEFAULT 'Pending'::mitumba_esales.payment_status NOT NULL,
    phone_number character varying(20),
    mpesa_receipt_number character varying(100),
    paid_at timestamp without time zone,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE mitumba_esales.payments OWNER TO postgres;

--
-- Name: products; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.products (
    product_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    user_id uuid NOT NULL,
    category mitumba_esales.product_category NOT NULL,
    name character varying(100) NOT NULL,
    price numeric(10,2) NOT NULL,
    stock_quantity integer DEFAULT 1,
    image_paths text[] NOT NULL,
    description text NOT NULL,
    size character varying(10) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT products_stock_quantity_check CHECK ((stock_quantity >= 0))
);


ALTER TABLE mitumba_esales.products OWNER TO postgres;

--
-- Name: rate_trader; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.rate_trader (
    rate_trader_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    buyer_id uuid NOT NULL,
    seller_id uuid NOT NULL,
    rating integer NOT NULL,
    comment text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT rate_trader_rating_check CHECK (((rating >= 1) AND (rating <= 5)))
);


ALTER TABLE mitumba_esales.rate_trader OWNER TO postgres;

--
-- Name: reviews; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.reviews (
    review_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    buyer_id uuid NOT NULL,
    product_id uuid NOT NULL,
    rating integer NOT NULL,
    comment text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT reviews_rating_check CHECK (((rating >= 1) AND (rating <= 5)))
);


ALTER TABLE mitumba_esales.reviews OWNER TO postgres;

--
-- Name: sales_summaries; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.sales_summaries (
    summary_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    trader_id uuid NOT NULL,
    total_sales numeric(12,2) DEFAULT 0.00,
    total_orders integer DEFAULT 0,
    total_items_sold integer DEFAULT 0,
    total_earnings numeric(12,2) DEFAULT 0.00,
    start_date date NOT NULL,
    end_date date NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE mitumba_esales.sales_summaries OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: mitumba_esales; Owner: postgres
--

CREATE TABLE mitumba_esales.users (
    user_id uuid DEFAULT mitumba_esales.gen_random_uuid() NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100),
    phone character varying(15),
    password character varying(100) NOT NULL,
    user_type character varying(10) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT email_or_phone_check CHECK (((email IS NOT NULL) OR (phone IS NOT NULL))),
    CONSTRAINT users_user_type_check CHECK (((user_type)::text = ANY ((ARRAY['Buyer'::character varying, 'Seller'::character varying])::text[])))
);


ALTER TABLE mitumba_esales.users OWNER TO postgres;

--
-- Name: cart_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cart_items (
    cart_item_id uuid NOT NULL,
    cart_id uuid NOT NULL,
    product_id uuid NOT NULL,
    quantity integer DEFAULT 1 NOT NULL,
    unit_price numeric(10,2) NOT NULL,
    subtotal numeric(10,2) GENERATED ALWAYS AS (((quantity)::numeric * unit_price)) STORED,
    added_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT cart_items_quantity_check CHECK ((quantity > 0))
);


ALTER TABLE public.cart_items OWNER TO postgres;

--
-- Name: carts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.carts (
    cart_id uuid NOT NULL,
    buyer_id uuid NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.carts OWNER TO postgres;

--
-- Name: mitumba_esales_discounts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mitumba_esales_discounts (
    discount_id character varying(10) NOT NULL,
    name character varying(255) NOT NULL,
    discount_type character varying(50) NOT NULL,
    value numeric(10,2) NOT NULL,
    min_purchase_amount numeric(10,2) DEFAULT 0.00,
    max_discount_amount numeric(10,2) DEFAULT NULL::numeric,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.mitumba_esales_discounts OWNER TO postgres;

--
-- Name: mitumba_esales_offer_discounts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mitumba_esales_offer_discounts (
    offer_discount_id character varying(10) NOT NULL,
    offer_id integer NOT NULL,
    discount_id character varying(10) NOT NULL
);


ALTER TABLE public.mitumba_esales_offer_discounts OWNER TO postgres;

--
-- Name: mitumba_esales_offers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mitumba_esales_offers (
    offer_id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    offer_type character varying(50) NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    is_active boolean DEFAULT true,
    priority integer DEFAULT 100,
    usage_limit integer,
    uses_count integer DEFAULT 0,
    applies_to character varying(255) DEFAULT 'all_products'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.mitumba_esales_offers OWNER TO postgres;

--
-- Name: mitumba_esales_offers_offer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mitumba_esales_offers_offer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mitumba_esales_offers_offer_id_seq OWNER TO postgres;

--
-- Name: mitumba_esales_offers_offer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mitumba_esales_offers_offer_id_seq OWNED BY public.mitumba_esales_offers.offer_id;


--
-- Name: notifications; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notifications (
    notification_id uuid NOT NULL,
    user_id uuid NOT NULL,
    message text NOT NULL,
    notifications_type character varying(20),
    is_read boolean DEFAULT false,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT notifications_notifications_type_check CHECK (((notifications_type)::text = ANY ((ARRAY['Order update'::character varying, 'Payment Confirmation'::character varying, 'General Alert'::character varying])::text[])))
);


ALTER TABLE public.notifications OWNER TO postgres;

--
-- Name: offer_products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.offer_products (
    offer_product_id character varying(255) NOT NULL,
    offer_id integer NOT NULL,
    product_id uuid NOT NULL
);


ALTER TABLE public.offer_products OWNER TO postgres;

--
-- Name: order_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_items (
    order_item_id uuid NOT NULL,
    order_id uuid NOT NULL,
    product_id uuid NOT NULL,
    quantity integer NOT NULL,
    unit_price numeric(10,2) NOT NULL,
    subtotal numeric(10,2) GENERATED ALWAYS AS (((quantity)::numeric * unit_price)) STORED,
    added_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT order_items_quantity_check CHECK ((quantity > 0))
);


ALTER TABLE public.order_items OWNER TO postgres;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_id uuid NOT NULL,
    buyer_id uuid NOT NULL,
    status public.order_status DEFAULT 'Pending'::public.order_status,
    total_price numeric(10,2) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: payments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payments (
    payment_id uuid NOT NULL,
    order_id uuid NOT NULL,
    buyer_id uuid NOT NULL,
    amount numeric(10,2) NOT NULL,
    payment_method public.payment_method DEFAULT 'M-Pesa'::public.payment_method NOT NULL,
    payment_status public.payment_status DEFAULT 'Pending'::public.payment_status NOT NULL,
    phone_number character varying(20),
    mpesa_receipt_number character varying(100),
    paid_at timestamp without time zone,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.payments OWNER TO postgres;

--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    product_id uuid NOT NULL,
    user_id uuid NOT NULL,
    category public.product_category NOT NULL,
    name character varying(100) NOT NULL,
    price numeric(10,2) NOT NULL,
    stock_quantity integer DEFAULT 1,
    image_paths text[] DEFAULT ARRAY[]::text[] NOT NULL,
    description text NOT NULL,
    size character varying(10) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT products_stock_quantity_check CHECK ((stock_quantity >= 0))
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: rate_trader; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rate_trader (
    rate_trader_id uuid NOT NULL,
    buyer_id uuid NOT NULL,
    seller_id uuid NOT NULL,
    rating integer NOT NULL,
    comment text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT rate_trader_rating_check CHECK (((rating >= 1) AND (rating <= 5)))
);


ALTER TABLE public.rate_trader OWNER TO postgres;

--
-- Name: reviews; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reviews (
    review_id uuid NOT NULL,
    buyer_id uuid NOT NULL,
    product_id uuid NOT NULL,
    rating integer NOT NULL,
    comment text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT reviews_rating_check CHECK (((rating >= 1) AND (rating <= 5)))
);


ALTER TABLE public.reviews OWNER TO postgres;

--
-- Name: transaction_history; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaction_history (
    transaction_id uuid NOT NULL,
    user_id uuid NOT NULL,
    transaction_type character varying(30) NOT NULL,
    related_payment_id uuid,
    transaction_status public.payment_status,
    amount numeric(10,2) NOT NULL,
    platform_fee numeric(10,2) DEFAULT 0.00,
    description text,
    processed_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.transaction_history OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id uuid NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100),
    phone character varying(15),
    password character varying(100) NOT NULL,
    user_type character varying(10) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT email_or_phone_check CHECK (((email IS NOT NULL) OR (phone IS NOT NULL))),
    CONSTRAINT users_user_type_check CHECK (((user_type)::text = ANY ((ARRAY['Buyer'::character varying, 'Seller'::character varying])::text[])))
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: students; Type: TABLE; Schema: school; Owner: postgres
--

CREATE TABLE school.students (
    student_id character varying(20) NOT NULL,
    full_name character varying(100) NOT NULL,
    dob integer,
    gender character varying(10),
    enrolled_in character varying(50),
    student_extracurricular character varying(60),
    fav_course character varying(50)
);


ALTER TABLE school.students OWNER TO postgres;

--
-- Name: students; Type: TABLE; Schema: schools; Owner: postgres
--

CREATE TABLE schools.students (
    student_id character varying(20) NOT NULL,
    full_name character varying(100) NOT NULL,
    dob integer NOT NULL,
    gender character varying(10) NOT NULL,
    enrolled_in character varying(50) NOT NULL,
    student_extracurricular character varying(60) NOT NULL,
    fav_course character varying(50) NOT NULL
);


ALTER TABLE schools.students OWNER TO postgres;

--
-- Name: orphanages; Type: TABLE; Schema: trashion; Owner: postgres
--

CREATE TABLE trashion.orphanages (
    orphange_id integer NOT NULL,
    orphanage_name character varying(255),
    registration_number integer,
    location character varying(255),
    contact_information integer,
    population integer
);


ALTER TABLE trashion.orphanages OWNER TO postgres;

--
-- Name: orphanages_orphange_id_seq; Type: SEQUENCE; Schema: trashion; Owner: postgres
--

CREATE SEQUENCE trashion.orphanages_orphange_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE trashion.orphanages_orphange_id_seq OWNER TO postgres;

--
-- Name: orphanages_orphange_id_seq; Type: SEQUENCE OWNED BY; Schema: trashion; Owner: postgres
--

ALTER SEQUENCE trashion.orphanages_orphange_id_seq OWNED BY trashion.orphanages.orphange_id;


--
-- Name: traders_data; Type: TABLE; Schema: trashion; Owner: postgres
--

CREATE TABLE trashion.traders_data (
    trader_id integer NOT NULL,
    name character varying(255),
    date_of_birth date,
    location character varying(255),
    gender character varying(255),
    contact_information integer
);


ALTER TABLE trashion.traders_data OWNER TO postgres;

--
-- Name: traders_data_trader_id_seq; Type: SEQUENCE; Schema: trashion; Owner: postgres
--

CREATE SEQUENCE trashion.traders_data_trader_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE trashion.traders_data_trader_id_seq OWNER TO postgres;

--
-- Name: traders_data_trader_id_seq; Type: SEQUENCE OWNED BY; Schema: trashion; Owner: postgres
--

ALTER SEQUENCE trashion.traders_data_trader_id_seq OWNED BY trashion.traders_data.trader_id;


--
-- Name: mitumba_esales_offers offer_id; Type: DEFAULT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.mitumba_esales_offers ALTER COLUMN offer_id SET DEFAULT nextval('mitumba_esales.mitumba_esales_offers_offer_id_seq'::regclass);


--
-- Name: mitumba_esales_offers offer_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitumba_esales_offers ALTER COLUMN offer_id SET DEFAULT nextval('public.mitumba_esales_offers_offer_id_seq'::regclass);


--
-- Name: orphanages orphange_id; Type: DEFAULT; Schema: trashion; Owner: postgres
--

ALTER TABLE ONLY trashion.orphanages ALTER COLUMN orphange_id SET DEFAULT nextval('trashion.orphanages_orphange_id_seq'::regclass);


--
-- Name: traders_data trader_id; Type: DEFAULT; Schema: trashion; Owner: postgres
--

ALTER TABLE ONLY trashion.traders_data ALTER COLUMN trader_id SET DEFAULT nextval('trashion.traders_data_trader_id_seq'::regclass);


--
-- Data for Name: classes; Type: TABLE DATA; Schema: cla; Owner: postgres
--

COPY cla.classes (class_id, class_name) FROM stdin;
\.


--
-- Data for Name: cart_items; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.cart_items (cart_item_id, cart_id, product_id, quantity, unit_price, added_at) FROM stdin;
\.


--
-- Data for Name: carts; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.carts (cart_id, buyer_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: mitumba_esales_discounts; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.mitumba_esales_discounts (discount_id, name, discount_type, value, min_purchase_amount, max_discount_amount, is_active, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: mitumba_esales_offer_discounts; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.mitumba_esales_offer_discounts (offer_discount_id, offer_id, discount_id) FROM stdin;
\.


--
-- Data for Name: mitumba_esales_offers; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.mitumba_esales_offers (offer_id, name, description, offer_type, start_date, end_date, is_active, priority, usage_limit, uses_count, applies_to, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: notifications; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.notifications (notification_id, user_id, message, notifications_type, is_read, created_at) FROM stdin;
\.


--
-- Data for Name: offer_products; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.offer_products (offer_product_id, offer_id, product_id) FROM stdin;
\.


--
-- Data for Name: order_items; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.order_items (order_item_id, order_id, product_id, quantity, unit_price, added_at) FROM stdin;
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.orders (order_id, buyer_id, status, total_price, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: payments; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.payments (payment_id, order_id, buyer_id, amount, payment_method, payment_status, phone_number, mpesa_receipt_number, paid_at, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.products (product_id, user_id, category, name, price, stock_quantity, image_paths, description, size, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: rate_trader; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.rate_trader (rate_trader_id, buyer_id, seller_id, rating, comment, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.reviews (review_id, buyer_id, product_id, rating, comment, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: sales_summaries; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.sales_summaries (summary_id, trader_id, total_sales, total_orders, total_items_sold, total_earnings, start_date, end_date, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: mitumba_esales; Owner: postgres
--

COPY mitumba_esales.users (user_id, name, email, phone, password, user_type, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: cart_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cart_items (cart_item_id, cart_id, product_id, quantity, unit_price, added_at) FROM stdin;
\.


--
-- Data for Name: carts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.carts (cart_id, buyer_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: mitumba_esales_discounts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mitumba_esales_discounts (discount_id, name, discount_type, value, min_purchase_amount, max_discount_amount, is_active, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: mitumba_esales_offer_discounts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mitumba_esales_offer_discounts (offer_discount_id, offer_id, discount_id) FROM stdin;
\.


--
-- Data for Name: mitumba_esales_offers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mitumba_esales_offers (offer_id, name, description, offer_type, start_date, end_date, is_active, priority, usage_limit, uses_count, applies_to, created_at, updated_at) FROM stdin;
1	Fashion Finds Summer Sale	Get great discounts on our everyday Fashion Finds collection.	promotional	2025-06-15 00:00:00	2025-07-15 23:59:59	t	10	\N	0	specific_categories	2025-06-15 14:51:46.688904	2025-06-15 14:51:46.688904
2	Good Quality Exclusive Discount	Special savings on premium and high-quality second-hand apparel.	promotional	2025-06-01 00:00:00	2025-08-31 23:59:59	t	5	\N	0	specific_categories	2025-06-15 14:51:46.688904	2025-06-15 14:51:46.688904
3	Kids Apparel Bundle Deal	Buy any 2 kids items, get a third for 50% off.	bundle	2025-06-20 00:00:00	2025-07-20 23:59:59	t	12	\N	0	specific_categories	2025-06-15 14:51:46.688904	2025-06-15 14:51:46.688904
4	Weekend Free Shipping Promo	Enjoy free standard shipping on all orders this weekend!	free_shipping	2025-06-21 00:00:00	2025-06-23 23:59:59	t	18	\N	0	entire_order	2025-06-15 14:51:46.688904	2025-06-15 14:51:46.688904
5	BOGO T-Shirt Offer	Buy one T-Shirt, get one of equal or lesser value free!	bogo	2025-06-18 00:00:00	2025-07-18 23:59:59	t	8	\N	0	specific_products	2025-06-15 14:51:46.688904	2025-06-15 14:51:46.688904
\.


--
-- Data for Name: notifications; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notifications (notification_id, user_id, message, notifications_type, is_read, created_at) FROM stdin;
\.


--
-- Data for Name: offer_products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.offer_products (offer_product_id, offer_id, product_id) FROM stdin;
\.


--
-- Data for Name: order_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_items (order_item_id, order_id, product_id, quantity, unit_price, added_at) FROM stdin;
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (order_id, buyer_id, status, total_price, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: payments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payments (payment_id, order_id, buyer_id, amount, payment_method, payment_status, phone_number, mpesa_receipt_number, paid_at, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (product_id, user_id, category, name, price, stock_quantity, image_paths, description, size, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: rate_trader; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rate_trader (rate_trader_id, buyer_id, seller_id, rating, comment, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reviews (review_id, buyer_id, product_id, rating, comment, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: transaction_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaction_history (transaction_id, user_id, transaction_type, related_payment_id, transaction_status, amount, platform_fee, description, processed_at) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, name, email, phone, password, user_type, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: school; Owner: postgres
--

COPY school.students (student_id, full_name, dob, gender, enrolled_in, student_extracurricular, fav_course) FROM stdin;
ST99	Abel Mekonnen	16	Male	\N	\N	\N
ST92	Tigist Alemu	17	Female	\N	\N	\N
ST98	Biruk Tesfaye	15	Male	\N	\N	\N
ST90	Selam Getachew	16	Female	\N	\N	\N
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: schools; Owner: postgres
--

COPY schools.students (student_id, full_name, dob, gender, enrolled_in, student_extracurricular, fav_course) FROM stdin;
ST99	Yeabsra Mekonnen	16	Male	Natural	Std_gov.t	Biology
ST92	Sala Alemu	17	Female	Natural	Science	physics
ST98	Biruk Tesfaye	15	Male	Social	Sport	History
ST90	Selam Getachew	16	Female	Social	Mini-Media	Civics
\.


--
-- Data for Name: orphanages; Type: TABLE DATA; Schema: trashion; Owner: postgres
--

COPY trashion.orphanages (orphange_id, orphanage_name, registration_number, location, contact_information, population) FROM stdin;
\.


--
-- Data for Name: traders_data; Type: TABLE DATA; Schema: trashion; Owner: postgres
--

COPY trashion.traders_data (trader_id, name, date_of_birth, location, gender, contact_information) FROM stdin;
1	Anita	2005-04-10	Nairobi	Female	704697456
2	Anita	2005-04-10	Nairobi	Female	704697456
3	Anita	2005-04-10	Nairobi	Female	704697456
\.


--
-- Name: mitumba_esales_offers_offer_id_seq; Type: SEQUENCE SET; Schema: mitumba_esales; Owner: postgres
--

SELECT pg_catalog.setval('mitumba_esales.mitumba_esales_offers_offer_id_seq', 1, false);


--
-- Name: mitumba_esales_offers_offer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mitumba_esales_offers_offer_id_seq', 5, true);


--
-- Name: orphanages_orphange_id_seq; Type: SEQUENCE SET; Schema: trashion; Owner: postgres
--

SELECT pg_catalog.setval('trashion.orphanages_orphange_id_seq', 1, false);


--
-- Name: traders_data_trader_id_seq; Type: SEQUENCE SET; Schema: trashion; Owner: postgres
--

SELECT pg_catalog.setval('trashion.traders_data_trader_id_seq', 3, true);


--
-- Name: classes classes_pkey; Type: CONSTRAINT; Schema: cla; Owner: postgres
--

ALTER TABLE ONLY cla.classes
    ADD CONSTRAINT classes_pkey PRIMARY KEY (class_id);


--
-- Name: cart_items cart_items_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.cart_items
    ADD CONSTRAINT cart_items_pkey PRIMARY KEY (cart_item_id);


--
-- Name: carts carts_buyer_id_key; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.carts
    ADD CONSTRAINT carts_buyer_id_key UNIQUE (buyer_id);


--
-- Name: carts carts_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.carts
    ADD CONSTRAINT carts_pkey PRIMARY KEY (cart_id);


--
-- Name: mitumba_esales_discounts mitumba_esales_discounts_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.mitumba_esales_discounts
    ADD CONSTRAINT mitumba_esales_discounts_pkey PRIMARY KEY (discount_id);


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_offer_id_discount_id_key; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_offer_id_discount_id_key UNIQUE (offer_id, discount_id);


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_pkey PRIMARY KEY (offer_discount_id);


--
-- Name: mitumba_esales_offers mitumba_esales_offers_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.mitumba_esales_offers
    ADD CONSTRAINT mitumba_esales_offers_pkey PRIMARY KEY (offer_id);


--
-- Name: notifications notifications_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (notification_id);


--
-- Name: offer_products offer_products_offer_id_product_id_key; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.offer_products
    ADD CONSTRAINT offer_products_offer_id_product_id_key UNIQUE (offer_id, product_id);


--
-- Name: offer_products offer_products_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.offer_products
    ADD CONSTRAINT offer_products_pkey PRIMARY KEY (offer_product_id);


--
-- Name: order_items order_items_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (order_item_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- Name: payments payments_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.payments
    ADD CONSTRAINT payments_pkey PRIMARY KEY (payment_id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- Name: rate_trader rate_trader_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.rate_trader
    ADD CONSTRAINT rate_trader_pkey PRIMARY KEY (rate_trader_id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (review_id);


--
-- Name: sales_summaries sales_summaries_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.sales_summaries
    ADD CONSTRAINT sales_summaries_pkey PRIMARY KEY (summary_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_phone_key; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.users
    ADD CONSTRAINT users_phone_key UNIQUE (phone);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: cart_items cart_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_items
    ADD CONSTRAINT cart_items_pkey PRIMARY KEY (cart_item_id);


--
-- Name: carts carts_buyer_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carts
    ADD CONSTRAINT carts_buyer_id_key UNIQUE (buyer_id);


--
-- Name: carts carts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carts
    ADD CONSTRAINT carts_pkey PRIMARY KEY (cart_id);


--
-- Name: mitumba_esales_discounts mitumba_esales_discounts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitumba_esales_discounts
    ADD CONSTRAINT mitumba_esales_discounts_pkey PRIMARY KEY (discount_id);


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_offer_id_discount_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_offer_id_discount_id_key UNIQUE (offer_id, discount_id);


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_pkey PRIMARY KEY (offer_discount_id);


--
-- Name: mitumba_esales_offers mitumba_esales_offers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitumba_esales_offers
    ADD CONSTRAINT mitumba_esales_offers_pkey PRIMARY KEY (offer_id);


--
-- Name: notifications notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (notification_id);


--
-- Name: offer_products offer_products_offer_id_product_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_products
    ADD CONSTRAINT offer_products_offer_id_product_id_key UNIQUE (offer_id, product_id);


--
-- Name: offer_products offer_products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_products
    ADD CONSTRAINT offer_products_pkey PRIMARY KEY (offer_product_id);


--
-- Name: order_items order_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (order_item_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- Name: payments payments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_pkey PRIMARY KEY (payment_id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- Name: rate_trader rate_trader_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rate_trader
    ADD CONSTRAINT rate_trader_pkey PRIMARY KEY (rate_trader_id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (review_id);


--
-- Name: transaction_history transaction_history_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaction_history
    ADD CONSTRAINT transaction_history_pkey PRIMARY KEY (transaction_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_phone_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_phone_key UNIQUE (phone);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: school; Owner: postgres
--

ALTER TABLE ONLY school.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (student_id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: schools; Owner: postgres
--

ALTER TABLE ONLY schools.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (student_id);


--
-- Name: orphanages orphanages_pkey; Type: CONSTRAINT; Schema: trashion; Owner: postgres
--

ALTER TABLE ONLY trashion.orphanages
    ADD CONSTRAINT orphanages_pkey PRIMARY KEY (orphange_id);


--
-- Name: traders_data traders_data_pkey; Type: CONSTRAINT; Schema: trashion; Owner: postgres
--

ALTER TABLE ONLY trashion.traders_data
    ADD CONSTRAINT traders_data_pkey PRIMARY KEY (trader_id);


--
-- Name: cart_items cart_items_cart_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.cart_items
    ADD CONSTRAINT cart_items_cart_id_fkey FOREIGN KEY (cart_id) REFERENCES mitumba_esales.carts(cart_id) ON DELETE CASCADE;


--
-- Name: cart_items cart_items_product_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.cart_items
    ADD CONSTRAINT cart_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES mitumba_esales.products(product_id) ON DELETE CASCADE;


--
-- Name: carts carts_buyer_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.carts
    ADD CONSTRAINT carts_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_discount_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_discount_id_fkey FOREIGN KEY (discount_id) REFERENCES mitumba_esales.mitumba_esales_discounts(discount_id) ON DELETE CASCADE;


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_offer_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_offer_id_fkey FOREIGN KEY (offer_id) REFERENCES mitumba_esales.mitumba_esales_offers(offer_id) ON DELETE CASCADE;


--
-- Name: notifications notifications_user_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.notifications
    ADD CONSTRAINT notifications_user_id_fkey FOREIGN KEY (user_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: offer_products offer_products_offer_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.offer_products
    ADD CONSTRAINT offer_products_offer_id_fkey FOREIGN KEY (offer_id) REFERENCES mitumba_esales.mitumba_esales_offers(offer_id) ON DELETE CASCADE;


--
-- Name: offer_products offer_products_product_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.offer_products
    ADD CONSTRAINT offer_products_product_id_fkey FOREIGN KEY (product_id) REFERENCES mitumba_esales.products(product_id) ON DELETE CASCADE;


--
-- Name: order_items order_items_order_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.order_items
    ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES mitumba_esales.orders(order_id) ON DELETE CASCADE;


--
-- Name: order_items order_items_product_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.order_items
    ADD CONSTRAINT order_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES mitumba_esales.products(product_id) ON DELETE CASCADE;


--
-- Name: orders orders_buyer_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.orders
    ADD CONSTRAINT orders_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: payments payments_buyer_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.payments
    ADD CONSTRAINT payments_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: payments payments_order_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.payments
    ADD CONSTRAINT payments_order_id_fkey FOREIGN KEY (order_id) REFERENCES mitumba_esales.orders(order_id) ON DELETE CASCADE;


--
-- Name: products products_user_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.products
    ADD CONSTRAINT products_user_id_fkey FOREIGN KEY (user_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: rate_trader rate_trader_buyer_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.rate_trader
    ADD CONSTRAINT rate_trader_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: rate_trader rate_trader_seller_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.rate_trader
    ADD CONSTRAINT rate_trader_seller_id_fkey FOREIGN KEY (seller_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: reviews reviews_buyer_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.reviews
    ADD CONSTRAINT reviews_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: reviews reviews_product_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.reviews
    ADD CONSTRAINT reviews_product_id_fkey FOREIGN KEY (product_id) REFERENCES mitumba_esales.products(product_id) ON DELETE CASCADE;


--
-- Name: sales_summaries sales_summaries_trader_id_fkey; Type: FK CONSTRAINT; Schema: mitumba_esales; Owner: postgres
--

ALTER TABLE ONLY mitumba_esales.sales_summaries
    ADD CONSTRAINT sales_summaries_trader_id_fkey FOREIGN KEY (trader_id) REFERENCES mitumba_esales.users(user_id) ON DELETE CASCADE;


--
-- Name: cart_items cart_items_cart_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_items
    ADD CONSTRAINT cart_items_cart_id_fkey FOREIGN KEY (cart_id) REFERENCES public.carts(cart_id) ON DELETE CASCADE;


--
-- Name: cart_items cart_items_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_items
    ADD CONSTRAINT cart_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;


--
-- Name: carts carts_buyer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carts
    ADD CONSTRAINT carts_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_discount_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_discount_id_fkey FOREIGN KEY (discount_id) REFERENCES public.mitumba_esales_discounts(discount_id) ON DELETE CASCADE;


--
-- Name: mitumba_esales_offer_discounts mitumba_esales_offer_discounts_offer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitumba_esales_offer_discounts
    ADD CONSTRAINT mitumba_esales_offer_discounts_offer_id_fkey FOREIGN KEY (offer_id) REFERENCES public.mitumba_esales_offers(offer_id) ON DELETE CASCADE;


--
-- Name: notifications notifications_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: offer_products offer_products_offer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_products
    ADD CONSTRAINT offer_products_offer_id_fkey FOREIGN KEY (offer_id) REFERENCES public.mitumba_esales_offers(offer_id) ON DELETE CASCADE;


--
-- Name: offer_products offer_products_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_products
    ADD CONSTRAINT offer_products_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;


--
-- Name: order_items order_items_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(order_id) ON DELETE CASCADE;


--
-- Name: order_items order_items_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;


--
-- Name: orders orders_buyer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: payments payments_buyer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: payments payments_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(order_id) ON DELETE CASCADE;


--
-- Name: products products_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: rate_trader rate_trader_buyer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rate_trader
    ADD CONSTRAINT rate_trader_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: rate_trader rate_trader_seller_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rate_trader
    ADD CONSTRAINT rate_trader_seller_id_fkey FOREIGN KEY (seller_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: reviews reviews_buyer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_buyer_id_fkey FOREIGN KEY (buyer_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- Name: reviews reviews_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;


--
-- Name: transaction_history transaction_history_related_payment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaction_history
    ADD CONSTRAINT transaction_history_related_payment_id_fkey FOREIGN KEY (related_payment_id) REFERENCES public.payments(payment_id);


--
-- Name: transaction_history transaction_history_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaction_history
    ADD CONSTRAINT transaction_history_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

--
-- Database "mitumba_esales" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: mitumba_esales; Type: DATABASE; Schema: -; Owner: student
--

CREATE DATABASE mitumba_esales WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE mitumba_esales OWNER TO student;

\connect mitumba_esales

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "mitumba_esales_db" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: mitumba_esales_db; Type: DATABASE; Schema: -; Owner: student
--

CREATE DATABASE mitumba_esales_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE mitumba_esales_db OWNER TO student;

\connect mitumba_esales_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "mitumbaesalesdb" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: mitumbaesalesdb; Type: DATABASE; Schema: -; Owner: student
--

CREATE DATABASE mitumbaesalesdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE mitumbaesalesdb OWNER TO student;

\connect mitumbaesalesdb

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "student" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: student; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE student WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE student OWNER TO postgres;

\connect student

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "your_db_name" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: your_db_name; Type: DATABASE; Schema: -; Owner: student
--

CREATE DATABASE your_db_name WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE your_db_name OWNER TO student;

\connect your_db_name

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

