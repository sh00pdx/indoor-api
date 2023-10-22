-- Create user table
CREATE TABLE user (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    username VARCHAR(50),
    password VARCHAR(255),
    email VARCHAR(100),
    name VARCHAR(100)
);

-- Create equipment table
CREATE TABLE equipment (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT,
    internal_identifier INT,
    external_identifier CHAR(36),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    creation_date DATE,
    name VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

-- Create configuration table
CREATE TABLE configuration (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    equipment_id BIGINT,
    name VARCHAR(100),
    description TEXT,
    state ENUM('Active', 'Inactive'),
    config_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (equipment_id) REFERENCES equipment(id)
);

-- Create product_record table
CREATE TABLE product_record (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    equipment_id BIGINT,
    ambient_temperature DECIMAL(5, 2),
    ambient_humidity DECIMAL(5, 2),
    soil_temperature DECIMAL(5, 2),
    order_sent BOOLEAN,
    record_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (equipment_id) REFERENCES equipment(id)
);

-- Create configuration_change_history table
CREATE TABLE configuration_change_history (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    configuration_id BIGINT,
    new_state ENUM('Active', 'Inactive'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (configuration_id) REFERENCES configuration(id)
);
