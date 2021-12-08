-- Generado por Oracle SQL Developer Data Modeler 21.2.0.183.1957
--   en:        2021-10-12 15:48:17 CLST
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE administrador (
    id_administrador   INTEGER NOT NULL,
    id_pedido_producto INTEGER NOT NULL,
    id_usuario         INTEGER NOT NULL
);

ALTER TABLE administrador ADD CONSTRAINT finanzas_pk PRIMARY KEY ( id_administrador );

CREATE TABLE bodega (
    id_bodega   INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    stock       INTEGER NOT NULL,
    stockRecomendado       INTEGER NOT NULL
);

ALTER TABLE bodega ADD CONSTRAINT bodega_pk PRIMARY KEY ( id_bodega );

CREATE TABLE cliente (
    id_cliente INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    nombre_cliente INTEGER NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente );

CREATE TABLE cocina (
    id_cocina        INTEGER NOT NULL,
    id_pedido        INTEGER NOT NULL,
    id_estado_pedido INTEGER NOT NULL
);

ALTER TABLE cocina ADD CONSTRAINT cocina_pk PRIMARY KEY ( id_cocina );

CREATE TABLE estado_pedido (
    id_estado_pedido INTEGER NOT NULL,
    estado           INTEGER NOT NULL
);

ALTER TABLE estado_pedido ADD CONSTRAINT estado_pedido_pk PRIMARY KEY ( id_estado_pedido );

CREATE TABLE reserva (
    id_reserva   INTEGER NOT NULL,
    id_mesa INTEGER NOT NULL,
    rut_cliente INTEGER NOT NULL,
    cantidad_personas INTEGER NOT NULL,
    fecha INTEGER NOT NULL
);

ALTER TABLE reserva ADD CONSTRAINT reserva_pk PRIMARY KEY ( id_reserva );



CREATE TABLE mesa (
    id_mesa        INTEGER NOT NULL,
    disponibilidad INTEGER NOT NULL,
    capacidad CHAR(1) NOT NULL
);

ALTER TABLE mesa ADD CONSTRAINT mesapk PRIMARY KEY ( id_mesa );

CREATE TABLE reservado (
    id_reservado   INTEGER NOT NULL,
    id_mesa INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    cantidad_personas INTEGER NOT NULL,
    fecha INTEGER NOT NULL
);

ALTER TABLE reservado ADD CONSTRAINT reservado_pk PRIMARY KEY ( id_reservado );


CREATE TABLE mesa_estado (
    id_mesa_estado INTEGER NOT NULL,
    id_cliente     INTEGER NOT NULL,
    estado         INTEGER NOT NULL
);

ALTER TABLE mesa_estado ADD CONSTRAINT mesa_estadopk PRIMARY KEY ( id_mesa_estado );

CREATE TABLE pedido (
    id_pedido    INTEGER NOT NULL,
    id_mesa      INTEGER NOT NULL,
    fecha_pedido DATE NOT NULL,
    precio_total INTEGER NOT NULL
);

ALTER TABLE pedido ADD CONSTRAINT pedido_pk PRIMARY KEY ( id_pedido );

CREATE TABLE pedido_producto (
    id_pedido_producto INTEGER NOT NULL
);

ALTER TABLE pedido_producto ADD CONSTRAINT pedido_preveedor_pk PRIMARY KEY ( id_pedido_producto );

CREATE TABLE pedidos_producto_intermedio (
    id_producto_intermedio INTEGER NOT NULL,
    id_producto            INTEGER NOT NULL,
    id_pedido_producto     INTEGER NOT NULL,
    cantidad_producto      INTEGER NOT NULL
);

ALTER TABLE pedidos_producto_intermedio ADD CONSTRAINT pedidos_producto_intermedio_pk PRIMARY KEY ( id_producto_intermedio );

CREATE TABLE producto_receta (
    id_producto_receta INTEGER NOT NULL,
    id_receta          INTEGER NOT NULL,
    id_producto        INTEGER NOT NULL,
    cantidad_producto  INTEGER NOT NULL
);

ALTER TABLE producto_receta ADD CONSTRAINT producto_receta_pk PRIMARY KEY ( id_producto_receta );

CREATE TABLE productos (
    id_producto  INTEGER NOT NULL,
    id_proveedor INTEGER NOT NULL,
    nombre_producto VARCHAR2(30 CHAR),
    descripcion     VARCHAR2(30 CHAR)
);

ALTER TABLE productos ADD CONSTRAINT productos_pk PRIMARY KEY ( id_producto );

CREATE TABLE proveedor (
    id_proveedor     INTEGER NOT NULL,
    nombre_proveedor VARCHAR2(30 CHAR),
    rut_proveedor    INTEGER NOT NULL ,
    contacto         INTEGER NOT NULL ,
    apellido_proveedor VARCHAR2(30 CHAR)
);

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( id_proveedor );

CREATE TABLE receta (
    id_receta INTEGER NOT NULL,
    precio    INTEGER NOT NULL,
    nombre    VARCHAR2(30 CHAR),  
    descripcion VARCHAR2(30 CHAR)
);

ALTER TABLE receta ADD CONSTRAINT receta_pk PRIMARY KEY ( id_receta );

CREATE TABLE receta_pedido (
    id_receta_pedido INTEGER NOT NULL,
    id_receta        INTEGER NOT NULL,
    id_pedido        INTEGER NOT NULL,
    cantidad_receta  INTEGER NOT NULL
);

ALTER TABLE receta_pedido ADD CONSTRAINT receta_pedido_pk PRIMARY KEY ( id_receta_pedido );

CREATE TABLE usuarios (
    id_usuario INTEGER NOT NULL,
    nombre     VARCHAR2(10) NOT NULL,
    contrasena VARCHAR2(15) NOT NULL
);

ALTER TABLE usuarios ADD CONSTRAINT usuarios_pk PRIMARY KEY ( id_usuario );

ALTER TABLE reservado
    ADD CONSTRAINT reservado_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );
        
ALTER TABLE reservado
    ADD CONSTRAINT reservado_mesa_fk FOREIGN KEY ( id_mesa )
        REFERENCES mesa ( id_mesa );

ALTER TABLE administrador
    ADD CONSTRAINT administrador_usuarios_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuarios ( id_usuario );

ALTER TABLE bodega
    ADD CONSTRAINT bodega_productos_fk FOREIGN KEY ( id_producto )
        REFERENCES productos ( id_producto );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_usuarios_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuarios ( id_usuario );

ALTER TABLE cocina
    ADD CONSTRAINT cocina_estado_pedido_fk FOREIGN KEY ( id_estado_pedido )
        REFERENCES estado_pedido ( id_estado_pedido );

ALTER TABLE cocina
    ADD CONSTRAINT cocina_pedido_fk FOREIGN KEY ( id_pedido )
        REFERENCES pedido ( id_pedido );

ALTER TABLE administrador
    ADD CONSTRAINT finanzas_pedido_producto_fk FOREIGN KEY ( id_pedido_producto )
        REFERENCES pedido_producto ( id_pedido_producto );

ALTER TABLE pedidos_producto_intermedio
    ADD CONSTRAINT intermedio_pedido_producto_fk FOREIGN KEY ( id_pedido_producto )
        REFERENCES pedido_producto ( id_pedido_producto );

ALTER TABLE pedidos_producto_intermedio
    ADD CONSTRAINT intermedio_productos_fk FOREIGN KEY ( id_producto )
        REFERENCES productos ( id_producto );

ALTER TABLE mesa_estado
    ADD CONSTRAINT mesa_estado_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE pedido
    ADD CONSTRAINT pedido_mesa_fk FOREIGN KEY ( id_mesa )
        REFERENCES mesa ( id_mesa );

ALTER TABLE producto_receta
    ADD CONSTRAINT producto_receta_bodega_fk FOREIGN KEY ( id_producto )
        REFERENCES bodega ( id_bodega );

ALTER TABLE producto_receta
    ADD CONSTRAINT producto_receta_receta_fk FOREIGN KEY ( id_receta )
        REFERENCES receta ( id_receta );

ALTER TABLE productos
    ADD CONSTRAINT productos_proveedor_fk FOREIGN KEY ( id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE receta_pedido
    ADD CONSTRAINT receta_pedido_pedido_fk FOREIGN KEY ( id_pedido )
        REFERENCES pedido ( id_pedido );

ALTER TABLE receta_pedido
    ADD CONSTRAINT receta_pedido_receta_fk FOREIGN KEY ( id_receta )
        REFERENCES receta ( id_receta );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            15
-- CREATE INDEX                             0
-- ALTER TABLE                             30
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
