CREATE TABLE stores (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(200) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(100)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    item_type VARCHAR(50) NOT NULL
);

CREATE TABLE store_products (
    store_id INT NOT NULL REFERENCES stores(store_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    quantity_available INT NOT NULL CHECK (quantity_available >= 0),
    discount DECIMAL(5, 2) DEFAULT 0 CHECK (discount >= 0 AND discount <= 100),
    PRIMARY KEY (store_id, product_id)
);

CREATE TABLE PreviousQueries (
    id SERIAL PRIMARY KEY,
    query_text TEXT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);