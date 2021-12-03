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

# 8. Script #
## 8.1 Database script for creating table ##
```sql
 
 1. Database/create.sql

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

2. Database/sequence.sql

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

## 8.3 API server: Lambda function with Flask server and PostGres ##
```python

4. amplify/backend/function/sensorlambdav3/src/index.py

from modal.sensor import Sensor
from sensorservice import SensorService
from dbhandler import DbHandler

import awsgi
import json
import logging
from os import error
import os

from flask_cors import CORS
from flask import Flask, app, jsonify, request


BASE_ROUTE ="/sensorsv3"

app = Flask(__name__)
CORS(app)

logger = logging.getLogger()

@app.route(BASE_ROUTE, methods=['POST'])
def create_customer():
    try:
        """
            PRODUCTION REQUEST VALUE
        """
        request_json = request.get_json()
        request_hex_id = request_json.get('hexid')
        request_name = request_json.get('name')
        request_temperature = request_json.get('temperature')
        request_location = request_json.get('location')

        """
            LOCAL TESTING
        """
        #request_hex_id = '0x123'
        #request_name = 'test name'
        #request_temperature = 15
        #request_location = 'Surrey'
    
        db_session = provide_database_session()
        sensor_service = SensorService(db_session)
        sensor_service.save_sensor(Sensor(name=request_name,hexid=request_hex_id,temperature=request_temperature, location =request_location))
    
        return jsonify(message='OK')
    except error as e:
         logger.critical(e)
         return jsonify(message='FAILED')
    

@app.route(BASE_ROUTE, methods=['GET'])
def list_customer():
    db_session = provide_database_session();

    # todo make list to json
    sensor_list =[]
    sensor_service = SensorService(db_session)
    sensors = sensor_service.get_sensor()
    for sensor in sensors:
        sensor_list.append(sensor.get_json)
    return sensor_list

def handler(event, context):
  logger.info('received event:')
  logger.info(event)
  return awsgi.response(app,event,context)

def provide_database_session():
    
    """ 
        PRODUCTION
    """
    dbusername = validate_db_username(os.environ.get("DB_USERNAME"))
    dbpassword = validate_db_password(os.environ.get("DB_PASSWORD"))
    dbhost = validate_db_host(os.environ.get("DB_HOST"))
    dbname = validate_db_name(os.environ.get("DB_NAME"))

    """
        LOCAL TESTING
    """
    #dbusername = validate_db_username('postgres')
    #dbpassword = validate_db_password('<Password>')
    #dbhost = validate_db_host('<I have terminated RDS>')
    #dbname = validate_db_name('postgres')

    dbhandler = DbHandler(logger,dbusername, dbpassword, dbhost , dbname)
    return dbhandler.get_orm_db_session()


def validate_db_username(username):
    if username != None:
        return username
    else:
        logger.critical("UNABLE TO GET DB USERNAME FROM ENVIRONMENT CONFIG")

def validate_db_password(password):
    if password != None:
        return password
    else:
        logger.critical("UNABLE TO GET DB PASSWORD FROM ENVIRONMENT CONFIG")

def validate_db_host(host):
    if host != None:
        return host
    else:
        logger.critical("UNABLE TO GET DB HOSTNAME FROM ENVIRONMENT CONFIG")

def validate_db_name(name):
    if name != None:
        return name
    else:
        logger.critical("UNABLE TO GET DB NAME FROM ENVIRONMENT CONFIG")
```

```python

4. amplify/backend/function/sensorlambdav3/src/sensorservice.py

from modal.sensor import Sensor
from sqlalchemy.orm.session import Session


class SensorService():

    def __init__(self, db_session):
        self.__db_session=db_session
    
    def save_sensor(self, sensor):
        self.__db_session.add(sensor)
        self.__db_session.commit()
        self.__db_session.flush()

    def get_sensor(self):
        return self.__db_session.query(Sensor).all()

    def get_sensor_by_id(self,id):
        return self.__db_session.query(Sensor).filter(Sensor.id == id).all()
```

```python

5. amplify/backend/function/sensorlambdav3/src/modal/sensor.py

from sqlalchemy import (
    Column,
    Text,
    Integer,
    Enum,
    BigInteger
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column('id',BigInteger, primary_key=True, unique=True, nullable=False)
    name = Column('name', Text, nullable=True)
    hexid = Column('hexid', Text, nullable=True)
    temperature = Column('temperature', Integer, nullable=True)
    location =  Column('location', Text, nullable=True)

```

```python 

6. amplify/backend/function/sensorlambdav3/src/dbhandler.py

from os import error
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbHandler():

    def __init__(self, logger, db_username, db_password, db_host, db_name):
        self.__logger =logger
        self.__db_username =db_username
        self.__db_password =db_password
        self.__db_host= db_host
        self.__db_name = db_name
    
    def get_orm_db_session(self):
        try:
            postgres_engine = create_engine(f'postgresql://{self.__db_username}:{self.__db_password}@{self.__db_host}:5432/{self.__db_name}')
            session = sessionmaker(bind=postgres_engine)()
            return session;
        except error as e:
            self.__logger.critical(e)
    
```

```python

6. amplify/backend/function/sensorlambdav3/src/Pipfile.lock

[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
src = {editable = true, path = "./src"}
aws-wsgi = "*"
boto3 = "*"
flask = "*"
flask-cors = "*"
psycopg2-binary = "*"
sqlalchemy = "*"

[requires]
python_version = "3.8"
```

```js

6. amplify/backend/function/sensorlambdav3/src/event.json

{ "httpMethod": "POST", "path":"/sensorsv3","queryStringParameters":""}

```

## 8.4 UI with Vuex and TailWindCss: ##
```js

7. src/api/sensorapi.js

import { API } from "aws-amplify";

const getsensorbyid = (id) => {
    console.log(id)
}
const postsensor = (sensor) => {
    API.post("equipmentapi", "/sensorsv3", {
        body: sensor
    })
}
const getsensor = () => API.get("equipmentapi", "/sensorsv3")

export { getsensor, postsensor, getsensorbyid }
```

```js

7. src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/add',
    name: 'Add',
    component: () => import('../views/Add.vue')
  },
  {
    path: '/sensors/:id',
    name: 'Sensors',
    
    component: () => import('../views/Sensors.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

```

```js

8. src/store/store.js

import { createStore } from 'vuex'
import { postsensor, getsensor } from '@/api/sensorapi'

export default createStore({
  state: {
    sensors: []
  },
  mutations: {
    SAVE_SENSOR_INVOKED(response) {
      /* todo: write commit message here */
      console.log(response)
    },
    GET_SENSOR_INVOKED(data) {
       /* todo: write commit message here */
      console.log(data)
    }
  },
  actions: {
    async submitsensor({commit}, sensor) {
      try {
        const response = await postsensor(sensor)
        commit("SAVE_SENSOR_INVOKED", response)
      } catch (error) {
        /* todo: create exception handling class and pass this error */
        console.log(error)
      }
    },
    async getsensors({commit}) {
      try {
        const response = await getsensor()
        this.state.sensors = response
        commit("GET_SENSOR_INVOKED", response)
      } catch (error) {
        /* todo: create exception handling class and pass this error */
        console.log(error)
      }
    }
  }
})


```

```html

9. src/view/Dashboard.vue

<template>
  <!-- start of container setup -->
  <div class="container mx-auto">
    <div class="main-content flex-1 bg-gray-100 mt-12 md:mt-2 pb-18 md:pb-5">
      <div class="flex flex-wrap">
        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
          <!--Metric Card-->
          <div
            class="
              bg-gradient-to-b
              from-green-200
              to-green-100
              border-b-4 border-green-600
              rounded-lg
              shadow-xl
              p-5
            "
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded-full p-5 bg-green-600">
                  <i class="fa fa-wallet fa-2x fa-inverse"></i>
                </div>
              </div>
              <div class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-600">
                  Total Sensors Record Counts
                </h5>
                <h3 class="font-bold text-3xl">
                  {{loadSensorInfo().length}}
                  <span class="text-green-500"
                    ><i class="fas fa-caret-up"></i
                  ></span>
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
          <!--Metric Card-->
          <div
            class="
              bg-gradient-to-b
              from-pink-200
              to-pink-100
              border-b-4 border-pink-500
              rounded-lg
              shadow-xl
              p-5
            "
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded-full p-5 bg-pink-600">
                  <i class="fas fa-users fa-2x fa-inverse"></i>
                </div>
              </div>
              <div class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-600">Total Sensors</h5>
                <h3 class="font-bold text-3xl">
                  {{loadSensorInfo().length}}
                  <span class="text-pink-500"
                    ><i class="fas fa-exchange-alt"></i
                  ></span>
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
          <!--Metric Card-->
          <div
            class="
              bg-gradient-to-b
              from-yellow-200
              to-yellow-100
              border-b-4 border-yellow-600
              rounded-lg
              shadow-xl
              p-5
            "
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded-full p-5 bg-yellow-600">
                  <i class="fas fa-user-plus fa-2x fa-inverse"></i>
                </div>
              </div>
              <div class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-600">
                  Working Sensors
                </h5>
                <h3 class="font-bold text-3xl">
                  2
                  <span class="text-yellow-600"
                    ><i class="fas fa-caret-up"></i
                  ></span>
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
      </div>
    </div>
  </div>
  <!-- end of container setup -->

  <!-- start of table -->
  <div class="container grid px-6 mx-auto">
    <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
      Sensor Details
    </h2>

    <div class="w-full overflow-hidden rounded-lg shadow-xs">
      <div class="w-full overflow-x-auto">
        <table class="w-full whitespace-no-wrap">
          <thead>
            <tr
              class="
                text-xs
                font-semibold
                tracking-wide
                text-left text-gray-500
                uppercase
                border-b
                dark:border-gray-700
                bg-gray-50
                dark:bg-gray-800
              "
            >
              <th class="px-4 py-3">Sensor ID</th>
              <th class="px-4 py-3">Sensor Name</th>
              <th class="px-4 py-3">Temperature (°C)</th>
              <th class="px-4 py-3">Status</th>
              <th class="px-4 py-3">Location</th>
            </tr>
          </thead>
          <tbody
            class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800"
          >
            <tr class="text-gray-700 dark:text-gray-400" v-for="sensor in loadSensorInfo()" v-bind:key="sensor.hexid">
              <td class="px-4 py-3">
                <div class="flex items-center text-sm">
                  <div>
                    <p class="font-semibold">
                      <router-link :to="'/sensors/' + 1"> {{sensor.hexid}} </router-link>
                    </p>
                  </div>
                </div>
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center text-sm">{{sensor.name}}</div>
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center text-sm">{{sensor.temperature}}</div>
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center text-sm">
                  <span
                    class="
                      px-2
                      py-1
                      font-semibold
                      leading-tight
                      text-green-700
                      bg-green-100
                      rounded-full
                      dark:text-green-100
                    "
                  >
                    Working
                  </span>
                </div>
              </td>

              <td class="px-4 py-3">
                <div class="flex items-center text-sm">{{sensor.location}}</div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <!-- end of table -->
</template>

<script>
import { mapActions} from "vuex";

export default {
  data() {
    return {
      
    };
  },
  methods: {
    ...mapActions(["getsensors"]),
    loadSensorInfo(){
      return this.$store.state.sensors;
    }
  },
  async mounted() {
    this.getsensors();
  }
};
</script>

```

```html

10. src/view/Add.vue

<template>
  <div class="container mx-auto grid">
    <h4 class="mb-4 text-lg text-purple-800">Please Add Sensor</h4>

    <div class="min-h-scree flex item-center justify-center">
      <!--start of form -->
      <div class="bg-white p-8 rounded shadow-2xl w-1/2">
        <form class="space-y-10">
          <div class="mb-3">
            <label for="hexId" class="mr-2">HexId</label>
            <input
              type="text"
              v-model="sensor.hexid"
              class="
                w-full
                border-2 border-gray-400
                p-3
                rounded
                outline-none
                focus:border-blue-500
              "
              placeholder="Please enter sensor hex id.."
            />
          </div>
          <div class="mb-3">
            <label for="hexId" class="mr-2">Name</label>
            <input
              type="text"
              v-model="sensor.name"
              class="
                w-full
                border-2 border-gray-400
                p-3
                rounded
                outline-none
                focus:border-blue-500
              "
              placeholder="Please enter sensor name.."
            />
          </div>
          <div class="mb-3">
            <label for="hexId" class="mr-2">Location</label>
            <input
              type="text"
              v-model="sensor.location"
              class="
                w-full
                border-2 border-gray-400
                p-3
                rounded
                outline-none
                focus:border-blue-500
              "
              placeholder="Please enter sensor location.."
            />
          </div>
          <div class="mb-3">
            <label for="hexId" class="mr-2">Temperature</label>
            <input
              type="text"
              v-model="sensor.temperature"
              class="
                w-full
                border-2 border-gray-400
                p-3
                rounded
                outline-none
                focus:border-blue-500
              "
              placeholder="Please enter sensor temperature.."
            />
          </div>
          <button
            type="button"
            class="block w-full bg-green-400 p-4 rounded"
            v-on:Click="submitForm()"
          >
            Submit
          </button>
        </form>
      </div>
      <!-- end of form -->
    </div>
  </div>
</template>

<script>
import { mapActions} from "vuex";

export default {
  data() {
    return {
      sensor: {
        hexid: "",
        name: "",
        location: "",
        temperature: "",
      },
    };
  },
  methods: {
    ...mapActions(["submitsensor", "getsensors"]),
    submitForm() {
      this.submitsensor(this.sensor);
    },
  }
};
</script>
```



# 9. Snapshots #
<img src="Snapshots/img1.png"/>
<img src="Snapshots/img2.png"/>

<img src="Snapshots/img7.png"/>
<img src="Snapshots/img8.png"/>
<img src="Snapshots/img9.png"/>

<img src="Snapshots/img4.png"/>
<img src="Snapshots/img3.png"/>
<img src="Snapshots/img5.png"/>
<img src="Snapshots/img6.png"/>
