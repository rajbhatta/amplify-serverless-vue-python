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
