CREATE TABLE records (
    id TEXT PRIMARY KEY,
    url TEXT,
    instruction TEXT,
    parsed_fields TEXT,
    extracted TEXT,
    confidence TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
