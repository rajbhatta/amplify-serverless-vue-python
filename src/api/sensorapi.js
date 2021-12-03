import { API } from "aws-amplify";

const getsensorbyid = (id) => {
    console.log(id)
    console.log('SENSOR ID IS RECEIVED')
}
const postsensor = (sensor) =>{
    var response = API.post("sensorapi", "/sensors", {
        body: {
          sensor_name: 'Heat Sens',
          model: 'HT',
          temperature: '15',
          operating_location: 'Vancouver',
        },
      });
      
    console.log(sensor)
    console.log(response)
    console.log('SENSOR IS RECEIVED')
}
const getsensor = () => {}

export { getsensor,postsensor,getsensorbyid}