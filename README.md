# 1. How project is created ? #
## 1.1 Install NPM ##
```js

```

## 1.2 Install VUE CLI ##
```js
sudo npm install -g @vue/cli
```

## 1.3 Create Vue Project using CLI ##
```js
 vue create clientmgmt
```

# 2. Add Vuex #
## 2.1 Add vuex ##
```js
vue add vuex
```

# 3. Install Tailwind CSS #
```js
vue add tailwind 
```

# 4. Install AWS Amplify dependency for UI #
```js
npm install aws-amplify @aws-amplify/ui-components
```
- Reference: https://docs.amplify.aws/start/getting-started/setup/q/integration/vue/#initialize-a-new-backend
- Make sure to run command:
```js 
amplify push -y
```
to make amplify available for UI

# 5. Dependencies and virtual environment setup inside lambda function #
```python
pipenv install aws-wsgi boto3 flask flask-cors psycopg2-binary SQLAlchemy SQLAlchemy-serializer
```

## 5.2 How to install dependencies ##
1. Go inside amplify folder (cd amplify)
2. Goto function (cd function)
3. Go inside sensorlambda (cd sensorlambda)
4. Run dependencies specified inside 1

## 5.3 How to mock lambda function with Amplify ##
```python
amplify mock function sensorlambdav3
```

# 6. Architecture diagrams #
## 6.1 Current AWS cloud design ##
<img src="Snapshots/current-design.png"/>

## 6.2 Alternative AWS cloud design ##
<img src="Snapshots/alternative-design.png"/>

# 7. API server flow design #
<img src="Snapshots/api-design.png"/>

# 8. Database Script #
## 8.1 Database script for creating table ##
```sql
-- Table: public.sensor

-- DROP TABLE public.sensor;

CREATE TABLE public.sensor
(
    id bigint NOT NULL DEFAULT nextval('sensor_id_seq'::regclass),
    hexid text COLLATE pg_catalog."default",
    name text COLLATE pg_catalog."default",
    temperature integer,
    location text COLLATE pg_catalog."default",
    CONSTRAINT sensor_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.sensor
    OWNER to postgres;
```

## 8.2 Database script for creating primary key using sequence ##
```sql
-- SEQUENCE: public.sensor_id_seq

-- DROP SEQUENCE public.sensor_id_seq;

CREATE SEQUENCE public.sensor_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.sensor_id_seq
    OWNER TO postgres;
```


# 8. Snapshots #
<img src="Snapshots/img1.png"/>
<img src="Snapshots/img2.png"/>

<img src="Snapshots/img7.png"/>
<img src="Snapshots/img8.png"/>
<img src="Snapshots/img9.png"/>

<img src="Snapshots/img4.png"/>
<img src="Snapshots/img3.png"/>
<img src="Snapshots/img5.png"/>
<img src="Snapshots/img6.png"/>
