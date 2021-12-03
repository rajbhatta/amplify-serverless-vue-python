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
          <button type="button" class="block w-full bg-green-400 p-4 rounded" v-on:Click="submitForm()">Submit</button>
        </form>
      </div>
      <!-- end of form -->
    </div>
  </div>
</template>

<script>
import {mapActions } from 'vuex'

export default {
    methods: {
        ...mapActions(['submitsensor','getsensors']),
        submitForm() {
          this.submitsensor()
        }
    }
};
</script>