PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE commands (
	id INTEGER NOT NULL,
	device_id INTEGER,
	target_name VARCHAR(256),
	function_name VARCHAR(256),
	ir_command VARCHAR(512),
	PRIMARY KEY (id),
	FOREIGN KEY(device_id) REFERENCES devices (id)
);
INSERT INTO commands VALUES(1,1,'TV','PowerCycle','2600320172390f0e0e2b0f0d0f0e0f0d0f0e0f0e0e0e0f0e0e0e0f0e0f0d0f0e0f2a0f0e0e0e0f0e0e0e0f0e0f0d0f0e0f0e0e0e0f2a0f0e0e0e0f0e0f0d0f0e0f0e0e0e0f0e0e2b0f0d0f2a0f2a0f2b0e2b0f0d0f0e0f2a0f0e0e2b0e2b0f2a0f2a0f0e0e2b0e00098c72390f0e0e2b0f0d0f0e0f0d0f0e0f0e0e0e0f0e0e0e0f0e0f0d0f0e0f2a0f0e0e0e0f0e0e0e0f0e0f0d0f0e0f0e0e0e0f2a0f0e0f0d0f0e0f0d0f0e0f0e0e0e0f0e0e2b0f0d0f2a0f2b0e2b0e2b0f0d0f0e0f2a0f0e0e2b0f2a0f2a0f2a0f0e0e2b0f00098b72390f0e0e2b0f0d0f0e0f0d0f0e0f0e0e0e0f0e0f0d0f0e0f0d0f0e0f2a0f0e0e0e0f0e0f0d0f0e0f0e0e0e0f0e0e0e0f2a0f0e0f0d0f0e0f0d0f0e0f0e0e0e0f0e0e2b0f0d0f2a0f2b0e2b0f2a0f0d0f0e0f2a0f0e0e2b0f2a0f2a0f2a0f0e0e2b0f000d05000000000000');
CREATE TABLE devices (
	id INTEGER NOT NULL,
	name VARCHAR(256),
	devtype INTEGER,
	host VARCHAR(256),
	mac_address VARCHAR(256),
	PRIMARY KEY (id)
);
INSERT INTO devices VALUES(1,'リビング',10039,'192.168.10.149','69c96f34ea34');
COMMIT;
