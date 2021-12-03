import { API } from "aws-amplify";

const getsensorbyid = (id) => {
    console.log(id)
}
const postsensor = (sensor) => {
    API.post("equipmentapi", "/sensorsv3", {
        body: sensor
    })
    console.log(sensor)
}
const getsensor = () => API.get("equipmentapi", "/sensorsv3")

export { getsensor, postsensor, getsensorbyid }