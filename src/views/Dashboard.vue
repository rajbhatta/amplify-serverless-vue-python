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
                  15
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
                  5
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
              <th class="px-4 py-3">Created At</th>
            </tr>
          </thead>
          <tbody
            class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800"
          >
            <tr class="text-gray-700 dark:text-gray-400">
              <td class="px-4 py-3">
                <div class="flex items-center text-sm">
                  <div>
                    <p class="font-semibold">
                      <router-link :to="'/sensors/' + 1"> 0xACAC </router-link>
                    </p>
                  </div>
                </div>
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center text-sm">Test Sensor Name</div>
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center text-sm">15</div>
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
                <div class="flex items-center text-sm">6/10/2020</div>
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
export default {
  name: "Home",
  components: {},
};
</script>
