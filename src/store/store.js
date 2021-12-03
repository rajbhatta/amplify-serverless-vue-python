import { createStore } from 'vuex'
import {postsensor,getsensor} from '@/api/sensorapi'

export default createStore({
  state: {
  },
  mutations: {
    SAVE_SENSOR(st, data){
      console.log(st)
      console.log(data)
    },
    GET_SENSOR(st, data){
      console.log(st)
      console.log(data)
    }
  },
  actions: {
    async submitsensor({commit}, sensor){
      await postsensor(sensor)
      commit("SAVE_SENSOR")
    },
    async getsensors({commit}){
      await getsensor()
      commit("GET_SENSOR")
    }
  },
  modules: {
  }
})
